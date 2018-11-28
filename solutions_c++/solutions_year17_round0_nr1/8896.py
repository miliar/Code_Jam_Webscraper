#include<cstdio>
#include<iostream>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include <bits/stdc++.h>

#define INF 2000000000
#define INF_LL 2000000000000000000ll
#define MOD_7 1000000007
#define MOD_9 1000000009

//typedef long long ll;

using namespace std;

string s;

void chng(int i,int j){
    int k=i;
    for(k=i;k<=j;k++){
        if(s[k]=='+')
         s[k]='-';
        else if(s[k]=='-')
         s[k]='+';
    }
}

long long int solve(int p1,int p2,int len,int k){
    long long int val=0;
    int i=p1,j=p2;
    while(i<len&&j<len){
        val++;
        //cout<<val<<"val\n";
        chng(i,j);
        while(i<len&&s[i]=='+')
         i++;
        j=i+k-1;
        //if(j>=len)
         //return -1;
    }
    if(i!=len)
     return -1;
    return val;
}

int main()
{
    //ios_base::sync_with_stdio(false);
    //cin.tie(NULL);
    //cout.tie(NULL);
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    int t,sv,p1,p2,k,l;
    long long int ans;
    cin>>t;
    sv=t;
    //string s;
    while(t--)
    {
        cin>>s;
        cin>>k;
        ans=0;
        l=s.length();
        p1=0;
        while(p1<l&&s[p1]=='+')
         p1++;
        p2=p1+k-1;
        //cout<<p1<<"P1"<<p2<<"\n";
        if(p1==l)
         ans=0;
        else
         ans=solve(p1,p2,l,k);
        if(ans==-1)
         printf("Case #%d: IMPOSSIBLE\n",sv-t);
        else
        printf("Case #%d: %lld\n",sv-t,ans);
    }

    return 0;
}
