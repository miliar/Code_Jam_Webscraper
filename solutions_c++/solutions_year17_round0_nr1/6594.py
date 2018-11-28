#include <iostream>
#include <cstring>
#include<bits/stdc++.h>
#define ll long long int
# define mp make_pair
 const ll M = 1e9+7;
#define pb push_back 
//"Yes\n";
using namespace std;
int main()
{
    freopen ("A-large.in", "r", stdin);
    freopen ("outz.txt", "w", stdout);
    int t;
    cin>>t;
    for(int e=1;e<=t;e++){
    string a; 
    int n,i,j,x=0,k,f=0;
    cin>>a>>k;
    n=a.size();
    for(i=0;i<n-k+1;i++)
    {
        if(a[i]=='-')
        {
            for(j=i;j<i+k;j++)
            {
                if(a[j]=='+')
                a[j]='-';
                else
                a[j]='+';
            }
            x++;
        }
    }
    for(i=0;i<n;i++)
    if(a[i]=='-')
    f=1;
    cout<<"Case #"<<e<<": ";
    if(f==1)
    cout<<"IMPOSSIBLE"<<endl;
    else
    cout<<x<<endl;
    }
    return 0;
}
