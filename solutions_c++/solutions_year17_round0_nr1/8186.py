#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<utility>
#include<queue>
#include<numeric>
#define llu long long
#define N 100000
#define m(a,b) (a>b? b : a)
#define M(a,b) (a>b? a : b)
#define mod 1000000007
using namespace std;

char flip(char a)
{
    if(a=='+')
        return '-';
    else
        return '+';
}

int main()
{
    llu i,j,k,l,t,e,m,n;
    scanf("%lld",&t);
    for(i=1;i<=t;i++)
    {
        string s;
        set<llu> se;
        cin>>s>>k;
        n=s.length();
        llu flips=n-k+1;
        for(j=0;j<(n-k+1);j++)
        {
            //cout<<j<<" ";
            if(s[j]=='-')
            {
                se.insert(j);
                for(l=j;l<j+k;l++)
                    s[l]=flip(s[l]);
            }
            m=count(s.begin(),s.end(),'+');
            if(m==n || se.size()==flips)
                break;
        }
        //cout<<s<<endl;
        m=count(s.begin(),s.end(),'+');
        if(m==n)
            cout<<"Case #"<<i<<": "<<se.size()<<endl;
        else
            cout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
    }
    return 0;
}


