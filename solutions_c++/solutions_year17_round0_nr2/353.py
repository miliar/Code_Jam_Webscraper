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
	fin.open("B-small.in");
	fin >> t;
	ofstream fout;
	fout.open("2.out");
	init();
	for (int ti = 1; ti <= t; ti++){
		fout << "Case #" << ti << ": ";
		long long n;
		fin >> n;
		if (n == 1e18) n--;
		int last = 0;
		long long ans = 0;
		for (int i = 17; i >= 0; i--){
			if (allOne[i]+ans > n) continue;
			for (int digit = 9; digit >= last; digit--){
				if (digit*allOne[i] + ans <= n){
					ans += digit*power[i];
					last = digit;
					break;
				}
			}
		}
		fout << ans << endl;
	}
	system("Pause");
	return 0;
}
