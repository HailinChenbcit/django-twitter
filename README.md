## Django-twitter Project

- [General info](#general-info)
- [Content](#content)
- [Technologies](#technologies)
- [Resources](#resources)
- [How To Run WorryLess Locally](#how-to-run-worryless-locally)
- [Features](#features)
- [Attribution](#attribution)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

## General Info

### Project Title 
Django-twitter Project

### Project Description
This is my personal project focusing on backend development of a twitter-like system.


### The Team
- Hailin(Adam) Chen - github: https://github.com/HailinChenbcit

## Content

Content of the project folder:

```
Top level of project folder:
│   .gitignore
│   bionic64.box
│   db.sqlite3
│   manage.py
│   mysql-apt-config_0.8.15-1_all.deb
│   provision.sh
│   README.md
│   requirements.txt
│   Vagrantfile
├───.idea
├───.vagrant
├───accounts
├───comments
├───friendships
├───inbox
├───likes
├───newsfeeds
├───testing
├───tweets
├───twitter
└───utils

```

## Technologies

Technologies used for this project:
- Used Push model to implement fanout news feed feature
- Django-Framework
- MySQL
- Hbase: Key-value store to split db queries for tables which ahs less reads and lot writes
- Redis, Memcached: Reduce db queries for tables Which has lot reads and less writes
- Amazon S3 
- Message Queue: for async tasks, reduce response times
- Rest API 
- Serialization, 
- Database Renormalization

## How to run locally
1. Download Vagrant
```
https://www.vagrantup.com/downloads
```
2. Create virtual machine and config development environment
```
https://app.vagrantup.com/hashicorp/boxes/bionic64
Rename the file as 'bionic64.box'
```
3. Add bionic64.box mirror to Vagrant
```
vagrant box add hashicorp/bionic64 bionic64.box
```
4. Config VM
```
Copy 
    Vagrantfile     - VM config file
    requirements.txt    - python dependencies pacakage 
    provision.sh    - shell script to initiate developent environment
    mysql-apt-config_0.8.15-1_all.deb   - mySql config file
to source directory
```
5. start VM and login to VM
```
## python 3.6.9    django 3.1.3
vagrant up
vagrant ssh
```

6. Reconnect to VM and start server
```
cd /vagrant
python manage.py runserver 0.0.0.0:8000
```

## Features
- Signup new account
- Post a tweet
- Like/Dislike tweets
- Add friend
- Comment on a tweet
- Newsfeeds
- Inbox to receive DM

## Attribution
- Django: https://www.djangoproject.com/
- Redis: https://redis.io/
- Vagrant: https://www.vagrantup.com/

## Contact
Hailin Chen - hchen256@my.bcit.ca  
LinkedIn: https://www.linkedin.com/in/hailin-c-75655a165/

