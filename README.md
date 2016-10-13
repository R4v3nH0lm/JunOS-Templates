# JunOS-Templates
Repo for playing with JunOS based configuration files to be templated with Jinja2

## Setup ##
`sudo pip install -r requirements.txt`

## Run ##
`python junos_template_gen.py`

## Tree ##
JunOS-Templates

├── README.md
├── junos_config_gen.py
├── requirements.txt
└── templates
    ├── base_config.txt
    ├── snmp.j2
    └── snmp.yaml