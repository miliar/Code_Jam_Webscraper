#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define present(container, element) (container.find(element) != container.end())
#define cpresent(container, element) (find(all(container),element) != container.end())
#define all(c) c.begin(), c.end()
typedef long long ll;
using namespace std;
int level[100005];
bool visited[100005];
int dis[1005][1005];
int main()
{
	int q;
 	cin>>q;
 	for(int q0=1;q0<=q;q0++)
 	{
 		ll d,n;
 		cin>>d>>n;
 		vector<pair<ll,ll> > v;
 		ll a[n],b[n];
 		for(int i=0;i<n;i++)
 		{
 			cin>>a[i]>>b[i];
 			v.pb(mp(a[i],b[i]));
		 }
		sort(v.begin(),v.end());
		double x,T = ((d-v[n-1].f)*1.0)/v[n-1].s;
		int ind = n-1;
		for(int i=n-2;i>=0;i--)
		{
			x = ((d-v[i].f)*1.0)/v[i].s;
			if(x>T)
                T = x,ind =i;

		}
		x = ((d-v[ind].f)*1.0)/v[ind].s;
		double H = ((d)*1.0)/T;
		printf("Case #%d: %0.6lf\n",q0,H);
	}
}
