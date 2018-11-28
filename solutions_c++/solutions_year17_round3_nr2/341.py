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

struct interval{
	int start;
	int end;
	int type;
};
bool cmp(interval i1, interval i2){
	return i1.start < i2.start;
}
vector<interval> ilist;
vector<int> slist[2];
int sum[2];

int main(){
	ios_base::sync_with_stdio(false);
	int t;
	ifstream fin;
	fin.open("B-large.in");
	fin >> t;
	ofstream fout;
	fout.open("2-large.out");
	fout.precision(20);
	fout.setf(ios::fixed);

	for (int ti = 1; ti <= t; ti++){
		fout << "Case #" << ti << ": ";
		int ac, aj;
		fin >> ac >> aj;
		sum[0] = sum[1] = 0;
		ilist.clear();
		slist[0].clear();
		slist[1].clear();
		for (int i = 0; i < ac; i++){
			int s, t;
			fin >> s >> t;
			ilist.push_back(interval{ s, t, 0 });
			sum[0] += (t - s);
		}
		for (int i = 0; i < aj; i++){
			int s, t;
			fin >> s >> t;
			ilist.push_back(interval{ s, t, 1 });
			sum[1] += (t - s);
		}
		sort(ilist.begin(), ilist.end(),cmp);
		int total = 0;
		for (int i = 1; i < ac + aj; i++){
			if (ilist[i].type == ilist[i - 1].type){
				slist[ilist[i].type].push_back(ilist[i].start - ilist[i - 1].end);
				total += 2;
			}
			else total++;
		}
		if (ilist[0].type == ilist[ac + aj-1].type){
			slist[ilist[0].type].push_back(ilist[0].start+1440 - ilist[ac+aj - 1].end);
			total += 2;
		}
		else total++;

		sort(slist[0].begin(), slist[0].end());
		sort(slist[1].begin(), slist[1].end());
		int ans = 0;
		//cout << sum[0] << " " << sum[1] << " before " << endl;
		for (int i = 0; i < slist[0].size(); i++){
			if (slist[0][i] + sum[0]>720) break;
			sum[0] += slist[0][i];
			ans++;
		}
		for (int i = 0; i < slist[1].size(); i++){
			if (slist[1][i] + sum[1]>720) break;
			sum[1] += slist[1][i];
			ans++;
		}
		//cout << sum[0]<<" "<<sum[1]<<" "<<total << " " << ans << endl;
		fout <<total- ans*2 << endl;

	}
	system("Pause");
	return 0;
}
