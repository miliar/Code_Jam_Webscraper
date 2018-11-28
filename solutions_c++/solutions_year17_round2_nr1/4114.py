#include <bits/stdc++.h>

using namespace std;
typedef long long int ll;

int main(){
	int t;
	cin>>t;
	for(int z=1; z<=t; z++){
		int n, d;
		cin>>d>>n;
		vector<pair<int,int> > ks(n);
		for(int i=0; i<n; i++){
			cin>>ks[i].first>>ks[i].second;
		}
		sort(ks.begin(), ks.end());

		vector<int> pos;
		int l=0, r=n;
		while(r>0){
			int p=0, s=100000;
			for(int j=0; j<r; j++){
				if(ks[j].second<s){
					p=j;
				}
			}
			pos.push_back(p);
			r=p;
		}

		l=0;
		while(true){
			bool f=true;
			for(int i=l; i<pos.size()-1; i++){
				int ki=ks[i].first, si=ks[i].second;
				int kj=ks[i+1].first, sj=ks[i+1].second;
				if((d-ki)*(ll)sj<(d-kj)*(ll)si){
					f=false;
					l=i+1;
					break;
				}
			}
			if(f){
				break;
			}
		}
		double ans=d;
		ans*=ks[l].second;
		d-=ks[l].first;
		ans/=d;
		printf("Case #%d: %0.7lf\n", z, ans);
	}
}