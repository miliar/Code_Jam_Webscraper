#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>
#include<math.h>
using namespace std;


bool sortRadius(pair<long long,long long> p1, pair<long long,long long> p2){
	if( p1.first == p2.first){
		return p1.second < p2.second;
	}
	return p1.first < p2.first;
}

bool sortHeight(pair<long long,long long> p1, pair<long long,long long> p2){
	if( p1.second == p2.second ){
		return p1.first < p2.first;
	}
	return p1.second < p2.second;
}

bool sortEffectiveHArea(pair<long long,long long> p1, pair<long long,long long> p2){
	long double e1 = 2*p1.first*p1.second;
	long double e2 = 2*p2.first*p2.second;
	if( e1 == e2 ){
		return p1.second < p2.second;
	}
	return e1 < e2;
}

bool sortEffectiveArea(pair<long long,long long> p1, pair<long long,long long> p2){
	long double e1 = 2*p1.first*p1.second + pow(p1.first,2);
	long double e2 = 2*p2.first*p2.second + pow(p2.first,2);;
	if( e1 == e2 ){
		return p1.second < p2.second;
	}
	return e1 < e2;
}

long double maxArea(vector< pair<long long,long long> >pancakes, int n, int k){

	long double maxHoritalArea = 0;
	long double maxVerticalArea = 0;

	//pick the largest radius as bottom
	sort(pancakes.begin(), pancakes.end(), sortEffectiveArea);	
	vector< pair<long long,long long> > selected;
	selected.push_back(pancakes.back());
	pancakes.pop_back();

	sort(pancakes.begin(), pancakes.end(), sortEffectiveHArea);
	for(int i=0; i<k-1; i++){
		selected.push_back(pancakes.back());
		pancakes.pop_back();
	}

	sort(selected.begin(), selected.end(), sortRadius);
	pair<long long,long long> cake = selected.back();
	selected.pop_back();
	k--;
	maxHoritalArea = pow(cake.first,2);
	maxVerticalArea = 2*cake.first*cake.second;
	//cout<<"curr cake"<<cake.first<<" "<<cake.second<<endl;
	while(k>0){
		cake = selected.back();
		selected.pop_back();

		maxVerticalArea += 2*cake.first*cake.second;
		//cout<<"maxVer"<<maxVerticalArea<<endl;
		//cout<<"curr cake"<<cake.first<<" "<<cake.second<<endl;
		k--;
	}
	//cout<<"maxHAre"<<maxVerticalArea<<endl;
	return M_PI * (maxHoritalArea + maxVerticalArea);
}

int main(){
	
	int ncase;
	cin >> ncase;

	for(int i=0; i<ncase; i++){
		int n,k;
		long long r,h;
		pair<long long,long long> cake;

		cin >> n >> k;
		vector< pair<long long,long long> > pancakes;

		for(int j=0; j<n; j++){
			cin >> r >> h;
			cake.first = r;
			cake.second = h;
			pancakes.push_back(cake);
		}
	
		long double result = maxArea(pancakes, n, k);
		printf("Case #%d: %.6Lf\n", i+1, result );
	}
	return 0;
}