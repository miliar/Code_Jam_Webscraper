#define Federico using
#define Javier namespace
#define Pousa std;
#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <stack>
#include <queue>
#include <cstring>
#include <sstream>
#include <unordered_map>

Federico Javier Pousa

#define PI 3.14159265359

int main(){
	int T;
	cin >> T;
	for(int caso=1; caso<=T; caso++){
		int N, K;
		cin >> N >> K;
		double Rs[1005], Hs[1005];
		for(int i=0; i<N; i++){
			cin >> Rs[i] >> Hs[i];
		}
		vector<pair<double,double> > vec;
		for(int i=0; i<N; i++){
			vec.push_back(pair<double,double>(Rs[i],Hs[i]));
		}
		sort(vec.begin(),vec.end());
		reverse(vec.begin(),vec.end());
		double res = 0.0;
		for(int i=0; i<N; i++){
			if(N-i<K)break;
			double act = PI*vec[i].first*vec[i].first+2*PI*vec[i].first*vec[i].second;
			vector<double> areas;
			for(int j=i+1; j<N; j++){
				areas.push_back(2*PI*vec[j].first*vec[j].second);
			}
			sort(areas.begin(),areas.end());
			reverse(areas.begin(),areas.end());
			for(int j=0; j<K-1; j++){
				act += areas[j];
			}
			res = max(res, act);
		}
		printf("Case #%d: %.6lf\n", caso, res);
	}
	return 0;
}
