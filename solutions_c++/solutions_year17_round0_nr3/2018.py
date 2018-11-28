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
	for(int t =0; t < T; t++) {
		cout << "Case #" << t+1 << ": ";
		long long N,K;
		cin >> N >> K;
		map<long long,long long> M;
		M[N] =1;
		while(K > 1) {
			auto it =M.end(); it--;
			if(it->ss >= K) break;
			K -=it->ss;
			if(it->ff&1) 
				M[it->ff/2] +=2*it->ss;
			else {
				M[it->ff/2] +=it->ss;
				M[it->ff/2-1] +=it->ss;}
			M.erase(it);}
		auto it =M.end(); it--;
		cout << it->ff/2 << " " << it->ff/2-1+(it->ff&1) << "\n";
		}
	return 0;}

// look at my code
// my code is amazing
