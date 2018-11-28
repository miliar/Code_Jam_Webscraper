#include <bits/stdc++.h>

using namespace std;
typedef long long int ll;
double pi=acos(-1);

double sol(vector<pair<ll,ll> > &rh, int id, int k, int n){
	vector<ll> rhp;
	for(int i=0; i<id; i++){
		rhp.push_back(rh[i].first*rh[i].second);
	}
	
	sort(rhp.begin(), rhp.end());
	double ans=0;
	int i=rhp.size()-1;
	while(k--){
		ans+=rhp[i];
		i--;
	}
	
	return ans;
}

int main(){
	int t;
	cin>>t;
	for(int z=1; z<=t; z++){
		int n, k;
		cin>>n>>k;
		vector<pair<ll, ll> > rh(n);
		for(int i=0; i<n; i++) cin>>rh[i].first>>rh[i].second;
		sort(rh.begin(), rh.end());
		double ans=0;
		for(int i=0; i<n; i++){
			if(i-(k-1)>=0){
				double tmp=pi*rh[i].first*rh[i].first+2*pi*rh[i].first*rh[i].second;
				tmp+=sol(rh,i,k-1,n)*2*pi;
				ans=max(ans,tmp);
			}
		}
		printf("Case #%d: %0.7lf\n",z,ans);
	}
}