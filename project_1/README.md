README v0.0 / 02 MARCH 2019

# Project 1

## Introduction

The purpose of this code is to access a PSQL database `news` and determine
the top three articles and their respective views, the top authors with their
respective views, and the days during which the ratio of request errors to
requests was greater than 1 percent.

We use two programs to obtain this information the first program
project_1_views.py contains code to set up a view called `pathview` which
contains a table consisting of two fields the path and the requests to that
path. project_1.py is our main code which uses the `pathview` view created
above to obtain our information.

## Usage
In order to use the program first navigate to the file in your console.

Now the main program uses a view called `pathview` which hasn't been created
yet. In order to create it simply use the command `python3 project_1_views.py`.
Now we can run our main code `python3 project_1.py`. If you use the command
`python project_1.py` and the python version associated with `python` is a
python version before 3 the print commands will not work.

### Requirements
Python version should be version 3 or greater. Below your version should be the
first entry.
```
vagrant@vagrant:/vagrant/project_1$ python3 --version
Python 3.5.2
vagrant@vagrant:/vagrant/project_1$ python --version
Python 2.7.12
```
