# JunOS-Templates
Repo for playing with JunOS based configuration files to be templated with Jinja2

### Tree ###
JunOS-Templates
    ├── README.md
    ├── base_config.txt
    ├── junos_config_gen.py
    ├── requirements.txt
    └── templates
        └── snmp.j2

### Setup ###
sudo pip install -r requirements.txt

### Run ###
python junos_template_gen.py