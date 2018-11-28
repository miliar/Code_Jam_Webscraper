#include<bits/stdc++.h>
#define pb push_back
#define F first
#define S second
#define mp make_pair
#define lli long long int
#define INF 1000000000000
#define MOD 1000000007
#define FOR(name,initial,final) for(lli name=initial;name<final;name++)
#define rz resize
#define all(x) (x).begin(),(x).end()
#define T int t; cin>>t; while(t--)
using namespace std;
typedef vector<lli> vli;
typedef pair<lli,lli> pi;
typedef pair<pair<lli,lli>,lli> ppi;
typedef vector<vector<lli> > vv;
int main()
{
	ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
	int t;
	cin>>t;
	for(int test=1;test<=t;test++)
	{
		lli n,k;
		cin>>n>>k;
		map<lli, lli> maps;
		maps[n]=1;
		map<lli, lli>::reverse_iterator iter;
		lli x=0;
		for(iter = maps.rbegin();iter!=maps.rend();++iter)
		{
			//cout<<iter->F<<' '<<iter->S<<endl;
			x = iter->F;
			lli y = iter->S;
			maps[x/2]+=y;
			maps[(x-1)/2]+=y;
			k-=y;
			if(k<=0)
				break;
		}
		lli a1 = x/2;
		lli a2 = (x-1)/2;
		cout<<"Case #"<<test<<": "<<a1<<' '<<a2<<endl;
	}
}