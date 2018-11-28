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
 
double PI = 3.14159265359;
/*struct node
{
	int i;
 
	bool friend operator < (node a,node b)
	{
		return w[a.i]>w[b.i];
	}
};
priority_queue<node>pq;*/
ll a[maxn],b[maxn];
vector<pair<ll,ll> > v;
int main()
{
	ios_base::sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL);
 	int q;
 	cin>>q;
 	int t =0 ;
 	while(q--)
 	{
 		t++;
 		int n,k;
 		cin>>n>>k;
 		v.clear();
 		for(int i=0;i<n;i++){
		 
 		cin>>a[i]>>b[i];
 		v.pb(mp(a[i],b[i]));}
	 
	 sort(v.begin(),v.end());
	 double max = 0.0;
	 //cout<<"Case #"<<t<<": ";
	 for(int i=n-1;i>=k-1;i--)
	 {
	 	set<ll> s;
	 	double sum = PI*(v[i].fi*v[i].fi)+2*PI*v[i].fi*v[i].se;
	 	for(int j=i-1;j>=0;j--)
	 	{
	 		s.insert(v[j].fi*v[j].se);
		 }
		 
		set<ll>::iterator it = s.end();
		if(s.size()>0)
		it--;
		int c =0;
		for(c=0;c<k-1;c++)
		{
			sum+=2*PI*(*it);
			it--;
		}
		if(sum>max) max = sum;
	 }
	 printf("Case #%d: %0.6lf\n",t,max);}
}
