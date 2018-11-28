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

string fileinPath = "D:\\workspace\\A-large.in";
//string fileinPath = "D:\\workspace\\C-large.in";
//string fileinPath = "D:\\workspace\\in.txt";
string fileoutPath = "D:\\workspace\\out.txt";
fstream fin(fileinPath);
ofstream fout(fileoutPath);

 
void f(int r, int c, vector<string>& x) {
	for (int i = 0; i < r; i++) {
		char pre = '#';
		for (int j = 0; j < c; j++) { // each line
			if (x[i][j] != '?') {
				pre = x[i][j];
				if (j > 0 && x[i][j-1] == '?') {
					int k = j - 1;
					while (k >= 0) x[i][k--] = pre;
				}
			}
			else if (pre != '#') x[i][j] = pre;
		}
		if (pre =='#' && i>0 && x[i-1][0]!='?') 
			x[i] = x[i - 1];
		if (pre != '#' && i>0 && x[i - 1][0] == '?') 
			for (int k = i - 1; k >= 0 && x[k][0]=='?'; k--)  
				x[k] = x[k + 1] ;
	}
}

int main()
{
	int num;
	int r, c;
	vector<string> x;
	while (fin >> num) {
		for (int i = 1; i <= num; i++) {
			fin >> r >> c;
			x = {};
			for (int i = 0; i < r; i++) {
				string tmp;
				fin >> tmp;
				x.push_back(tmp);
			}
			f(r, c, x);
			fout << "Case #" << i << ": " << endl;
			for (auto a:x ) 
				fout << a << endl;
		}
	}
}

