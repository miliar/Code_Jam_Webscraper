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



int main(){
	ios_base::sync_with_stdio(false);
	int t;
	ifstream fin;
	fin.open("A-large.in");
	fin >> t;
	ofstream fout;
	fout.open("1-large.out");
	for (int ti = 1; ti <= t; ti++){
		fout << "Case #" << ti << ": ";
		int ans = 0;
		string s;
		int k;
		fin >> s >> k;
		//cout << s << " "<<k << endl;
		for (int i = 0; i+k <= s.size(); i++){
			if (s[i] == '-'){
				ans++;
				for (int j = 0; j < k; j++){
					if (s[i + j] == '+')s[i + j] = '-';
					else s[i + j] = '+';
				}
			}
		}
		//cout << ans << " " << s << endl;
		for (int i = s.size() - k; i < s.size(); i++){
			if (s[i] == '-') ans = -1;
		}
		if (ans == -1) fout << "IMPOSSIBLE" << endl;
		else fout << ans << endl;
	}
	system("Pause");
	return 0;
}
