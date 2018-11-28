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

const int maxn = 18;
long long power[maxn];
long long allOne[maxn];

void init(){
	power[0] = allOne[0] = 1;
	for (int i = 1; i < maxn; i++){
		power[i] = power[i - 1] * 10;
		allOne[i] = allOne[i - 1] + power[i];
	}
}


int main(){
	ios_base::sync_with_stdio(false);
	int t;
	ifstream fin;
	fin.open("C-large.in");
	fin >> t;
	ofstream fout;
	fout.open("3-3.out");
	init();
	for (int ti = 1; ti <= t; ti++){
		fout << "Case #" << ti << ": ";
		long long n, k;
		fin >> n >> k;
		long long base = 1;
		long long entered = 0;
		while (entered+base < k){
			entered += base;
			base *= 2;
		}
		long long rmin = (n - entered) / base;
		long long remain = (n - entered) % base;
		if (k - entered <= remain){
			fout <<rmin-rmin/2<<" "<<rmin/2<<endl;
		}
		else{
			fout <<  rmin-1 -(rmin-1) / 2 << " " << (rmin-1) / 2 << endl;
		}
		
	}
	system("Pause");
	return 0;
}
