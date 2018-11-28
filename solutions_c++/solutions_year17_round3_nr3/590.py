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
	freopen("D:\\temp\\c111.in", "r", stdin);
	freopen("D:\\temp\\outc21.txt", "w", stdout);
	int o1;
	cin>>o1;
	for (int t = 1; t <= o1; ++t){
		int n, k;
		cin>>n>>k;
		double u;
		cin>>u;
		vector<double> ps(n);
		for (int i = 0; i < n; ++i)
			cin>>ps[i];
		sort(ps.begin(), ps.end());
		ps.push_back(1.0);
        for(int c = 0; c < n; ++c)
		{
            double r = min(ps[c + 1] - ps[c], u / (c + 1));
			u -= (c + 1) * r;
			for(int i = 0; i <= c; ++i)
                ps[i] += r;
		}
		double res = 1.0;
		for (int i = 0; i < n; ++i)
			res *= ps[i];

		cout<<"Case #"<<t<<": "<<setprecision(12)<<res<<endl;
	}
}