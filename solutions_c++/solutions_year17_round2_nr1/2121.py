#include<bits/stdc++.h>
using namespace std;

#define fast ios_base::sync_with_stdio(0);cin.tie(0);
#define ff first
#define ss second
#define ll long long
#define ull unsigned long long
#define mp make_pair
#define pb push_back
#define PI 3.14159265
#define all(x) (x).begin(), (x).end()
#define fileinput(name) freopen((name),"r",stdin);
#define filewrite(name) freopen((name),"w",stdout);

bool cmp(const pair<int,int> &p1,const pair<int,int> &p2){
	return  p1.ss < p2.ss;
}
int main(){
	fileinput("A-large.in");
	filewrite("output.txt");
	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++){
		ll d,n;
		cin>>d>>n;
		vector < pair < ll,ll> > pos;
		ll a,b;
		for(int i=0;i<n;i++){
			cin>>a>>b;
			pos.pb(mp(a,b));
		}
		long double time=0;
		long double ttime=0;
		time = (long double)(d-pos[0].first)/(long double)pos[0].second;
		for(int i=1;i<n;i++){
			if(d - pos[i].first > 0){
				ttime=  (long double)(d - pos[i].first) /  (long double)(pos[i].second);
				if(ttime>time)
					time=ttime;
			}
			
		}
		long double ans=d/time;
		
		cout<<"Case #"<<tt<<": "<<fixed<<setprecision(6)<<ans<<endl; 
	}
	
	return 0;
}
