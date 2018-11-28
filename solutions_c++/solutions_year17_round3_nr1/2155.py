#include<bits/stdc++.h>
using namespace std;
#define MOD 1000000007
#define INF INT_MAX/2
#define PI 3.14159265358979323846264338327950
#define reset(a,x) memset(a,x,sizeof(a))

#define ll long long
#define ull unsigned long long
#define ii pair<int,int>
#define vi vector<int> 
#define vii vector<ii>
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define all(c) (c).begin,(c).end()
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
#define rep(a,b,c)   for(int (a)=(b); (a)<(c); (a)++)
#define repn(a,b,c)  for(int (a)=(b); (a)<=(c); (a)++)
#define repd(a,b,c)  for(int (a)=(b); (a)>=(c); (a)--)

int moves[8][2]={{-1,0},{1,0},{0,1},{0,-1},{1,1},{-1,-1},{-1,1},{1,-1}};
bool issafe(int i,int j){
    return (i>=0 && i<8 && j>=0 && j<8);
}

int main(){
	int t,n,k;
	cin>>t;
	long long r,h;
	repn(test,1,t){
		cin>>n>>k;
		vector<pair<long long,long long> > area;
		for(int i=0;i<n;i++){
			cin>>r>>h;
			area.push_back(make_pair(r*h,r));
		}

		sort(area.begin(),area.end(),greater<pair<long long,long long> >());
		long double ans=0;
		pair<long long,long long> maxr=make_pair(0,0);
		pair<long long,long long> minr=make_pair(LLONG_MAX/2,INF);
		for(int i=0;i<k;i++){
			if(maxr.second<area[i].second)
				maxr=area[i];
			if(minr.first>area[i].first)
				minr=area[i];
			ans+=2*area[i].first;
		}
		bool flag=false;
		for(int i=k;i<n;i++){
			if(maxr.second<area[i].second){
				if(area[i].second*area[i].second+2*area[i].first>maxr.second*maxr.second+2*maxr.first){
					flag=true;
					maxr=area[i];
				}
			}
		}
		if(flag){
			ans+=2*maxr.first-2*minr.first;
		}
		ans+=maxr.second*maxr.second;
		ans=ans*PI;
		printf("Case #%d: ",test);
		cout<<fixed<<setprecision(10);
		cout<<ans<<endl;
	}

	return 0;
}

