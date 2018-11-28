#include <bits/stdc++.h>
#define pi acos(-1)
using namespace std;

bool cmp(pair<long long,long long> p1, pair<long long, long long> p2){
	if(p1.first*p1.second!=p2.first*p2.second)
		return p1.first*p1.second>p2.first*p2.second;	
	return p1.first > p2.first;
}




void solver(int NC){
		
	int n, k;
	cin>>n>>k;
	int r,h;
	vector<pair<long long,long long> > save; 
	for(int i = 0 ; i< n ; i ++){
		cin>>r>>h;
		save.push_back(make_pair(r,h));
			
	}	
	double ansans = 0 ;
	for(int i = 0 ; i< n ; i++){
		vector<pair<long long, long long> > save1;
		for(int j = 0 ; j<n ; j++) if(i!=j){
			if(save[i].first>=save[j].first){
				save1.push_back(save[j]);	
			}	
		}	
		if(save1.size()<k-1)	continue;
		sort(save1.begin(), save1.end(), cmp);
		double ans = pi*(double)save[i].first*(double)save[i].first ;
		long long temp = save[i].first*save[i].second;
		for(int j = 0; j<k-1;j++ ){
			temp += save1[j].first*save1[j].second;	
		}
		
		ans += (double)temp *2.0 * pi;

		ansans = max(ansans, ans);


	}
	
	printf("Case #%d: %.9f\n", NC, ansans);
}

int main(){

	int TC;
	int NC = 1;


	cin>>TC;
	while(TC-- ){
		solver(NC);
		NC++;	
	}

	return 0;	
}
