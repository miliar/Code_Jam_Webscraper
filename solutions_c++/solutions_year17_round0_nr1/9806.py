using namespace std;
#include<iostream>
#include<stdio.h>
#include<math.h>
#include<bits/stdc++.h>
int main()
{freopen("input.in","r",stdin); // command to open file and read dinput
freopen("mynumbers.out","w",stdout);// command to write in a file
    int testcase,kd,control_var,in;
    string str;
    cin>>testcase;

                for(int q=1;q<=testcase;q++)
                    {   control_var=0;
                cin>>str;   cin>>kd;
                        for(int i=0;i<str.length();i++)
                    {   if(str[i]=='-')
                        {   control_var++;
                                for(int j=i;j<i+kd;j++)
                                    {  if(j>=str.length())
                                        control_var = -1;
                                        if(str[j]=='-')
                                            str[j]='+';
                                                    else
                                                str[j]='-';
                                    }}}
        if(control_var==-1)//to check for UNPOSSIBLE CASES
            cout<<"Case #"<<q<<": IMPOSSIBLE"<<endl;
        else //TO print out minimum variable
            cout<<"Case #"<<q<<": "<<control_var<<endl;}}
