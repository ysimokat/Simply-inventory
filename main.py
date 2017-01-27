#!/usr/bin/env python
""" file: main.py
    ask user input number of sizes
    store inventory data in to a list
    finding the row sum
    finding the col sum
    finding the grand total
    print output to the screen
"""
import numpy as np

def user_input(college):
    """ ask user enter the number of sweatshirts in each size """
    L = [] # empty list
    c = 'for College %d: ' % (college)
    s = input("%s Enter the number of small size: "%(c))
    m = input("%s Enter the number of medium size: "%(c))
    l = input("%s Enter the number of large size: "%(c))
    xl = input("%s Enter the number of X-large size: "%(c))
    L.extend([s,m,l,xl])
    print L
    print "----------------------------------------------------------"
    return L

def get_list2d():
    """ get an array contain 7 lists
        each list contain size of s,m,l,xl
    """
    a = np.array([user_input(i+1) for i in range(7)]) # get data
    return a   #an array,contain 7 lists

def row_sum(a,row,col):
    """ calculate sum of each row """
    for j in range(col):
        for i in range(row):
            b = a.sum(axis=1) #sum of each row
    return b

def col_sum(a,row,col):
    """ calculate sum of each column """
    for i in range(row):
        for j in range(col):
            c = a.sum(axis=0)  #sum of each column
    return c

def grand_total(a,row,col):
    """ calculate total sweatshirts """
    for i in range(row):
        for j in range(col):
            tot = a.sum() # sum all
    return tot

def print_header():
    """ print output header """
    head1 = "Inventory Report"
    head2 = "College"
    print ("%+55s" % str(head1))
    print
    print ("%+50s" % str(head2))
    print 
    print "%25d"%1,"%7d"%2,"%7d"%3,"%7d"%4,"%7d"%5,"%7d"%6,"%7d"%7,"%14s"%("Size Total")
    return head1,head2

def print_small(a,c):
    """ print a row of small size from 7 colleges"""
    s = a[0:7,0] #slice first col from each row,small
    s = list(s)
    print
    print "\tSmall\t\t",("\t" .join(map(str,s))),"\t",c[0]
    print
    return 

def print_medium(a,c):
    """ print a row of medium size from 7 colleges """
    m = a[0:7,1] #slice second col from each row,medium
    m = list(m)
    print "\tMedium\t\t",("\t" .join(map(str,m))),"\t",c[1]
    print
    return m

def print_size(): 
    """ a row called size between M&L """
    head = "Size"
    print ("%s" % str(head))
    return head

def print_large(a,c):
    """ print a row of large size from 7 colleges """
    l = a[0:7,2] #slice third col from each row,size large
    l = list(l)
    print "\tLarge\t\t",("\t" .join(map(str,l))),"\t",c[2]
    print
    return l

def print_xlarge(a,c):
    """ print a row of Xlarge size from 7 colleges """
    xl = a[0:7,3] #slice size xl data from array
    xl = list(xl)
    print "\tXlarge\t\t",("\t" .join(map(str,xl))),"\t",c[3]
    print
    return xl

def print_coltotal(b):
    """ print a row of total sweatshirts from each college """ 
    #print type(b) #for debugging
    total = list(b)
    print "\tCollege Total\t",("\t" .join(map(str,total)))
    print
    return total

def print_total(tot):
    """ print total inventory of all sweatshirts """
    t = tot
    print ("%+55s" % str("Total Quantity On Hand = ") + str(t))
    return t

def main():
    """ main function """
    row = 4
    col = 7 
    a = get_list2d()
    b = row_sum(a,row,col)
    c = col_sum(a,row,col)
    tot = grand_total(a,row,col)
    header = print_header()
    small = print_small(a,c)
    medium = print_medium(a,c)
    size = print_size()
    large = print_large(a,c)
    xlarge = print_xlarge(a,c)
    coltotal = print_coltotal(b)
    t = print_total(tot)
if __name__ == "__main__":
    main()
