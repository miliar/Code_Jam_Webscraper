//============================================================================
// Name        : Test2.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <bits/stdc++.h>
using namespace std;

int T, R[55], Q[55][55], N, P, st[55];
bool solve(int i, int x){
	if(i == N)return true;

	while(st[i] < P){
		int si = (10 * Q[i][st[i]] + (11 * R[i]) - 1) / (11 * R[i]), di = (10 * Q[i][st[i]]) / (9 * R[i]);
		//cout << i << ',' << st[i] << ' ' << si << ',' << di << endl;
		if((di < si) || (di < x)){
			st[i]++;
			continue;
		}
		if(x < si)return false;

		if(solve(i + 1, x)){
			st[i]++;
			return true;
		}else return false;
	}
	return false;
}
int main(){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		scanf("%d %d", &N, &P);
		for(int i = 0; i < N; i++)
			scanf("%d", &R[i]);

		for(int i = 0; i < N; i++){
			for(int j = 0; j < P; j++)
				scanf("%d", &Q[i][j]);
			sort(Q[i], Q[i] + P);
		}

		for(int i = 0; i < N; i++)
			st[i] = 0;

		vector <int> v;
		for(int i = 0; i < P; i++){
			int si = (10 * Q[0][i] + (11 * R[0]) - 1) / (11 * R[0]), di = (10 * Q[0][i]) / (9 * R[0]);
			for(int k = si; k <= di; k++)v.push_back(k);
		}
		sort(v.begin(), v.end());
		v.resize(unique(v.begin(), v.end()) - v.begin());

		int res = 0;
		for(int i = 0; i < (int)v.size(); i++)
			while(solve(0, max(1, v[i])))res++;

		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}
