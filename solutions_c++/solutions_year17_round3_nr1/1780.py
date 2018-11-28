#include<cstdio>
#include<iostream>
#include<cmath>
#include<vector>
#include<string>
#include<algorithm>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<iomanip>
#include<fstream>

#define rep(i,a,N) for(int i=0+a;i<N;i++)
#define lint long long int
#define SIZE 100005
#define pb push_back
#define MP make_pair

using namespace std;

int main(){
	ofstream ofs("D:\\tomo\\Programming\\GCJ\\Round1C\\A-small.txt");
	lint t;
	cin>>t;
	double pi=3.14159265359;
	rep(i,0,t){
		lint n,k;
		double sum=0,fin=0;
		vector<pair<double,double>> rh(1000);
		cin>>n>>k;
		rep(j,0,n){
			double a,b;
			cin>>a>>b;
			rh.pb(MP(a,b));
		}
		sort(rh.begin(),rh.end(),greater<pair<double,double>>());
		rep(j,0,n){
			vector<double> h2(1000);
			h2.pb(0);
			sum=rh[j].first*rh[j].first+rh[j].first*2*rh[j].second;
			rep(l,j+1,n){
				h2.pb(rh[l].second*rh[l].first*2);
			}
			sort(h2.begin(),h2.end(),greater<double>());
			rep(l,0,k-1){
				sum+=h2[l];
			}
			if(fin<sum)fin=sum;
			sum=0;
		}
		ofs<<"Case #"<<i+1<<": "<<fixed<<setprecision(25)<<fin*pi<<endl;
	}

return 0;
}