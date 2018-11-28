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

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    ios_base::sync_with_stdio(false);
    ll t,i,j,k,z,cnt,n,m,l,st,flag;
    cin>>t;
    string s;
    for(z=1;z<=t;z++)
    {
        cin>>s;
        n=s.length();
        ll a[n+5];
        for(i=0;i<n;i++)
            a[i+1]=s[i]-'0';
        cnt=0;
        for(i=1;i<n;i++)
        {
            if(a[i]==a[i+1])
                cnt++;
            if(a[i]<a[i+1])
                cnt=0;

            if(a[i+1]<a[i])
            {
                a[i-cnt]=a[i-cnt]-1;
                for(j=i-cnt+1;j<=n;j++)
                    a[j]=9;
                break;
            }
        }


        cout<<"Case #"<<z<<": ";
        i=1;
        while(a[i]==0)
            i++;
        for(i;i<=n;i++)
            cout<<a[i];
        cout<<endl;
    }

    return 0;
}
