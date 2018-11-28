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

typedef long long cat;

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
		if(T >= 10) {cerr << t << ((t == T-1)?"\n":" "); flush(cerr);}
		cout << "Case #" << t+1 << ": ";
		int N,C,M;
		cin >> N >> C >> M;
		vector< vector<int> > S(C);
		for(int i =0; i < M; i++) {
			int a,b;
			cin >> a >> b;
			S[b-1].push_back(a-1);}
		int p1[2] ={0,0};
		for(int i =0; i < 2; i++) ALL_THE(S[i],it) if(*it == 0) p1[i]++;
		int ans1 =p1[0]+p1[1];
		int p2[2] ={0,0};
		for(int i =0; i < 2; i++) p2[i] =S[i].size()-p1[i];
		int x =min(p2[0],p1[1]);
		p1[1] -=x, p2[0] -=x;
		x =min(p2[1],p1[0]);
		p1[0] -=x, p2[1] -=x;
		ans1 +=max(p2[0],p2[1]);
		cout << ans1 << " ";
		sort(begin(S[0]),end(S[0]));
		sort(begin(S[1]),end(S[1]));
		vector< pair<int,int> > tr(ans1,make_pair(-1,-1));
		for(int i =0; i < S[0].size(); i++) tr[i].ff =S[0][i];
		for(int i =0; i < S[1].size(); i++) tr[ans1-1-i].ss =S[1][i];
		int eq =0, v =-1;
		for(int i =0; i < ans1; i++) if(tr[i].ff == tr[i].ss && tr[i].ff != -1) {
			eq++;
			v =tr[i].ff;}
		int neq =0;
		for(int i =0; i < ans1; i++) if(tr[i].ff != v && tr[i].ss != v) neq++;
		int ans2 =0;
		if(v != -1) ans2 =max(0,eq-neq);
		cout << ans2 << "\n";}
	return 0;}

// look at my code
// my code is amazing