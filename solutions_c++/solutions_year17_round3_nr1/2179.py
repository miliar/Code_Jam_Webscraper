//============================================================================
// Name        : jam17cpp.cpp
// Author      : Javier Sardinas
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <time.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <numeric>
#include <bits/stdc++.h>

using namespace std;

const long double pi = 3.1415926535897932384626433832795;

void p2017_1c_a_small() {
	int t, n, k;
	pair<int, int> rh[1010];
	cin >> t;
	for (int cas = 1; cas <= t; cas++) {
		cout << "Case #" << cas << ": ";
		cin >> n >> k;
		for (int i = 0; i < n; ++i)
			cin >>rh[i].first >> rh[i].second;
		sort(rh, rh+n);
		long long best = 0.0;
		long long current;
		vector<long long> v;
		for(int i = k-1; i < n; ++i){
			current = 1LL*rh[i].first*rh[i].first + 2LL*rh[i].first * rh[i].second;
			for (int j = 0; j < i; ++j)
				v.push_back(rh[j].first * rh[j].second);
			sort(v.begin(), v.end());
			for(int j = i-1; j > i-k; --j)
				current += 2LL*v[j];
			if (current > best)
				best = current;
			v.clear();
		}
		cout<< setiosflags(ios::fixed) <<std::setprecision(8)<<1.0*best*pi<<"\n";
	}
}

void brute(){
	int t, n, k;
		pair<int, int> rh[1010];
		cin >> t;
		for (int cas = 1; cas <= t; cas++) {
			cout << "Case #" << cas << ": ";
			cin >> n >> k;
			for (int i = 0; i < n; ++i)
				cin >>rh[i].first >> rh[i].second;
			int p[10] = {0,1,2,3,4,5,6,7,8,9};
			long long current, best = 0;
			do{
				int bestr = 0;
				current = 0;
				for(int i = 0; i < k; ++i){
					current += 2LL*rh[p[i]].first*rh[p[i]].second;
					if(rh[p[i]].first > bestr)
						bestr = rh[p[i]].first;
				}
				current += 1LL*bestr*bestr;
				if (current > best)
					best = current;
			}while(next_permutation(p,p+n));

			cout<< setiosflags(ios::fixed) <<std::setprecision(8)<<1.0*best*pi<<"\n";
		}
}

void p2017_1c_b_small() {
	int t;
	cin >> t;
	for (int cas = 1; cas <= t; cas++) {
		cout << "Case #" << cas << ": ";

	}
}

void p2017_1c_c_small() {
	int t;
	cin >> t;
	for (int cas = 1; cas <= t; cas++) {
		cout << "Case #" << cas << ": ";

	}
}

int main() {

	//p2017_1c_a_small();
	brute();

	return 0;
}
