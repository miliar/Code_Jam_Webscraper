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

int n, p,m;
int a[20];

void main_solve() {
	in >> n >> p;
	memset(a, 0, sizeof a);
	FOR(i,n){
		int k;
		in >> k;
		a[k%p]++;
	}
	m=a[0];
	if (p==2){
		m+=(a[1]+1)/2;
	} else if (p==3) {
		int k=min(a[1], a[2]);
		m+=k;
		a[1]-=k;
		a[2]-=k;
		m+=(a[1]+2)/3;
		m+=(a[2]+2)/3;
	}
	
	out << m << endl;
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
