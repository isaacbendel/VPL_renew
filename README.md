# VPL_renew #
Script to automatically renew books from Vaughan Public Library

I got sick of paying fines every month for overdue books. Especially as my kids take out two dozen books at a time :-)

So you can enter a list of all your login info, and this script will login, renew everything, and save a screenshot so that you can be sure that it worked properly.

This is a `python` script, so you need to have `python` installed on your machine. You will also need to install the `selenium` package (you can use `pip`), and download the `chromedriver` utility.

You can set this up using `cron` (or whatever) to run every week, and no more needing to be on top of renewing books.



There are a few parameters you have to set at the top of the file;
```
PATH_TO_CHROMEDRIVER = '/home/user/Downloads/chromedriver'
LOGIN_INFO = [('LIBRARYCARD1','PIN1'),('LIBRARYCARD2','PIN2')]
PATH_FOR_SCREENSHOTS = '/home/user/Pictures'
TIME_FACTOR = 1
```

`TIME_FACTOR`: Often with automated browsing a site takes a little longer to load, and that throws off the whole script. So I've added a 'wait factor' here. The time settings as they are worked fine when I was writing this, but if errors start occuring - you can just increase this value (to 1.5 or 2) and it should take care of the issue.

## Success ##
![alt text](https://github.com/isaacbendel/VPL_renew/blob/master/Renewal_for_account_XXXXXXXXXXX_on_08-09-17.png "")


