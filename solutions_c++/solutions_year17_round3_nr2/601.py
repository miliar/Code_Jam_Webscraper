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
	freopen("D:\\temp\\bl1.in", "r", stdin);
	freopen("D:\\temp\\outbl1.txt", "w", stdout);
	int o1;
	cin>>o1;
	
	for (int t = 1; t <= o1; ++t){
		vector<bool> mas1(1500, true);
		vector<bool> mas2(1500, true);
		int ac, aj;
		cin>>ac>>aj;
		vector<pair<int, int>> CC(ac), CJ(aj);
		for (int i = 0; i < ac; ++i){
			cin>>CC[i].first>>CC[i].second;
			for (int j = CC[i].first; j < CC[i].second; ++j)
				mas1[j] = false;
		}
		for (int i = 0; i < aj; ++i){
			cin>>CJ[i].first>>CJ[i].second;
			for (int j = CJ[i].first; j < CJ[i].second; ++j)
				mas2[j] = false;
		}
		int c = 0;
		int j =  0;
		int n = 24 * 60;
		vector<vector<pair<int, int> > > dyn(n, vector<pair<int, int>>(n, make_pair(20000, 2000)));
		if (mas1[0]){
			dyn[0][1].first = 0;
		}
		if (mas2[0])
			dyn[0][0].second = 1;
		for(int i = 1; i < n; ++i){
			for (int j = 0; j < n; ++j){
				if (j > 0 && mas1[i]){
					dyn[i][j].first = min(dyn[i - 1][j - 1].first, dyn[i - 1][j - 1].second + 1);
				}
				if (mas2[i]){
					dyn[i][j].second = min(dyn[i - 1][j].second, dyn[i - 1][j].first + 1);
				}
			}
		}
		long long ans1 = dyn[n - 1][n / 2].first;
		dyn.assign(n, vector<pair<int, int>>(n, make_pair(20000, 2000)));
		if (mas1[0]){
			dyn[0][1].first = 1;
		}
		if (mas2[0])
			dyn[0][0].second = 0;
		for(int i = 1; i < n; ++i){
			for (int j = 0; j < n; ++j){
				if (j >0 && mas1[i]){
					dyn[i][j].first = min(dyn[i - 1][j - 1].first, dyn[i - 1][j - 1].second + 1);
				}
				if (mas2[i]){
					dyn[i][j].second = min(dyn[i - 1][j].second, dyn[i - 1][j].first + 1);
				}
			}
		}
		ans1 = min(ans1, (long long)dyn[n - 1][n / 2].second);
		cout<<"Case #"<<t<<": "<<setprecision(12)<<ans1<<endl;
	}
}