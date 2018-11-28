#include<bits/stdc++.h>
using namespace std;
int main()
{
freopen("A-large.in","r",stdin);
freopen("pa.txt","w",stdout);
ios_base::sync_with_stdio(false);
long long t,n,ans=0,i,k,l,z,f,cc=0;
char s[10000];
cin>>t;
while(t--)
{
++cc;
z=1;
ans=0;
f=1;
cin>>s>>k;
l=strlen(s);
for(i=0;i<=l-k;i++)
{
z=1;
if(s[i]=='-')
{
ans++;
s[i]='+';
while(z<k)
{

if(s[i+z]=='-')
s[i+z]='+';
else
s[i+z]='-';
z++;
}
}
//cout<<s<<endl;
}
for(i=0;i<l;i++)
{
    if(s[i]=='-')
    {

        f=0;
        break;

    }

}
if(f==0)
    cout<<"Case #"<<cc<<": "<<"IMPOSSIBLE"<<endl;
else
    cout<<"Case #"<<cc<<": "<<ans<<endl;

}
return 0;

}
