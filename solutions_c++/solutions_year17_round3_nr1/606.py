#include <bits/stdc++.h>
using namespace std;
const double pi=acos(-1.);
int main(){
	ios::sync_with_stdio(0);
	cout << fixed << setprecision(9);
	
	int tc=0,t,n,k,i,j;
	cin >> t;
	while(t--){
		cout << "Case #" << ++tc << ": ";
		cin >> n >> k;
		long long r,h;
		vector<pair<long long,long long>>v;
		for(i=0;i<n;++i){
			cin >> r >> h;
			v.emplace_back(r,h);
		}
		long long rm=0,hm=0; int id=0;
		for(i=0;i<n;++i){
			tie(r,h)=v[i];
			if(rm*rm+2*rm*hm<r*r+2*r*h){
				rm=r;
				hm=h;
				id=i;
			}
		}
		v.erase(v.begin()+id);
		sort(v.begin(),v.end(),[](const auto&a,const auto&b){
			if(a.first*a.second==b.first*b.second)
				return a.first>b.first;
			return a.first*a.second>b.first*b.second;
		});
		long long s=2*rm*hm,rmx=rm;
		for(i=0;i<min(k-1,int(v.size()));++i){
			tie(r,h)=v[i];
			s+=2*r*h;
			rmx=max(rmx,r);
		}
		s+=rmx*rmx;
		cout << pi*s << '\n';
	}
	return 0;
}