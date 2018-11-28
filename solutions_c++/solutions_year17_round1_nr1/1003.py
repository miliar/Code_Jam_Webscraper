#include <bits/stdc++.h>
// iostream is too mainstream
#include <cstdio>
// bitch please
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <list>
#include <cmath>
#include <iomanip>
#include <time.h>
#define dibs reserve
#define OVER9000 1234567890123456789LL
#define ALL_THE(CAKE,LIE) for(auto LIE =CAKE.begin(); LIE != CAKE.end(); LIE++)
#define tisic 47
#define soclose 1e-8
#define chocolate win
// so much chocolate
#define patkan 9
#define ff first
#define ss second
#define abs(x) ((x < 0)?-(x):x)
#define uint unsigned int
#define dbl long double
#define pi 3.14159265358979323846
using namespace std;
// mylittledoge

#ifdef DONLINE_JUDGE
	// palindromic tree is better than splay tree!
	#define lld I64d
#endif

int main() {
	cin.sync_with_stdio(0);
	cin.tie(0);
	cout << fixed << setprecision(10);
	int T;
	cin >> T;
	for(int t =0; t < T; t++) {
		cout << "Case #" << t+1 << ":\n";
		int R,C;
		cin >> R >> C;
		vector<string> V(R);
		for(int i =0; i < R; i++) cin >> V[i];
		vector< vector<int> > L(C);
		for(int i =0; i < C; i++) for(int j =0; j < R; j++)
			if(V[j][i] != '?') L[i].push_back(j);
		int a =0;
		for(int i =0; i < C; i++) {
			while(a < C && L[a].empty()) a++;
			if(a == C) {
				for(int j =0; j < R; j++) V[j][i] =V[j][i-1];
				continue;}
			int b =0;
			for(int j =0; j < (int)L[a].size(); j++) 
				while(b < ((j == (int)L[a].size()-1)?R:L[a][j+1])) {
					for(int k =i; k <= a; k++) V[b][k] =V[L[a][j]][a];
					b++;}
			i =a;
			a++;}
		for(int i =0; i < R; i++) cout << V[i] << "\n";}
	return 0;}

// look at my code
// my code is amazing
