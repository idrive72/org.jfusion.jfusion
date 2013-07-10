<?php

/**
 * This is view file for cpanel
 *
 * PHP version 5
 *
 * @category   JFusion
 * @package    Joomla.Administrator
 * @subpackage com_jfusion
 * @author     JFusion Team <webmaster@jfusion.org>
 * @copyright  2008 JFusion. All rights reserved.
 * @license    http://www.gnu.org/copyleft/gpl.html GNU/GPL
 * @link       http://www.jfusion.org
 */
// no direct access
defined('_JEXEC') or die('Restricted access');

/**
 * JFusion component helper.
 *
 * @package		Joomla.Administrator
 * @subpackage	com_jfusion
 * @since		1.6
 */

class JFusionHelper
{
	/**
	 * Configure the Linkbar.
	 *
	 * @param	string	The name of the active view.
	 *
	 * @return	void
	 * @since	1.6
	 */
	public static function addSubmenu($vName)
	{
        $jname = JFactory::getApplication()->input->get('jname');
		JHtmlSidebar::addEntry(
			JText::_('CPANEL'),
			'index.php?option=com_jfusion&task=cpanel',
			$vName == 'cpanel'
		);

		JHtmlSidebar::addEntry(
			JText::_('JOOMLA_OPTIONS'),
			'index.php?option=com_jfusion&task=plugineditor&jname=joomla_int',
			$vName == 'plugineditor' && $jname == 'joomla_int'
		);

		JHtmlSidebar::addEntry(
			JText::_('CONFIGURATION'),
			'index.php?option=com_jfusion&task=plugindisplay',
			$vName == 'plugindisplay' || ( $vName == 'plugineditor' && $jname != 'joomla_int' )
		);

		JHtmlSidebar::addEntry(
			JText::_('NEW_USERSYNC'),
			'index.php?option=com_jfusion&task=syncoptions',
			$vName == 'syncoptions'
		);

		JHtmlSidebar::addEntry(
			JText::_('USERSYNC_HISTORY'),
			'index.php?option=com_jfusion&task=synchistory',
			$vName == 'synchistory'
		);

		JHtmlSidebar::addEntry(
			JText::_('LOGIN_CHECKER'),
			'index.php?option=com_jfusion&task=loginchecker',
			($vName == 'loginchecker'||$vName == 'logincheckerresult'||$vName == 'logoutcheckerresult')
		);

		JHtmlSidebar::addEntry(
				JText::_('CONFIG_DUMP'),
				'index.php?option=com_jfusion&task=configdump',
				$vName == 'configdump'
		);

		JHtmlSidebar::addEntry(
            JText::_('LANGUAGE'),
            'index.php?option=com_jfusion&task=languages',
            $vName == 'languages'
        );

		JHtmlSidebar::addEntry(
			JText::_('VERSIONS'),
			'index.php?option=com_jfusion&task=versioncheck',
			$vName == 'versioncheck'
		);
	}
}