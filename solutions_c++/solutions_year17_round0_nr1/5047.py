#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
#include <cstdlib>
#include <time.h>
#include <bits/stdc++.h>


using namespace std;

void flip(string & s , int l, int r){
	int i;
	for(i=l;i<=r;i++){
		if(s[i] == '+')s[i] = '-';
		else s[i] = '+';
	}
}

int check(string s){
	int i;
	for(i=0;i<s.length();i++)if(s[i] == '-')return 0;
	return 1;
}

int main(){
	int k,i,j;
	string s;
	int t;
	cin >> t;
	for(i=1;i<=t;i++){
		cin >> s;
		cin >> k;
		int count = 0;
		int n = s.length();
		for(j=0;j<n;j++){
			if(s[j] == '-' and j+k-1 <= n-1){
				flip(s,j,j+k-1);
				count ++;

			}
		}
		cout << "Case #" << i << ": ";
		if(check(s)) cout << count << endl;
		else cout << "Impossible" << endl;

	}
}