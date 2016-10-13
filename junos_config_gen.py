# Import librarys
#################
from jinja2 import Environment, FileSystemLoader
import yaml

# Global Variables
##################

# Script Actions
################


def GenerateConfig(ConfigVariables):
	env = Environment(loader=FileSystemLoader('./templates/'))
	template = env.get_template('base_config.txt')
	print template.render(ConfigVariables)

def LoadYamlFile():
	with open('templates/snmp.yaml') as _:
		ConfigVariables = yaml.load(_)
		GenerateConfig(ConfigVariables)

if __name__ == '__main__':
	LoadYamlFile()