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


const int maxn = 1010;
int K[maxn];
int S[maxn];
vector<double> speed[maxn];
vector<double> tim;
vector<double> dis;
const double eps = 1e-8;

bool cmp(pair<double, int> a, pair<double, int> b){
	if (abs(a.first - b.first) < eps) return S[a.second] < S[b.second];
	return a.first < b.first;
}

void prepare(int n,int d){
	vector<pair<double, int>> temp = vector<pair<double, int>>();
	tim.clear();
	dis.clear();
	for (int i = 0; i < n; i++){
		speed[i].clear();
		//speed[i].push_back(make_pair(S[i], 0));
		temp.push_back(make_pair(K[i], i));
	}
	double t = 0;
	while (1){
		sort(temp.begin(), temp.end(), cmp);
		tim.push_back(t);
		dis.push_back(temp[0].first);
		if (temp[0].first>=d) break;	
		double dt = (d-temp[0].first)/S[temp[0].second];
		for (int i = 0; i<n; i++){
			speed[temp[i].second].push_back(temp[i].second);
			if (i + 1 <n && abs(temp[i].first - temp[i +1].first) < eps) S[temp[i + 1].second] = S[temp[i].second];
			else if (i + 1 <n &&S[temp[i + 1].second] < S[temp[i].second]){
				dt = min(dt, (temp[i + 1].first - temp[i].first) / (S[temp[i].second] - S[temp[i + 1].second]));
			}
		}
		for (int i = 0; i < n; i++){
			temp[i].first += dt*S[temp[i].second];
		}
		t += dt;
	}
	//for (int i = 0; i < tim.size(); i++) cout << i << " " << tim[i] << endl;
}



int main(){
	ios_base::sync_with_stdio(false);
	int t;
	ifstream fin;
	fin.open("A-large.in");
	fin >> t;
	ofstream fout;
	fout.open("1.out");
	fout.precision(20);
	fout.setf(ios::fixed);

	for (int ti = 1; ti <= t; ti++){
		fout << "Case #" << ti << ": ";
		int d,n;
		fin >>d>> n;
		for (int i = 0; i < n; i++){
			fin >> K[i] >> S[i];

		}
		prepare(n,d);
		double ans = 1e18;
		for (int i = 1; i < tim.size(); i++){
			ans = min(ans, dis[i] / tim[i]);
		}
		fout << ans << endl;
		//cout << ti << " " << d << " " << n << " " << ans << endl;
		
	}
	system("Pause");
	return 0;
}
