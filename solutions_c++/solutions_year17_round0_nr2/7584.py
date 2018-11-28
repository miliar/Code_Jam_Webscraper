# include <bits/stdc++.h>
# define For(i,n) for(ll  i=0;i<n;++i)
# define Foro(i,n) for(int i=n-1;i>0;i--)
#define cin(c) scanf("%lld",&c)
# define cout(c) printf("%lld\n",c)
# define ve vector<long long> v
# define se set<long long>s
# define pb push_back
# define ll long long
# define mod 1000000007
# define inf 10001
# define mp make_pair
using namespace std;
//ll ar[1000000],br[1000000];
int main()
{
int t;
cin>>t;
For(g,t)
{
int flag=0;
ll n,pos=-1,m;
cin>>n;
m=n;
ve;
while(n)
{
ll d=n%10;
v.pb(d);
n=n/10;
}
reverse(v.begin(),v.end());
For(i,v.size()-1)
{
if(v[i]>v[i+1])
{
flag=1;
 pos=v[i];
break;
}

}
cout<<"Case #"<<g+1<<": ";
if(flag==0)
cout<<m<<"\n";
else
{



For(i,v.size())
{
if(v[i]==pos)
{
v[i]=v[i]-1;
 pos=i;
break;
}
}
For(i,v.size())
{
if(i>pos)
v[i]=9;
}





For(i,v.size())
{
if(v[i]!=0)
cout<<v[i];
}
cout<<"\n";
//cout<<"Case #"<<g+1<<": "<<ans<<"\n";
}
}
}
