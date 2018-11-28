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

vector< vector< vector< pair<int,int> > > > cov;

int main() {
	cin.sync_with_stdio(0);
	cin.tie(0);
	cout << fixed << setprecision(10);
	int T;
	cin >> T;
	for(int t =0; t < T; t++) {
		if(T >= 10) {cerr << t << ((t == T-1)?"\n":" "); flush(cerr);}
		cout << "Case #" << t+1 << ": ";
		int R,C;
		cin >> R >> C;
		vector<string> V(R);
		for(int i =0; i < R; i++) cin >> V[i];
		bool pos =true;
		vector< pair<int,int> > opt;
		cov.clear();
		cov.resize(R,vector< vector< pair<int,int> > >(C));
		map<int,int> M;
		for(int i =0; i < R; i++) for(int j =0; j < C; j++) if(V[i][j] == '|' || V[i][j] == '-') {
			bool isH =true, isV =true;
			for(int k =j+1; k < C; k++) {
				if(V[i][k] == '#') break;
				if(V[i][k] != '.') isH =false;}
			for(int k =j-1; k >= 0; k--) {
				if(V[i][k] == '#') break;
				if(V[i][k] != '.') isH =false;}
			for(int k =i+1; k < R; k++) {
				if(V[k][j] == '#') break;
				if(V[k][j] != '.') isV =false;}
			for(int k =i-1; k >= 0; k--) {
				if(V[k][j] == '#') break;
				if(V[k][j] != '.') isV =false;}
			if(isH) {
				for(int k =j+1; k < C; k++) {
					if(V[i][k] == '#') break;
					if(V[i][k] == '.') cov[i][k].push_back(make_pair(i*C+j,1));}
				for(int k =j-1; k >= 0; k--) {
					if(V[i][k] == '#') break;
					if(V[i][k] == '.') cov[i][k].push_back(make_pair(i*C+j,1));}
				}
			if(isV) {
				for(int k =i+1; k < R; k++) {
					if(V[k][j] == '#') break;
					if(V[k][j] == '.') cov[k][j].push_back(make_pair(i*C+j,0));}
				for(int k =i-1; k >= 0; k--) {
					if(V[k][j] == '#') break;
					if(V[k][j] == '.') cov[k][j].push_back(make_pair(i*C+j,0));}
				}
			if(!isH && !isV) {pos =false; break;}
			if(isH && !isV) V[i][j] ='-';
			if(!isH && isV) V[i][j] ='|';
			if(isH && isV) V[i][j] ='A';
			int m =M.size();
			M[i*C+j] =m;}
		for(int i =0; i < R; i++) for(int j =0; j < C; j++) if(V[i][j] == 'A' || V[i][j] == '|' || V[i][j] == '-') 
			opt.push_back(make_pair(i,j));
		int O =opt.size();
		vector<int> X(2*O,0);
		vector< vector<int> > G(2*O);
		for(int i =0; i < R; i++) for(int j =0; j < C; j++) {
			if(V[i][j] == '|') X[2*M[i*C+j]] =1;
			if(V[i][j] == '-') X[2*M[i*C+j]+1] =1;}
		for(int i =0; i < R; i++) for(int j =0; j < C; j++) if(V[i][j] == '.') {
			if(cov[i][j].empty()) {pos =false; break;}
			if(cov[i][j].size() == 1) X[2*M[cov[i][j][0].ff]+cov[i][j][0].ss] =1;
			else {
				G[2*M[cov[i][j][0].ff]+1-cov[i][j][0].ss].push_back(2*M[cov[i][j][1].ff]+cov[i][j][1].ss);
				G[2*M[cov[i][j][1].ff]+1-cov[i][j][1].ss].push_back(2*M[cov[i][j][0].ff]+cov[i][j][0].ss);}
			}
		if(!pos) {cout << "IMPOSSIBLE\n"; continue;}
		for(int i =0; i < O; i++) if(X[i] == 1) {
			queue<int> q;
			q.push(i);
			while(!q.empty()) {
				ALL_THE(G[q.front()],it) if(X[*it] == 0) {
					X[*it] =1;
					q.push(*it);}
				q.pop();}
			}
		for(int i =0; i < O; i++) if(X[2*i] == 1 && X[2*i+1] == 1) pos =false;
		if(!pos) {cout << "IMPOSSIBLE\n"; continue;}
		for(int i =0; i < O; i++) if(X[2*i] == 0 && X[2*i+1] == 0) {
			queue<int> q;
			vector<int> Y =X;
			q.push(2*i);
			Y[2*i] =1;
			while(!q.empty()) {
				ALL_THE(G[q.front()],it) if(Y[*it] == 0) {
					Y[*it] =1;
					q.push(*it);}
				q.pop();}
			bool ok =true;
			for(int j =0; j < O; j++) if(Y[2*j] == 1 && Y[2*j+1] == 1) ok =false;
			if(ok) {X =Y; continue;}
			q.push(2*i+1);
			X[2*i+1] =1;
			while(!q.empty()) {
				ALL_THE(G[q.front()],it) if(X[*it] == 0) {
					X[*it] =1;
					q.push(*it);}
				q.pop();}
			ok =true;
			for(int j =0; j < O; j++) if(X[2*j] == 1 && X[2*j+1] == 1) ok =false;
			if(!ok) {pos =false; break;}
			}
		if(!pos) {cout << "IMPOSSIBLE\n"; continue;}
		else {
			cout << "POSSIBLE\n";
			for(int i =0; i < O; i++) {
				if(X[2*i]) V[opt[i].ff][opt[i].ss] ='|';
				else V[opt[i].ff][opt[i].ss] ='-';}
			for(int i =0; i < R; i++) cout << V[i] << "\n";
			}
		}
	return 0;}

// look at my code
// my code is amazing