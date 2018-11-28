#include <bits/stdc++.h>
using namespace std;


int main(){
	int tc, d, n, k, s;
	scanf("%d", &tc);
	int w=0;
	while(w<tc){
		//std::vector<pair<int ,int> > myMap;
		vector<double> times;
		scanf("%d%d", &d, &n);
		for (int i=0;i<n; i++){
			scanf("%d%d", &k, &s);
			times.push_back(double(d-k)/s);
		}
		sort(times.begin(), times.end());
		// cout<<endl;
		// for (int i = 0; i < myMap.size(); ++i)
		// {
		// 	cout<<myMap[i].first<<" "<<myMap[i].second<<" "<<double(d-myMap[i].second)/myMap[i].first<<endl;
		// }
		cout<<"Case #"<<w+1<<": "<<fixed<<setprecision(6)<<d/times[n-1]<<endl;
		w++;
	}
}