#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
void check(string &s,int k,int j);
void compute(string &s,int j);
int c=0,m=0,con=1;
int main()
{
    int t;
    cin>>t;
    while(t>0)
    {
        string s;
        cin>>s;
        int j;
        cin>>j;
        compute(s,j);
        t--;
        con++;
    }
}
void compute(string &s,int j)
{
    int i;
    for(i=0;i<s.length();i++)
    {
        if(s[i]=='-'){
            check(s,i,j);
            c++;
        }
    }
    if(m==0)
    cout<<"Case #"<<con<<": "<<c<<'\n';
    else
        cout<<"Case #"<<con<<": "<<"IMPOSSIBLE"<<'\n';
    c=0;m=0;
}
void check(string &s,int k,int j)
{
    int i;
    if(k+j>s.length()){
        m=-1;
    }
    for(i=k;i<k+j;i++)
    {
        if(s[i]=='-')
            s[i]='+';
        else
            s[i]='-';
    }
}
