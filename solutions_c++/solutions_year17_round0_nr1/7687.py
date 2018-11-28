// codeJam.cpp : 定义控制台应用程序的入口点。
//
#include <stdio.h>  
#include <stdlib.h>  
#include <iostream>  
#include <fstream>
#include <iomanip> 
#include <string>
#include <vector>
#include <map>
#include <unordered_map>
#include <queue>
#include <stack>
#include <list>
#include <algorithm>
#include <cmath>

using namespace std;

//string fileinPath = "D:\\workspace\\A-small-attempt0.in";
string fileinPath = "D:\\workspace\\A-large.in";
//string fileinPath = "D:\\workspace\\in.txt";
string fileoutPath = "D:\\workspace\\out.txt";
fstream fin(fileinPath);
ofstream fout(fileoutPath);

int cntFlip(string& s, int k) {
	int n = s.size();
	int cnt = 0;
	for (int i = 0; i < n; i++) {
		if (s[i] == '+') continue;
		if (i > n - k) return -1;
		cnt++;
		for (int j = 0; j < k; j++) 
			s[i+j] = s[i+j] == '+' ? '-' : '+';
	}
	return cnt;
}

int main()
{
	int num, k;
	string s;
	while (fin >> num) {
		for (int i = 1; i <= num; i++) {
			fin >> s >> k;
			int x = cntFlip(s, k);
			if (x >= 0) fout << "Case #" << i << ": " << x << endl;
			else fout << "Case #" << i << ": IMPOSSIBLE" << endl;
		}
	}
}

