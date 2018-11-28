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

string buildstring(llu num)
{
    string s="";
    for(llu i=0;i<num;i++)
        s+="9";
    return s;
}

int main()
{
    llu i,j,k,l,t,e,m,n;
    scanf("%lld",&t);
    for(j=1;j<=t;j++)
    {
        string s,rep;
        cin>>s;
        n=s.length();
        for(i=n-2;i>=0;i--)
        {
            if(s[i]>s[i+1])
            {
                s[i]=((s[i]-'0')-1)+'0';
                rep=buildstring(n-i-1);
                s.replace(i+1,n,rep);
            }
        }
        if(s[0]=='0' && n!=1)
            s.erase(0,1);
        string tc="Case #";
        tc+=to_string(j);
        tc+=": ";
        cout<<tc<<s<<endl;
    }
    return 0;
}


