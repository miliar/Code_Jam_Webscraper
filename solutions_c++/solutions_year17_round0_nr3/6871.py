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

//void C_small(){
//	int t;
//	cin >> t;
//	vector < pair<int, int> > v(1000);
//	vector <char> flag(1000);
//	for (int c = 1; c <= t; c++){
//		int n, k;
//		cin >> n >> k;
//		memset(flag, 0, sizeof(flag) * n);
//		int min_pos;
//		for (int i = )
//		for(int i = 0; i < n; i ++)
//	}
//}

void C_small(){
	int t;
	cin >> t;
//	vector < pair<int, int> > v(1000);

	for (int c = 1; c <= t; c++){
		int n, k;
		cin >> n >> k;
		vector <int> v;
		v.push_back(-1);
		v.push_back(n);
		int max_pos;
		int pos = -1;
		for(int i = 0; i < k; i ++){
//			cout << "===========" << endl;
			int max_max = INT32_MIN;
			int max_min = INT32_MIN;
			pos = -1;
			for (int j = 1; j < v.size(); j ++){
//				cout << "cir " << v[j] << endl;
				if (v[j] == v[j - 1] + 1) continue;
				int new_pos = (v[j - 1] + v[j]) / 2;
				int minv = min (new_pos - v[j - 1] - 1, v[j] - new_pos - 1);
				int maxv = max (new_pos - v[j - 1] - 1, v[j] - new_pos - 1);
				if (minv > max_min){
					max_min = minv;
					max_max = maxv;
					max_pos = new_pos;
//					cout << " => max pos " << max_pos << endl;
					pos = j - 1;
				} else if (minv == max_min && maxv > max_max){
					max_max = maxv;
					max_pos = new_pos;
					pos = j - 1;
				}
			}

//			cout << "max pos " << max_pos << endl;
//			cout << "pos is " << pos << endl;
			v.insert(v.begin() + pos + 1, max_pos);
//			for(int x : v)
//				cout << x << " ";
//			cout << endl;
		}
//		cout << "pos is " << pos << endl;
//		cout << "=> gap is " << gap << endl;
		int l = v[pos + 1] - v[pos] - 1;
		int r = v[pos +2 ] - v[pos + 1] - 1;
//		cout << l << " " << r << endl;
		cout << "Case #" << to_string(c) << ": " << max(l,r) << " " << min(l, r) << endl;
	}
}

int main() {
//	A();
//	B_small();
	C_small();
	return 0;
}
