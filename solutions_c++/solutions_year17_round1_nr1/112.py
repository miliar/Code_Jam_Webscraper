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


int r, c, t;
char a[25][25];
char ch;

bool check(int k) {
	FOR(j,r){
		if (a[k][j]!='?')
				return true;
	}
	return false;
}

void fill(int k) {
	int i = 0;
	while (a[k][i]=='?')
		i++;
	FOR(j,i)
		a[k][j]=a[k][i];
	ch = a[k][i];
	while (i<r) {
		if (a[k][i]=='?')
			a[k][i]=ch;
		else
			ch = a[k][i];
		i++;
	}  
}

void main_solve() {
	in >> r >> c;
	FOR(j,r){
		FOR(i,c){
			in >> a[i][j];
		}
	}
	int k = 0;
	while (!check(k)) {
		k++;
	}
	fill(k);
	for(int j=k-1; j>=0; j--){
		FOR(i,r)
			a[j][i] = a[j+1][i];
	}
	k++;
	while (k<c){
		if (check(k))
			fill(k);
		else{
			FOR(i,r)
				a[k][i] = a[k-1][i];
		}
		k++;
	}
	FOR(j,r){
		FOR(i,c){
			out << a[i][j];
		}
		out << endl;
	}
}

int main() {
	in.open("input.in");
	out.open("output.out");
	clock_t start;
	int t;
	in >> t;
	for (int i=0 ; i<t; i++) {
		cout << "Starting case: " << i+1 << endl;
		out << "Case #"<< i+1 << ":" << endl;
		start = clock();
		main_solve();
		cout << "Time: " << (clock()-start)/(double)CLOCKS_PER_SEC << "s" << endl;
	}
	in.close();
	out.close();
	return 0;
}
