#define _CRT_SECURE_NO_WARNINGS
#include <Windows.h>

#include <map>
#include <string>
#include <stdio.h>
#include <vector>
#include <sstream>
#include <stack>
#include <bitset>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <iostream>
#include <algorithm>
#include <limits.h>
#include <float.h>


using namespace std;


void rowFill(vector<vector<char>>& charMp, int i, int j){
	if (charMp[i][j] == '?')  return;

	for (int k = j + 1; k < charMp[i].size(); k++){
		if (charMp[i][k] == '?')
			charMp[i][k] = charMp[i][j];
		else break;
	}
	for (int k = j - 1; k >= 0; k--){
		if (charMp[i][k] == '?')
			charMp[i][k] = charMp[i][j];
		else break;
	}
}

void copyTo(vector<vector<char>>& charMp, int from, int to){
	charMp[to] = charMp[from];
}

void fillEmpty(vector<vector<char>>& charMp){
	vector<bool> isFill(charMp.size(), false);
	for (int i = 0; i < charMp.size(); i++){
		if (charMp[i][0] != '?') isFill[i] = true;
	}

	for (int i = 0; i < charMp.size(); i++){
		if (isFill[i]){
			for (int j = i + 1; j < charMp.size(); j++){
				if (!isFill[j])
					copyTo(charMp, i, j);
				else break;
			}
			for (int j = i - 1; j >= 0; j--){
				if (!isFill[j])
					copyTo(charMp, i, j);
				else break;
			}
		}

	}

}


int main(){
	freopen("A-large.in", "r", stdin);
	freopen("result", "w", stdout);
	
	int t;
	cin >> t;

	for (int k = 1; k <= t; k++){
		int r, c;

		cin >> r >> c;
		vector<vector<char>> charMp(r, vector<char>(c, '?'));
		for (int i = 0; i < r; i++){
			for (int j = 0; j < c; j++){
				cin >> charMp[i][j];
			}
		}

		for (int i = 0; i < r; i++){
			for (int j = 0; j < c; j++){
				rowFill(charMp, i, j);
			}
		}


		fillEmpty(charMp);


		printf("Case #%d:\n", k);
		for (int i = 0; i < r; i++){
			for (int j = 0; j < c; j++){
				cout << charMp[i][j];
			}
			cout << endl;
		}
	}


	
}
