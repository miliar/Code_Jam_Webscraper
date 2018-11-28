using namespace std;
#include<iostream>
#include<stdio.h>
#include<math.h>
#include<bits/stdc++.h>
int main()
{freopen("input.in","r",stdin); // command to open file and read input
freopen("largepancake.out","w",stdout);// command to write in a file
    int testing,mini,control;
    string arr;
    cin>>testing;

                for(int q=1;q<=testing;q++)
                    {   control=0; cin>>arr;   cin>>mini;
                        for(int i=0;i<arr.length();i++)
                    {   if(arr[i]=='-') {   control++; for(int j=i;j<i+mini;j++)//to evaluate that it doesn't go out of bound
                                    {  if(j>=arr.length())
                                        control = -1;
                                        if(arr[j]=='-')
                                            arr[j]='+';     // to interchange
                                                    else arr[j]='-'; }}}
                                if(control==-1)//to check for UNPOSSIBLE CASES
                                    cout<<"Case #"<<q<<": IMPOSSIBLE"<<endl;
                                           else //TO print out minimum variable
                                            cout<<"Case #"<<q<<": "<<control<<endl;}return 0;}
