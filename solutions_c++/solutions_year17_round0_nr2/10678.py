#include<iostream>
#include<stdio.h>
#include<fstream>
#include<bits/stdc++.h>
using namespace std;
int main()
{
        freopen("tempin1.in", "r", stdin);
        freopen("tempout.txt", "w", stdout);
    int test,i,j,k,testnum,dig,num,digprev,flag,counter,notest;
notest=0;
    cin>>test;
    while(test--)
    {
      cin>>num;
      notest++;
      for(i=num;i>0;i--)
      {   testnum=i;
     // digprev=0;
     flag=0;
      counter=0;
        while(testnum)
        {  counter++;
            dig=testnum%10;
            if(counter==1)
            {
            digprev=dig;
            testnum=testnum/10;
            continue;
            } else
            if(!(digprev>=dig))
            {
                flag=1;
                break;
            }
            digprev=dig;
            testnum=testnum/10;
        }
        if(flag==0)
            break;
      }
      cout<<"Case #"<<notest<<": "<<i<<endl;


    }
    return 0;
    }

