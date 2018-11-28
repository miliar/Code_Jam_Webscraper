#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define ite iterator
#define mp make_pair
#define ff first
#define ss second
#define pb push_back
#define null NULL
#define ioS ios::sync_with_stdio(false);
#define mod 1000000007
#define Max 9000000000000000000
#define Min (-1)*9000000000000000000


int main()
{
ioS;
ll i,j,k,l,r,m,n,o,t;

cin>>t;
char str[1001];
for(o=1;o<=t;o++)
{
cin>>str;
cin>>n;
l=strlen(str);
ll ans=0;
bool flag=1;
for(i=0;i<l;i++)
{
    if(str[i]=='-')
    {
        if(i+n<=l)
        {
            ans++;
            for(j=i;j<=i+n-1;j++)
            {
                if(str[j]=='-')
                    str[j]='+';
                else
                    str[j]='-';
            }
        }
        else
        {
            flag=0;
            break;
        }
    }
}


cout<<"Case #"<<o<<": ";
if(flag)
    cout<<ans<<endl;
else
    cout<<"IMPOSSIBLE"<<endl;
}
}
