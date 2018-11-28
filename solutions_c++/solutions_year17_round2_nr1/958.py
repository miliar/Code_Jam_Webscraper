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
		int D,N;
		cin >> D >> N;
		vector< pair<int,int> > H(N);
		for(int i =0; i < N; i++) cin >> H[i].ff >> H[i].ss;
		sort(begin(H),end(H));
		vector< pair<int,int> > H2;
		for(int i =0; i < N; i++) 
			if(H2.empty() || H2.back().ss > H[i].ss) H2.push_back(H[i]);
		N =H2.size();
		while(true) {
			double tt =1e5;
			int fc =-1;
			for(int i =0; i < N-1; i++) {
				double tc =(H2[i+1].ff-H2[i].ff)/(H2[i].ss-H2[i+1].ss);
				if(tc*H2[i].ss+H2[i].ff < D-soclose) {
					tt =min(tt,tc);
					if(abs(tc-tt) < soclose) fc =i;}
				}
			if(fc == -1) break;
			H2.erase(H2.begin()+fc);
			N--;}
		cout << 1.0*D*H2[0].ss/(D-H2[0].ff) << "\n";}
	return 0;}

// look at my code
// my code is amazing
