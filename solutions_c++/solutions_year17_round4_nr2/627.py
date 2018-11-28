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

int n,c,m,y,z, s;

vector <vector <int> > a;
vector <vector <int> > b;

int x[1000][1000];

void main_solve() {
	in >> n >> c >> m;
	memset(x,0,sizeof x);
	FOR(i,n){
		vector <int> a1;
		a.push_back(a1);
	}
	FOR(i,c){
		vector <int> a1;
		b.push_back(a1);
	}
	FOR(i,m){
		int pi, bi;
		in >> pi >> bi;
		pi--;
		bi--;
		a[pi].push_back(bi);
		b[bi].push_back(pi);
		x[pi][bi]++;
	}
	FOR(i,n){
		sort(a[i].begin(), a[i].end());
	}
	FOR(i,c){
		sort(b[i].begin(), b[i].end());
	}
	y=0;
	z=0;
	FOR(i,c){
		y=max(y,(int) b[i].size());
	}
	s=0;
	FOR(i,n){
		int k = a[i].size();
		if (k>=y){
			int y0,z0;
			int l,r;
			l=y;
			r=k;
			while (l<r){
				int p=(l+r)/2;
				if (p*i-s >=k-p){
					r=p;
				} else {
					l=p+1;
				}
			}
			y0=l;
			z0=k-l;
			if (y0>y || (y0==y && z0<z)){
				y=y0;
				z=z0;
			}
		}
		s+=k;
	}
	s=0;
	z=0;
	FOR(i,n){
		int k = a[i].size();
		if (k>=y){
			z+=k-y;
		}
		s+=k;
	}
	b.clear();
	a.clear();
	out << y << ' ' << z << endl;
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
