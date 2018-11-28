//Rikesh Agrawal

#include<iostream>
#include<cstdio>
#include<cmath>
#include<queue>
#include<vector>
#include<algorithm>
#include<stack>
#include<string>
#include<functional>
#include<set>
#define ll long long
#define mod 1000000007
#define INF 999999999
#define DEBUG cout<<"and_roid"<<endl
#define pb push_back
#define PI 3.141592
using namespace std;
ll a[1005];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    ios_base::sync_with_stdio(false);
    ll t,i,j,k,z,cnt,n,m,l,flag;
    cin>>t;
    string s;
    for(z=1;z<=t;z++)
    {
        cnt=0;  flag=0;
        cin>>s; cin>>k;
        for(i=0;i<s.length();i++)
        {
            if(s[i]=='+')
                a[i+1]=1;
            else
                a[i+1]=0;
        }
        n=s.length();
        for(i=1;i<=n-k+1;i++)
        {
            if(a[i]==0)
            {
                cnt++;
                for(j=i;j<i+k;j++)
                    a[j]=(a[j]+1)%2;
            }
        }
        for(i=n-k+2;i<=n;i++)
        {
            if(a[i]==0)
            {
                flag=1;
                break;
            }
        }
        if(flag==0)
            cout<<"Case #"<<z<<": "<<cnt<<endl;
        else
            cout<<"Case #"<<z<<": IMPOSSIBLE"<<endl;
    }
    return 0;
}
