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

//string fileinPath = "D:\\workspace\\B-small-attempt0.in";
string fileinPath = "D:\\workspace\\B-large.in";
//string fileinPath = "D:\\workspace\\in.txt";
string fileoutPath = "D:\\workspace\\out.txt";
fstream fin(fileinPath);
ofstream fout(fileoutPath);

string f(string s) {
	if (s.size() <= 1) return s;
	int n = s.size();
	int tail = n - 1;
	for (int i=n-1; i >0 ; i--) {
		if (s[i]>=s[i-1]) continue;
		s[i-1]--;
		for (int j=i; j <= tail; j++) s[j] = '9';
		tail = i - 1;
	}
	return s[0]=='0'?s.substr(1, n-1) : s;
}

int main()
{
	int num;
	string n;
	while (fin >> num) {
		for (int i = 1; i <= num; i++) {
			fin >> n;
			string x = f(n);
			fout << "Case #" << i << ": " << x << endl;
		}
	}
}

