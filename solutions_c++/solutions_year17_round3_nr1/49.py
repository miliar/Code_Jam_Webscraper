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
		int N,K;
		cin >> N >> K;
		vector< pair<long long,long long> > P(N);
		for(int i =0; i < N; i++) {
			long long r,h;
			cin >> r >> h;
			P[i].ff =r;
			P[i].ss =r*h;}
		sort(begin(P),end(P));
		long long sum =0, ans =0;
		multiset<long long> S;
		for(int i =0; i < K-1; i++) {
			sum +=P[i].ss;
			S.insert(P[i].ss);}
		for(int i =0; i <= N-K; i++) {
			ans =max(ans,P[i+K-1].ff*P[i+K-1].ff+2*P[i+K-1].ss+2*sum);
			if(i == N-K) break;
			sum +=P[i+K-1].ss;
			S.insert(P[i+K-1].ss);
			sum -=*S.begin();
			S.erase(S.begin());}
		cout << ans*pi << "\n";}
	return 0;}

// look at my code
// my code is amazing
