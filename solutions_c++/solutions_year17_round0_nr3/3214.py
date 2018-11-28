#include<bits/stdc++.h>
#include<vector>
#include<set>
#include<stack>
#include<queue>
#include<list>
#include<map>
#define ll long long
#define INF 2000000000
#define NINF -2000000000
#define MOD 1000000007
#define br '\n'
using namespace std;
struct classcomp {
  bool operator() (const ll& lhs, const ll& rhs) const
  {return lhs>rhs;}
};
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	freopen("C-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin>>t;
	for(int tc=1;tc<=t;tc++)
	{
		ll n,k;
		cin>>n>>k;
		map<ll,ll,classcomp> m;
		map<ll,ll,classcomp>::iterator it;
		m.insert(make_pair(n,1));
		ll val,count,ans,newval1,newval2;
		while(k>0)
		{
			it=m.begin();
			val=it->first;
			count=it->second;
			ans=val;
			val--;
			newval1=val-(val/2);
			newval2=val/2;
			if(m.find(newval1)!=m.end())
			{
				m[newval1]+=count;
			}
			else
			{
				m[newval1]=count;
			}
			if(m.find(newval2)!=m.end())
			{
				m[newval2]+=count;
			}
			else
			{
				m[newval2]=count;
			}
			k-=count;
			m.erase(m.begin());
		}
		ans--;
		ll ans_max=ans-(ans/2);
		ll ans_min=ans/2;
		cout<<"Case #"<<tc<<": "<<ans_max<<" "<<ans_min<<br;
	}
	return 0;
}

