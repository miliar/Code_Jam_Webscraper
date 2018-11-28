#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define vll vector<ll>
#define pb push_back
ll t,k,l;
string str;
vll g[1025];
vll bi;
void bits(ll no)
{
	bi.clear();
	while(no)
	{
		bi.pb(no%2);
		no/=2;
	}
	for(ll i=bi.size();i<l;i++) bi.pb(0);
}
void creategraph()
{
	ll end=1<<l;
	for(ll i=0;i<end;i++)
	{
		g[i].clear();
		bits(i);
		for(ll j=0;j<=l-k;j++)
		{
			ll no=0;
			for(ll kk=0;kk<j;kk++) no+=(bi[kk])?(1<<kk):0;
			for(ll kk=j;kk<j+k;kk++) no+=(bi[kk])?0:(1<<kk);
			for(ll kk=j+k;kk<l;kk++) no+=(bi[kk])?(1<<kk):0;
			g[i].pb(no);
		} 
	}
}
ll num()
{
	ll no=0;
	for(ll i=0;i<l;i++)
	{
		no+=str[i]=='+'?(1<<(l-i-1)):0;
	}
	return no;
}
ll bfs(ll s)
{
	queue<ll> q;
	vector<bool> done(1<<l,false);
	vll dist((1<<l),INT_MAX);
	q.push(s);
	done[s]=true;
	dist[s]=0;
	while(!q.empty())
	{
		ll f=q.front();
		q.pop();
		for(ll i=0;i<g[f].size();i++) if(!done[g[f][i]])
		{
			q.push(g[f][i]);
			done[g[f][i]]=true;
			dist[g[f][i]]=dist[f]+1;
		}
	}
	return dist[(1<<l)-1];
}
int main()
{	
	freopen("A-small-attempt0.in","r",stdin);
	freopen("outputf.in","w",stdout);
	cin>>t;
	for(ll tt=1;tt<=t;tt++) 
	{
		cout<<"Case #"<<tt<<": ";
		cin>>str;
		cin>>k;
		l=str.length();
		creategraph();
		// for(ll i=0;i<(1<<l);i++)
		// {
		// 	cout<<i<<"->";
		// 	for(ll j=0;j<g[i].size();j++) cout<<g[i][j]<<" ";
		// 	cout<<endl;
		// }
		ll no=num();
		ll ans=bfs(no);
		if(ans==INT_MAX) cout<<"IMPOSSIBLE\n";
		else cout<<ans<<"\n";
	}
}