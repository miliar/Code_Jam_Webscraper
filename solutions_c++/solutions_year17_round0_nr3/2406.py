#include<bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#define ll long long int
#define nn 2001
#define inf -15000000000000ll
#define logn 21
#define ff first
#define se second
#define mod 1000000007ll
#define pdd pair<double,double>
#define db double
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define pll pair<ll,ll>
#define mt make_tuple
using namespace std;
using namespace __gnu_pbds;
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> OST;

map<ll,ll>m[70];

pll calc(ll k,ll p,ll pos)
{
	if(k<=p)
	{
		ll t=0;
		map<ll,ll>::reverse_iterator u;
		for(u=m[pos].rbegin();u!=m[pos].rend();u++)
		{
			if(t+u->se>=k)
				break;
			t+=u->se;
		}
		return mp((u->ff)/2,(u->ff-1)/2);
	}
	k-=p;
	for(auto& u:m[pos])
	{
		m[pos+1][u.ff/2]+=u.se;
		m[pos+1][(u.ff-1)/2]+=u.se;
	}
	return calc(k,p*2ll,pos+1);
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	ifstream fin;
	ofstream fout;
	fin.open("/home/nishant/Downloads/C-large.in");
	fout.open("/home/nishant/Downloads/soutputC4.txt");
	int t;
	fin>>t;
	for(int tt=1;tt<=t;tt++)
	{
		fout<<"Case #"<<tt<<": ";
		ll n,k;
		fin>>n>>k;
		m[0][n]=1;
		pll res=calc(k,1,0);
		fout<<max(0ll,res.ff)<<' '<<max(0ll,res.se)<<endl;
		for(int i=0;i<65;i++)
			m[i].clear();
	}
	return 0;
}