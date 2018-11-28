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
int main()
{
    //freopen("data2.in","r",stdin);
    //freopen("out2.txt","w",stdout);
    int t,l1=0;
    cin>>t;
    while(t--)
    {
        l1++;
        ll n,n2;
        cin>>n;
        n2=n;
        int i,j,k,l;
        string str="";
        while(n2)
        {
            str=str+char(n2%10+'0');
            n2/=10;
        }
        reverse(str.begin(),str.end());
        bool f=0;
        l=str.length();
        while(!f)
        {
            int prev=str[0]-'0';
            for(i=1;i<l;i++)
            {
                int cur=str[i]-'0';
                if(cur<prev)
                {
                    str[i-1]--;
                    break;
                }
                prev=cur;
            }
            if(i==l)
                f=1;
            for(;i<l;i++)
            {
                str[i]='9';
            }
        }
        for(i=0;i<l;i++)
        {
            n2=n2*10+(str[i]-'0');
        }
        cout<<"Case #"<<l1<<": "<<n2<<"\n";
    }
    return 0;
}
