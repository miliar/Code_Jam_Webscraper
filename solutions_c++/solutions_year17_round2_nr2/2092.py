#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <string>
#include <fstream>

#define IN_FILE "B-small-attempt3.in"
#define OUT_FILE "out.txt"

using namespace std;

typedef long long ll;
typedef long double ld;

int main() {
	ios::sync_with_stdio(0);
	ifstream xin(IN_FILE);
	ofstream xout(OUT_FILE);
	cin.rdbuf(xin.rdbuf());
	cout.rdbuf(xout.rdbuf());
	int t;
	int tc = 1;
	cin >> t;
	while (t--) {
		string str;
		pair <ll,char> u[3];
		ll n, tmp;
		cin >> n >> u[0].first >> tmp >> u[1].first >> tmp >> u[2].first >> tmp;
		u[0].second = 'R';
		u[1].second = 'Y';
		u[2].second = 'B';
		sort(u, u + 3);
		bool failed = false;
		ll ivals = u[2].first;
		if (ivals > (n / 2))
			failed = true;
		else {
				ll rem = ivals - u[1].first;
				ll rem0 = u[0].first - rem;
				ll gival = rem0;
				u[1].first -= gival;
				u[0].first -= gival;
				if (u[1].first < 0)
					system("pause");
				if (u[0].first < 0)
					system("pause");
				for (int i = 0; i < gival; i++) {
					str.push_back(u[2].second);
					str.push_back(u[1].second);
					str.push_back(u[0].second);
				}
				for (int i = 0; i < u[1].first; i++) {
					str.push_back(u[2].second);
					str.push_back(u[1].second);
				}
				for (int i = 0; i < u[0].first; i++) {
					str.push_back(u[2].second);
					str.push_back(u[0].second);
				}
		}
		if (!failed)
			cout << "Case #" << tc << ": " << str << "\n";
		else
			cout << "Case #" << tc << ": IMPOSSIBLE\n";
		tc++;
	}
	//system("pause");
	return 0;
}
