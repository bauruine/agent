# README

## upd89 Agent

upd89 is a system update management for debian based systems.

## Dependencies

this upd89-agent is a python module, it's depending on the python-apt package

## Installation from github

	apt install python-apt python-daemonize python-configparser
	git clone https://github.com/upd89/agent.git
	python setup.py build
	python setup.py install
	update-rc.d upd89 defaults

## Installation from pip

	pip install upd89
	update-rc.d upd89 defaults

## Configuration

Please customize /etc/upd89/config.ini for you needs
