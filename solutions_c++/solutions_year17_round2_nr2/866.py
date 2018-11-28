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
#define OVER9000 1234567890
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
	int col[26];
	col['B'-'A'] =4;
	col['R'-'A'] =1;
	col['Y'-'A'] =2;
	col['O'-'A'] =3;
	col['V'-'A'] =5;
	col['G'-'A'] =6;
	string inv =".RYOBVG";
	for(int t =0; t < T; t++) {
		cout << "Case #" << t+1 << ": ";
		int N,cnt[7];
		cin >> N >> cnt[1] >> cnt[3] >> cnt[2] >> cnt[6] >> cnt[4] >> cnt[5];
		if(2*max(cnt[1],max(cnt[2],cnt[4])) > cnt[1]+cnt[2]+cnt[4]) {
			cout << "IMPOSSIBLE\n";
			continue;}
		string S;
		for(int i =0; i < N; i++) {
			int a =0;
			for(int j =0; j < 3; j++) 
				if(S.empty() || col[S[S.length()-1]-'A'] != (1<<j)) a =max(a,cnt[1<<j]);
			bool done =false;
			for(int j =0; j < 3; j++) 
				if(S.empty() || col[S[S.length()-1]-'A'] != (1<<j)) if(a == cnt[1<<j]) {
					if(col[S[0]-'A'] != (1<<j)) continue;
					done =true;
					S +=inv[1<<j];
					cnt[1<<j]--;
					break;}
			if(done) continue;
			for(int j =0; j < 3; j++) 
				if(S.empty() || col[S[S.length()-1]-'A'] != (1<<j)) if(a == cnt[1<<j]) {
					S +=inv[1<<j];
					cnt[1<<j]--;
					break;}
			}
		cout << S << "\n";}
	return 0;}

// look at my code
// my code is amazing
