genEnv
====================

This package installs scripts that can run from the command line. The script generates an `env` file to be used with `docker run` and a `env_local` file for setting local terminal environment variables.


## Install

        pip install https://github.com/mbstacy/py-local-env/zipball/main

## Upgrade

        pip install https://github.com/mbstacy/py-local-env/zipball/main  -U


## Operation

Must be logged into the appropriate AWS account for secrets  `stack/secretname` to exist.

        $ genEnv --help
                usage: genEnv [-h] [-s STACK] [-f FILENAME]

                Create 'env' file for local development.

                optional arguments:
                -h, --help            show this help message and exit
                -s STACK, --stack STACK
                                        stack(default=`dev`)
                -f FILENAME, --filename FILENAME
                                        Specific ansible yaml file. Default: {current directory}/ansible_vars/{ stack }_ansible_vars.yml
        $ # default stack=dev
          # default file location
          # {current directory}/ansible_vars/{ stack }_ansible_vars.yml
        $ genEnv
        $ genEnv -s stage 
        The requested secret stage/apigee-nonprod-common@harvard.edu was not found

The last example is the result of logging into AWS Dev vs Prod AWS account. `stage` is in Prod AWS account.
### Outputs two files
ALWAYS ADD FILES TO `.gitignore`. Never commit files to code repository.

* .env : docker env file `docker run --env-file ./.env -it {{ image }}`
* .env_local : `. .env_local`
