#include <bits/stdc++.h>
#include <iostream>
#include <math.h>
#include <string>
#include <stack>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <cstdio>
using namespace std;
#define ll long long
#define Min(a,b) ((a<=b) ? a : b)
#define Max(a,b) ((a>=b) ? a : b)
#define pb push_back
#define MP make_pair
typedef pair < int , int >  pii;
#define vi vector<int>
#define pii pair< int,int >
#define vll vector<ll>
#define MAX 10010999// sqrt of MAX
#define MOD 1000000007
#define LMT 10000 // sqrt of MAX
#define LEN 5761465 // MAX primes that can be within range
#define RNG 100032 //
#define sq( x ) ( x * x )
#define chkC(x,n) ( x[n>>6] &  ( 1<<(( n>>1 ) &31)))
#define setC(x,n) ( x[n>>6] |= ( 1<<(( n>>1 ) &31)))
#define ff first
#define ss second
#define MAXNODE 10100
#define MAXLEN 100
#define vc vector<char>
#define sc(n) scanf("%lld",&n)

string s;

int main()
{
    //ios_base::sync_with_stdio(false);
    //cin.tie(NULL);
    //FILE*f=freopen("input.txt","r",stdin);
    //FILE*o=freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int tc=1;tc<=t;tc++)
    {
        cin>>s;
        int len=s.size();
        cout<< "Case #"<<tc<< ": ";
        if(len==1)cout<<s<<endl;
        else
        {
            for(int i=len-1;i>=1;i--)
            {
                if(s[i]==s[i-1] && s[i]!='0')continue;
                if(s[i]<=s[i-1])
                {
                    s[i]='9';
                    if(s[i-1]=='0')s[i-2]--,s[i-1]='9';
                    else s[i-1]--;
                }
            }
            int p=0;
            for(int i=0;i<len;i++)
            {
                if(s[i]=='0' && p==0)continue;
                else
                {
                    if(s[i]<s[i-1])s[i]=s[i-1];
                    cout<<s[i];
                    p=1;
                }
            }
            cout<<endl;
        }
    }

    //fclose(f);
    //fclose(o);

    return 0;
}
