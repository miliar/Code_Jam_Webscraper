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
For(i,t)
{
int c=0,ans=0;
string s;
cin>>s;
int m;
cin>>m;
For(g,s.length()-m+1)
{
if(s[g]=='-')
{
ans++;
for(int j=g;j<g+m;j++)
{
if(s[j]=='+')
s[j]='-';
else
s[j]='+';
}
}
}
For(h,s.length())
{
if(s[h]=='+')
c++;
}
if(c==s.length())
cout<<"Case #"<<i+1<<":"<<" "<<ans<<"\n";
else
cout<<"Case #"<<i+1<<":"<<" "<<"IMPOSSIBLE"<<"\n";
}
}
