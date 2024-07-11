genLocalEnvFile
====================

This package installs scripts that can run from the command line. In addition, the script generates a `.env` file. File format options(-t) for `Shell` and `Docker`. 

## Install

        pip install https://github.com/harvard-huit/pyLocalEnv/zipball/main

## Upgrade

        pip install https://github.com/harvard-huit/pyLocalEnv/zipball/main  -U


## Operation

Must be logged into the appropriate AWS account for secrets  `stack/secretname` to exist.

        $ genLocalEnvFile -h
                usage: genLocalEnvFile [-h] [-s STACK] [-t TYPE] [-f FILENAME]

                Create 'env' file for local development.

                options:
                -h, --help            show this help message and exit
                -s STACK, --stack STACK 
                                stack(default='dev')
                -t TYPE, --type TYPE  Type of file creation shell or docker(default='docker')
                -f FILENAME, --filename FILENAME
                                Specific filename to pass in k8s variable yaml file. Default: {current directory}/k8s_vars/{stack}_k8s_vars.yml
        $ # default stack=dev
          # default file location
          # {current directory}/ansible_vars/{ stack }_ansible_vars.yml
        $ genLocalEnvFile
        $ genLocalEnvFile -s stage 
        The requested secret stage/apigee-nonprod-common@harvard.edu was not found

The last example is the result of logging into AWS Dev vs Prod AWS account. `stage` is in Prod AWS account.
### Outputs two files
ALWAYS ADD FILES TO `.gitignore`. Never commit files to code repository.

* .env : docker env file or shell env vars
