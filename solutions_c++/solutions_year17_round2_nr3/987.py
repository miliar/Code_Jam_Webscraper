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
		int N,Q;
		cin >> N >> Q;
		vector<int> E(N),S(N);
		vector< vector< pair<int,int> > > G(N);
		for(int i =0; i < N; i++) cin >> E[i] >> S[i];
		for(int i =0; i < N; i++) for(int j =0; j < N; j++) {
			int a;
			cin >> a;
			if(a == -1) continue;
			G[i].push_back(make_pair(j,a));}
		vector< vector<double> > D(N,vector<double>(N,1e18));
		for(int i =0; i < N; i++) {
			vector<long long> dist(N,1e18);
			dist[i] =0;
			priority_queue< pair<long long,int>, vector< pair<long long,int> >, greater< pair<long long,int> > > q;
			q.push(make_pair(0,i));
			while(!q.empty()) {
				pair<long long,int> p =q.top();
				q.pop();
				if(p.ff != dist[p.ss]) continue;
				ALL_THE(G[p.ss],it) if(dist[it->ff] > p.ff+it->ss) {
					dist[it->ff] =p.ff+it->ss;
					q.push(make_pair(dist[it->ff],it->ff));}
				}
			for(int j =0; j < N; j++) if(dist[j] <= E[i]) {
				D[i][j] =min(D[i][j],1.0*dist[j]/S[i]);}
			}
		for(int i =0; i < N; i++) D[i][i] =0;
		for(int i =0; i < N; i++) for(int j =0; j < N; j++)
			for(int k =0; k < N; k++)
				D[j][k] =min(D[j][k],D[j][i]+D[i][k]);
		vector<int> visq(N,0);
		for(int q =0; q < Q; q++) {
			int u,v;
			cin >> u >> v;
			u--, v--;
			cout << D[u][v] << ((q == Q-1)?"\n":" ");}
		}
	return 0;}

// look at my code
// my code is amazing
