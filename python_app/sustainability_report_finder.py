import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import requests
import time
import random
from pathlib import Path

SERPAPI_KEY = "YOUR_SERPAPI_KEY"  # placeholder: replace with a valid key

class SustainabilityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sustainability Report Finder")
        self.file_path = tk.StringVar()
        self.output_folder = tk.StringVar()
        self.year_from = tk.IntVar(value=2020)
        self.year_to = tk.IntVar(value=2023)
        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.root, padx=10, pady=10)
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Button(frame, text="Seleziona Excel", command=self.select_file).grid(row=0, column=0, pady=5, sticky="ew")
        ttk.Entry(frame, textvariable=self.file_path, width=40).grid(row=0, column=1, padx=5)

        ttk.Label(frame, text="Anno da").grid(row=1, column=0, sticky="e")
        ttk.Entry(frame, textvariable=self.year_from, width=10).grid(row=1, column=1, sticky="w")

        ttk.Label(frame, text="Anno a").grid(row=2, column=0, sticky="e")
        ttk.Entry(frame, textvariable=self.year_to, width=10).grid(row=2, column=1, sticky="w")

        ttk.Button(frame, text="Seleziona cartella output", command=self.select_output_folder).grid(row=3, column=0, pady=5, sticky="ew")
        ttk.Entry(frame, textvariable=self.output_folder, width=40).grid(row=3, column=1, padx=5)

        ttk.Button(frame, text="Avvia ricerca", command=self.run).grid(row=4, column=0, columnspan=2, pady=10)

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
        if file_path:
            self.file_path.set(file_path)

    def select_output_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_folder.set(folder)

    def run(self):
        if not self.file_path.get() or not self.output_folder.get():
            messagebox.showwarning("Attenzione", "Seleziona un file Excel e una cartella di output")
            return
        try:
            df = pd.read_excel(self.file_path.get())
        except Exception as e:
            messagebox.showerror("Errore", f"Impossibile leggere il file Excel: {e}")
            return
        companies = df.iloc[:, 0].dropna().astype(str).tolist()
        results = []
        for company in companies:
            for year in range(self.year_from.get(), self.year_to.get() + 1):
                query = f"{company} sustainability report {year}"
                url = self.search_google(query)
                if url:
                    results.append({"company": company, "year": year, "url": url})
                time.sleep(random.uniform(1, 3))
        if results:
            out_path = Path(self.output_folder.get()) / "report_links.xlsx"
            pd.DataFrame(results).to_excel(out_path, index=False)
            messagebox.showinfo("Completato", f"Risultati salvati in {out_path}")
        else:
            messagebox.showinfo("Nessun risultato", "Non sono stati trovati report")

    def search_google(self, query):
        # Questa funzione usa SerpAPI, un servizio che consente di eseguire ricerche su Google
        params = {
            "api_key": SERPAPI_KEY,
            "engine": "google",
            "q": query,
            "num": 1
        }
        try:
            response = requests.get("https://serpapi.com/search", params=params, timeout=30)
            response.raise_for_status()
            data = response.json()
            organic = data.get("organic_results")
            if organic:
                return organic[0].get("link")
        except Exception as e:
            print(f"Errore durante la ricerca di '{query}': {e}")
        return None


def main():
    root = tk.Tk()
    SustainabilityApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
