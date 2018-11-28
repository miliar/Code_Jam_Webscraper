// Created by alex_mat21. And it works!

#include <iostream>
#include <fstream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstring>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <sstream>
#include <stdio.h>
#include <math.h>
#include <bitset>
#include <string> 
#include <iomanip>
#include <cmath>
#include <utility>
#include <ctime>
#include <cstdlib>

#define FOR(i,n) for(int i=0,_n=n;i<_n;i++)
#define FORR(i,s,n) for(int i=s,_n=n;i<_n;i++)

using namespace std;

ifstream in;
ofstream out;

int n, p, k, t, cnt,lt,rt;
vector <int> r;
vector <vector <int> > q;
int x[60];

int up(int i, int j){
	return (10*q[i][j])/(9*r[i]);
}

int down(int i, int j){
	return (10*q[i][j] + 11*r[i] - 1)/(11*r[i]);
}

void main_solve() {
	in >> n >> p;
	FOR(i,n){
		in >> k;
		r.push_back(k);
	}
	FOR(i,n){
		vector <int> q0;
		FOR(j,p){
			in >> k;
			q0.push_back(k);
		}
		sort(q0.begin(),q0.end());
		q.push_back(q0);
	}
	cnt=0;
	memset(x,0,sizeof x);
	FOR(i,p){
		lt=down(0,i);
		rt=up(0,i);
		//cout << i << ' ' << lt << ' ' << rt << endl;
		for (int m=lt; m<=rt; m++){
			t=1;
			for (int j=1; j<n; j++){
				//cout << j << ' ' << x[j] << ' ' << down(1,x[1]) << ' ' << up(1,x[1]) << " !!!!" <<endl;
				while (x[j]<p && up(j,x[j])<m)
					x[j]++;
				if (x[j]==p || (x[j]<p && down(j,x[j])>m)){
					t=0;
					break;
				}
			}
			//cout << x[1] << ' ' << t << endl;
			if (t){
				cnt++;
				for (int j=1; j<n; j++)
					x[j]++;
				break;
			}
		}
		
	}
	r.clear();
	q.clear();
	out << cnt << endl;
}

int main() {
	in.open("input.in");
	out.open("output.out");
	clock_t start;
	int t;
	in >> t;
	for (int i=0 ; i<t; i++) {
		cout << "Starting case: " << i+1 << endl;
		out << "Case #"<< i+1 << ": ";
		start = clock();
		main_solve();
		cout << "Time: " << (clock()-start)/(double)CLOCKS_PER_SEC << "s" << endl;
	}
	in.close();
	out.close();
	return 0;
}
