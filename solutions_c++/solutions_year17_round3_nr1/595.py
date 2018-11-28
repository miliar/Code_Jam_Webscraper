#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#define _USE_MATH_DEFINES
#include <math.h>
#include <string>
#include <iomanip>
using namespace std;

bool compH(pair<long,long>p1, pair<long,long> p2){
	return (p1.second * p1.first < p2.second * p2.first);
}
bool compR(pair<long,long>p1, pair<long,long> p2){
	return (p1.first > p2.first || p1.first == p2.first && p1.second>p2.second);
}

double ffun(pair<long,long> p){
	return  M_PI * p.first * p.first + M_PI * p.first * 2 * p.second;
}

double fun(pair<long,long> p){
	return  M_PI * p.first * 2 * p.second;
}

int main(){
	freopen("D:\\temp\\al15.in", "r", stdin);
	freopen("D:\\temp\\outl15.txt", "w", stdout);
	int o1;
	cin>>o1;
	for (int t = 1; t <= o1; ++t){
		int n, k;
		cin>>n>>k;
		vector<pair<long,long>> cakes(n);		
		for(int i = 0; i < n; ++i){
			cin>>cakes[i].first>>cakes[i].second;
		}
		sort(cakes.begin(), cakes.end(), compR);
		vector<vector<double>> dyn(k, vector<double>(n, -1));
		dyn[0][0] = ffun(cakes[0]);
		for (int i = 1; i < n; ++i)
			dyn[0][i] = max(dyn[0][i - 1], ffun(cakes[i]));
		for (int j = 1; j < k; ++j)
		{			
			for (int i = 1; i < n; ++i){
				if (dyn[j - 1][i - 1] < 0) continue;
				if (dyn[j][i - 1] < 0) {
					dyn[j][i] =dyn[j - 1][i - 1] + fun(cakes[i]);
					continue;
				}
				dyn[j][i] = max(dyn[j - 1][i - 1] + fun(cakes[i]), dyn[j][i - 1]);
			}
		}
		cout<<"Case #"<<t<<": "<<fixed<<setprecision(8)<<dyn[k - 1][n - 1]<<endl;
	}
}