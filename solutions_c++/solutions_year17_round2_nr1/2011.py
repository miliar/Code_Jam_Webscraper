#include<bits/stdc++.h>

# define ini(c) int c; scanf("%d",&(c))
# define outi(c) printf("%d \n",(c)) 
# define rf freopen("input.txt","r",stdin)
# define wf freopen("output.txt","w",stdout)
# define pb(c) push_back(c)
# define mp(c,d) make_pair(c,d)
# define all(c) (c).begin(),(c).end()
# define tr(c,i) for(typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
# define test(c) ini(c);while(c--)

using namespace std;

typedef vector< int > vi;
typedef vector< vi > vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;
typedef long long ll;

int main()
{
	rf;
	wf;
	int tt;
	cin>>tt;
	int k,s;
	for(int ct=1;ct<=tt;ct++)
	{
		int d,n;
		cin>>d>>n;
		vii dist;
		int mi=n;
		while(mi--)
		{
			cin>>k>>s;
			dist.pb(mp(d-k,s));
		}
		sort(dist.begin(),dist.end());
		double x,y;
		double a,b;
		double target,time_target;
		x=(dist[n-1].first)*1.0;
		y=(dist[n-1].second)*1.0;
		//cout<<dist[n-1].first<<endl;
		for(int i=n-2;i>=0;i--){
			
			a=(dist[i].first)*1.0;
			b=(dist[i].second)*1.0;
			time_target=x/y;
			target=((a*1.0)/time_target);
			if(b>target){
				y=target;
			}
			else{
				y=b*1.0;
			}
			x=a;
			
		//	cout<<x<<" "<<y<<endl;
		}
		time_target=x/y;
		target=((d*1.0)/time_target);
		cout<<"Case #"<<ct<<": "<<fixed<<setprecision(7)<<target<<endl;
	}
	
}
