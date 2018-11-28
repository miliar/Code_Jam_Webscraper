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

string mat[26];
char name[700];
pair<int, int> pos[700];

bool cmp(pair<int, int> a, pair<int, int> b){
	if (a.first == b.first) return a.second < b.second;
	return a.first < b.first;
}

bool solved[26];

void solve(int i, int j, int row, int col, char a){
	int l = j;
	int r = j;
	int u = i;
	int d = i;
	//decrease left

	while (l >= 0){
		bool ok = true;
		for (int rr = u; rr <= d; rr++){
			if (mat[rr][l] != a && mat[rr][l] != '?'){
				ok = false;
				break;
			}
		}
		if (ok){
			l--;
		}
		else break;
	}
	if(l!=j)l++;
	//decrease up

	while (u >= 0){
		bool ok = true;
		for (int cc = l; cc <= r; cc++){
			if (mat[u][cc] != a && mat[u][cc] != '?'){
				ok = false;
				break;
			}
		}
		if (ok){
			u--;
		}
		else break;
	}
	if(u!=i)u++;
	//increase right

	while (r<col){
		bool ok = true;
		for (int rr = u; rr <= d; rr++){
			if (mat[rr][r] != a && mat[rr][r] != '?'){
				ok = false;
				break;
			}
		}
		if (ok){
			r++;
		}
		else break;
	}
	if(r!=j)r--;
	//increase down
	//cout << "now is " <<a<<" "<< l << " " << r << " " << " " << u << " " << d << endl;
	while (d <row){
		bool ok = true;
		for (int cc = l; cc <= r; cc++){
			//cout << mat[d][cc] << endl;
			if (mat[d][cc] != a && mat[d][cc] != '?'){
				ok = false;
				break;
			}
		}
		if (ok){
			d++;
	
		}
		else {
			break;
		}
	}
	if (d != i) d--;
	solved[a - 'A'] = true;
	for (int i = u; i <= d; i++){
		for (int j = l; j <= r; j++){
			mat[i][j] = a;
		}
	}
	/*for (int i = 0; i < row; i++){
		for (int j = 0; j < col; j++){
			cout << mat[i][j];
		}
		cout << endl;
	}*/
}


int main(){
	ios_base::sync_with_stdio(false);
	int t;
	ifstream fin;
	fin.open("A-large.in");
	fin >> t;
	ofstream fout;
	fout.open("1-large.out");
	for (int ti = 1; ti <= t; ti++){
		fout << "Case #" << ti << ": "<<endl;
		int r, c;
		fin >> r >> c;
		int cnt = 0;
		fill(solved, solved + 26, false);
		for (int i = 0; i < r; i++){
			fin >> mat[i];
		}
		for (int i = 0; i < r; i++){
			for (int j = 0; j < c; j++){
				if ((mat[i][j] != '?')&&solved[mat[i][j] - 'A'] == false){
					solve(i, j, r, c, mat[i][j]);
				}
			}
		}
		for (int i = 0; i < r; i++){
			for (int j = 0; j < c; j++){
				fout << mat[i][j];
			}
			fout << endl;
		}


		
	}
	system("Pause");
	return 0;
}
