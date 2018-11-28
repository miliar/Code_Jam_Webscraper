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
		long long N;
		cin >> N;

		vector<long long> pos;
		long long x =min(N,9LL);
		while(x <= (N-9)/10) x =x*10+9;
		pos.push_back(x);

		vector<int> dig;
		while(N > 0) {
			dig.push_back(N%10);
			N /=10;}
		int D =dig.size();

		for(int i =-1; i < D; i++) {
			x =0;
			for(int j =D-1; j > i; j--) {
				if(j < D-1 && dig[j] < dig[j+1]) {
					x =-1; 
					break;}
				x =x*10+dig[j];}
			if(x == -1) continue;
			if(i == -1) {
				pos.push_back(x);
				break;}
			for(int d2 =(i == D-1)?0:dig[i+1]; d2 < dig[i]; d2++) {
				long long y =x*10+d2;
				for(int j =0; j < i; j++) y =y*10+9;
				pos.push_back(y);}
			}

		sort(begin(pos),end(pos));
		cout << pos.back() << "\n";}
	return 0;}

// look at my code
// my code is amazing
