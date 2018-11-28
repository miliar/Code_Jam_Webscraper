/*
Copyright @ Rishabh Sharma
Email-rishabh435@gmail.com
NIT Warangal
*/
#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<cmath>
#include<string.h>
#include<stdlib.h>
#include<vector>
#include<stack>
#include<queue>
#include<map>
#include<time.h>
#define lli long long int
#define li long int
using namespace std;
template<typename X>
X maxi(X a, X b)
{
    return (a>b)?a:b;
}

template<typename X>
X mini(X a, X b)
{
    return (a>b)?b:a;
}
lli isno(lli n)
{
    int flag=1;
    int ll1=n%10;
    n=n/10;
    while(n>0)
    {
    //cout<<"j";
        int ll2=n%10;
        if(ll2>ll1)
            return 0;
        else
        {
            ll1=ll2;

        }
        n=n/10;
    }
    return 1;
}

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    lli t;
    cin>>t;
    int casee=1;
    while(t--)
    {
        lli n;
        cin>>n;
        //cout<<solve(n);
        for(lli i=n; ;i--)
        {
            if(isno(i)==1)
            {
                cout<<"Case #"<<casee<<": "<<i;
                break;
            }
        }
        casee++;
        cout<<"\n";
    }
    return 0;
}
