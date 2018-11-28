using namespace std;
#include<iostream>
#include<stdio.h>
#include<math.h>
#include<bits/stdc++.h>
int main()
{freopen("input.in","r",stdin); // command to open file and read input
freopen("largepancake.out","w",stdout);// command to write in a file
int testing,astrum,control;string arrange;cin>>testing;
for(int q=1;q<=testing;q++){control=0;cin>>arrange;cin>>astrum;
for(int i=0;i<arrange.length();i++){if(arrange[i]=='-'){control++; for(int j=i;j<i+astrum;j++)//to evaluate that it doesn't go out of bound
{if(j>=arrange.length())
control = -1;if(arrange[j]=='-')
arrange[j]='+';else arrange[j]='-'; }}}if(control==-1)//to check for UNPOSSIBLE CASES
cout<<"Case #"<<q<<": IMPOSSIBLE"<<endl;
else cout<<"Case #"<<q<<": "<<control<<endl;}return 0;}
