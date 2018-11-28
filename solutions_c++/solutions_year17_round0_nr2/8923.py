//============================================================================
// Name        : GCJ.cpp
// Author      : Fei Bi
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <stdlib.h>
#include <algorithm>
#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include <cfloat>
#include <string>
#include <stack>
#include <sstream>
#include <math.h>
#include <iomanip> //for set precision
#include <unordered_map>
#include <unordered_set>
using namespace std;

void split(const string& s, char delim,vector<string>& v) {
    auto i = 0;
    auto pos = s.find(delim);
    while (pos != string::npos) {
      v.push_back(s.substr(i, pos-i));
      i = ++pos;
      pos = s.find(delim, pos);

      if (pos == string::npos)
         v.push_back(s.substr(i, s.length()));
    }
}

void A(){
	int n;
	cin >> n;
	string line;
	int k;
	for(int index = 0; index < n; index ++){
		cin >> line;
		cin >> k;
		int i = 0;
		int cnt = 0;
		bool out = false;

		while (true){
			if (i >= line.size()) break;
			while (i <= line.size() - k && line[i] != '-') i ++;
			if (i > line.size() - k){
				while (i < line.size()){
					if (line[i] == '-') {
						cnt = -1;
						out = true;
						break;
					}
					i ++;
				}
			} else {
				cnt ++;
				for(int j = 0; j < k; j++)
					line[i + j] = (line[i + j] == '+') ? '-' : '+';
			}
			if(out) break;
		}
		cout << "Case #" << to_string(index + 1) << ": " << ((cnt == -1) ? "IMPOSSIBLE" : to_string(cnt)) << endl;
	}
}

bool check (string & a){
	int l = a.size();
	if (l == 1) return true;
	for (int i = 1; i < l; i ++)
		if(a[i] < a[i-1])	return false;
	return true;
}

void B_small(){
	int n;
	cin >> n;
	string a;
	for (int c = 1; c <= n; c++){
		cin >> a;
		while (!check(a)){
			int b = stoi(a);
			b--;
			a = to_string(b);
		}
		cout << "Case #" << to_string(c) << ": " << a << endl;
	}

}

int main() {
//	A();
	B_small();
	return 0;
}
