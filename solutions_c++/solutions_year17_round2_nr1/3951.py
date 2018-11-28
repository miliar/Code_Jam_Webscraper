#include <bits/stdc++.h>
#define  mp make_pair
#define pb push_back
#define pf push_front
#define pp pop_back
#define ppf pop_front
#define fi first
#define se second
#define maxn 1000005
 
typedef long long ll;
using namespace std;
#define pi pair<int,int>
 
 
/*struct node
{
	int i;
 
	bool friend operator < (node a,node b)
	{
		return w[a.i]>w[b.i];
	}
};
priority_queue<node>pq;*/


int main()
{
	//ios_base::sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL);
 	int q;
 	cin>>q;
 	int t1 = 0;
 	while(q--)
 	{
 		t1++;
 		
 		ll d,n;
 		cin>>d>>n;
 		vector<pair<ll,ll> > v;
 		ll a[n],v1[n];
 		for(int i=0;i<n;i++)
 		{
 			cin>>a[i]>>v1[i];
 			v.pb(mp(a[i],v1[i]));
		 }
		sort(v.begin(),v.end());
		int sz = n;
		ll last = d;
		double t,lt = ((d-v[n-1].fi)*1.0)/v[n-1].se;
		int idx = n-1;
		for(int i=n-2;i>=0;i--)
		{
			t = ((d-v[i].fi)*1.0)/v[i].se;
			if(t>lt) lt = t,idx =i;
			 
		}
		///cout<<lt<<endl;
		t = ((d-v[idx].fi)*1.0)/v[idx].se;
		double res = ((d)*1.0)/lt;
		//cout<<res<<endl;
		printf("Case #%d: %0.6lf\n",t1,res);
	}
}