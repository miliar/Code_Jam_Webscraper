#include"stdafx.h"
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<assert.h>
#include<ctime>
#include<queue>
#include<fstream>
#include<string>
using namespace std;

const int maxn = 60;
double prob[maxn];

bool check(int n,double g, double u){
	double temp = 0;
	for (int i = 0; i < n; i++){
		if (prob[i] < g) temp += g - prob[i];
	}
	if (temp < u) return true;
	else return false;
}

double bin_search(int n, double u){
	double lo = 0;
	double hi = 1;
	while (hi - lo>1e-8){
		double mid = (hi + lo) / 2;
		if (check(n, mid, u)) lo = mid;
		else hi = mid;
	}
	double ans = 1;
	for (int i = 0; i < n; i++){
		if (prob[i] < lo) ans *= lo;
		else ans *= prob[i];
	}
	return ans;
}

int main(){
	ios_base::sync_with_stdio(false);
	int t;
	ifstream fin;
	fin.open("C-small-1-attempt0.in");
	fin >> t;
	ofstream fout;
	fout.open("3.out");
	fout.precision(20);
	fout.setf(ios::fixed);

	for (int ti = 1; ti <= t; ti++){
		fout << "Case #" << ti << ": ";

		int n, k;
		fin >> n >> k;
		double u;
		fin >> u;

		for (int i = 0; i < n; i++)fin >> prob[i];
		fout << bin_search(n, u) << endl;


	}
	system("Pause");
	return 0;
}
