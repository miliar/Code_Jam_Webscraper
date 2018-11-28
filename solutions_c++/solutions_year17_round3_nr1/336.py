#include"stdafx.h"
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<assert.h>
#include<ctime>
#include<queue>
#include<fstream>
#include<string>
using namespace std;

const double pi =acos(-1);
const int maxn = 1010;

long long r[maxn];
long long h[maxn];

pair<long long, long long> cp[maxn];
pair<long long,long long> rh[maxn];

bool cmp(pair<long long, long long> a, pair<long long, long long> b){
	if (a.first*a.second == b.first*b.second) return a.first > b.first;
	return a.first*a.second > b.first*b.second;
}

bool cmp1(pair<long long, long long> a, pair<long long, long long> b){
	if (a.first == b.first) return a.second < b.second;
	return a.first< b.first;
}

int main(){
	ios_base::sync_with_stdio(false);
	int t;
	ifstream fin;
	fin.open("A-large.in");
	fin >> t;
	ofstream fout;
	fout.open("1-large.out");
	fout.precision(20);
	fout.setf(ios::fixed);

	for (int ti = 1; ti <= t; ti++){
		fout << "Case #" << ti << ": ";

		int n, k;
		fin >> n >> k;
		//cout << n << " case "<<ti<<" "<< k << endl;
		for (int i = 0; i < n; i++){
			fin >> r[i] >> h[i];
			cp[i] = make_pair(r[i], h[i]);
		}
		sort(r, r + n);
		sort(cp, cp + n, cmp1);
		long long ans = 0;
		for (int i = 0; i < n;i++){
			int cnt = 0;
			for (int j = 0; j < n; j++){
				if (i == j) continue;
				if (cp[j].first <= cp[i].first)
				{
					rh[cnt] = cp[j];
					cnt++;
				}
			}
			if (cnt < k - 1) continue;
			sort(rh, rh + cnt, cmp);
			long long temp = 2*cp[i].first*cp[i].second;
			for (int j = 0; j < k-1; j++){
				temp += 2 * rh[j].first*rh[j].second;
			}
			ans = max(ans, temp + cp[i].first*cp[i].first);
		}
		/*
		for (int i = n - 1; i >= k; i--){
			long long val = r[i];
			long long temp =0;
			int cnt = 0;
			long long maxV = 0;
			for (int j = 0; j < n; j++){
				if (cp[j].first <= val){
					cnt++;
					temp += 2 * cp[j].first*cp[j].second;
					maxV = max(maxV, cp[j].first);
				}
				if (cnt == k) break;
			}
			if (cnt == k){
				//cout << val << " " << temp << endl;
				ans = max(ans, maxV*maxV+temp);
			}
		}*/
		fout << pi*ans << endl;
	}
	system("Pause");
	return 0;
}
