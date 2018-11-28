#include <iostream>
#include <string>
#include <utility>
#include <vector>
#include <iomanip>
using namespace std;
typedef unsigned long long ull;

const double PI  =3.141592653589793238463;


bool myComparison(const pair<ull,ull> &a,const pair<ull,ull> &b)
{
	return a.first*a.second>b.first*b.second;
}

int main() {
	ull t;
	cin >> t;
	//std::cout << std::fixed;
	std::cout << std::setprecision(8);
	for (ull i = 1; i<=t; ++i) {
		ull n, k;
		cin >> n >> k;
		vector<pair<ull,ull>> v;
		for (ull j = 0; j < n; ++j) {
			ull r, h;
			cin >> r >> h;
			v.push_back(make_pair(r,h));
			//ha[j] = 2*r[j]*PI*h[j];			
		}
		sort(v.begin(),v.end(),myComparison);
		double ans = 0;
		ull bigR = 0;
		for (ull j = 0; j < k-1; ++j) {
			ans += 2*v[j].first*PI*v[j].second;
			if (v[j].first>bigR) bigR = v[j].first;
		}
		double testAns = ans;
		for (ull j = k-1; j < n; ++j) {
			double test = ans + 2*v[j].first*PI*v[j].second;
			ull testR;
			if (v[j].first > bigR) testR = v[j].first;
			else testR = bigR;
			test += testR*testR*PI;
			//cout << v[j].first << " " << test << endl;;
			if (test>testAns) testAns = test;
		}
		
		cout << "Case #" << i << ": " << testAns << endl;
	}
	

	return 0;
}