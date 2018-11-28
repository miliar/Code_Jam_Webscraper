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
int ans[maxn];

void solve_basic(int n,int r, int g, int b){
	fill(ans, ans + n, 0);
	int ind = 0;
	while (b > 0){
		ans[ind] = 2;
		if (r >= g) {
			ans[ind + 1] = 0;
			r--;
		}
		else {
			ans[ind + 1] = 1;
			g--;
		}
		b--;
		ind += 2;
	}
	while (ind<n){
		if (ans[ind - 1] == 0){
			ans[ind] = 1;
			g--;
		}
		else{
			ans[ind] = 0;
			r--;
		}
		ind++;
	}
}




int main(){
	ios_base::sync_with_stdio(false);
	int t;
	ifstream fin;
	fin.open("B-small-attempt1.in");
	fin >> t;
	ofstream fout;
	fout.open("2.out");
	fout.precision(20);
	fout.setf(ios::fixed);

	for (int ti = 1; ti <= t; ti++){
		fout << "Case #" << ti << ": ";

		int N, R, O, Y, G, B,V;
		fin >> N >> R >> O >> Y >> G >> B>>V;
		if (Y > N / 2 || R > N / 2 || B > N / 2) fout << "IMPOSSIBLE";
		else{
			pair<int,char> temp[3];
			temp[0] = make_pair(R, 'R'), temp[1] = make_pair(Y, 'Y'), temp[2]= make_pair(B, 'B');
			sort(temp, temp + 3);
			solve_basic(N,temp[0].first, temp[1].first, temp[2].first);
			for (int i = 0; i < N; i++){
				//cout << i << " " << ans[i] << endl;
				fout << temp[ans[i]].second;
			}
		}
		fout << endl;
	}
	system("Pause");
	return 0;
}
