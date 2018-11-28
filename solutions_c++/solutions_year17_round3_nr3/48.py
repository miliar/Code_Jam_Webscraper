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
		double U;
		cin >> N >> K >> U;
		vector<double> P(N);
		for(int i =0; i < N; i++) cin >> P[i];
		sort(begin(P),end(P));
		for(int i =0; i < N; i++) {
			double m =(i == N-1)?1:P[i+1];
			double x =min(m-P[i],U/(i+1));
			for(int j =0; j <= i; j++) P[j] +=x, U -=x;
			}
		double ans =1;
		for(int i =0; i < N; i++) ans *=P[i];
		cout << ans << "\n";}
	return 0;}

// look at my code
// my code is amazing
