#include<stdio.h>
#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
#include<map>
#define ll long long
#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define tr(v,it) for(typeof(v.begin()) it=v.begin();it!=v.end();it++)
using namespace std;
int a[1002];
int main()
{
    freopen("data4.in","r",stdin);
    //freopen("out4.txt","w",stdout);
    int t;
    cin>>t;
    string str;
    int l1=0;
    while(t--)
    {
        l1++;
        cin>>str;
        int k,i,j,l,m,n;
        cin>>k;
        l=str.length();
        for(i=0;i<l;i++)
        {
            if(str[i]=='+')
                a[i]=1;
            else a[i]=0;
        }
        int ans=0;
        for(i=0;i<l-k+1;i++)
        {
            if(a[i])
                continue;
            ans++;
            for(j=0;j<k;j++)
            {
                a[i+j]=a[i+j]^1;
            }
        }
        cout<<"Case #"<<l1<<": ";
        for(i=0;i<l;i++)
        {
            if(a[i]==0)
            {
                cout<<"IMPOSSIBLE\n";
                break;
            }
        }
        if(i==l)
            cout<<ans<<"\n";
    }
    return 0;
}
