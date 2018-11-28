#include <bits/stdc++.h>
#define ll long long
#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    double a,b,c,d,e,max=0;
    ll int i,j,k,l,t;
    ofstream myfile;
    myfile.open ("example.txt");
    myfile.precision(8);
    cin>>t;
    l=1; 
    while(l<=t)
    {   max=0;
        cin>>a>>b;
        for(i=0;i<b;i++)
        {
            cin>>d>>e;
            c = (a-d)/e;
            if(c>max)
                max=c;
        }
        e=a/max;
        myfile<<"Case #"<<l<<": "<<e<<endl;
        l++;
    }
    return 0;
}
