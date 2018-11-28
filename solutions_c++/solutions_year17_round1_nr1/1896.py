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

bool check(string & line){
	for (char c : line)
		if (c != '?')
			return true;

	return false;
}

void A(){
	int n;
	cin >> n;
	string line;
	for(int index = 0; index < n; index ++){

		int a, b;
		cin >> a >> b;
		vector <string> v(a);
		for (int i = 0; i < a ; i ++){
			cin >> line;
			if(check(line) == false){
				v[i] = line;
				continue;
			}
			char last = '?';
			for (int j = 0; j < line.size(); j ++){
				if (line[j] == '?' && last != '?')
					line[j] = last;
				if (line[j] != '?')
					last = line[j];
			}
			for (int j = line.size() - 1; j >= 0; j--) {
				if (line[j] == '?' && last != '?')
					line[j] = last;
				if (line[j] != '?')
					last = line[j];
			}

//			if (line[0] != '?')
				v[i] = line;
//			else
//				v[a] = v[a-1];
		}
		for (int i = 1; i < v.size(); i ++){
//			cout << v[i] << endl;
			if (v[i][0] == '?')
				v[i] = v[i - 1];
		}

		for (int i = v.size() - 2; i >=0; i--) {
			if (v[i][0] == '?')
				v[i] = v[i + 1];
		}

		cout << "Case #" << to_string(index + 1) << ":" << endl;
		for (auto s : v)
			cout << s << endl;
	}
}


int main() {
	A();
	return 0;
}
