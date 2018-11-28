#include <iostream>
#include <string>
#include <queue>
#include <fstream>
#include <stdio.h>
#include <math.h>
#include <cstring>
#include <vector>
#include <algorithm>
#include <climits>
#include <sstream>
#include <map>
#include <set>
#include <stack>
#include <iomanip>
using namespace std;

typedef long long ll;
typedef vector<int> vi;

int grid[50][50];
int up[50], down[50], l[50], r[50];
int n,m; 

bool can_expand_up(int idx){
	if(up[idx] == 0) return false;
	int i = up[idx] - 1;
	for(int j = l[idx]; j<= r[idx]; j ++){
		if(grid[i][j] != -1)
			return false;
	}
	return true;
}
void expand_up(int idx){
	up[idx] --;
	int i = up[idx];
	for(int j = l[idx]; j <= r[idx]; j ++){
		grid[i][j] = idx;
	}
}

bool can_expand_down(int idx){
	if(down[idx] == n - 1) return false;
	int i = down[idx] + 1;
	for(int j = l[idx]; j<= r[idx]; j ++){
		if(grid[i][j] != -1)
			return false;
	}
	return true;
}
void expand_down(int idx){
	down[idx] ++;
	int i = down[idx];
	for(int j = l[idx]; j <= r[idx]; j ++){
		grid[i][j] = idx;
	}
}


bool can_expand_l(int idx){
	if(l[idx] == 0) return false;
	int j = l[idx] - 1;
	for(int i = up[idx]; i <= down[idx]; i ++){
		if(grid[i][j] != -1)
			return false;
	}
	return true;
}
void expand_l(int idx){
	l[idx] --;
	int j = l[idx];
	for(int i = up[idx]; i <= down[idx]; i ++){
		grid[i][j] = idx;
	}
}

bool can_expand_r(int idx){
	if(r[idx] == m - 1) return false;
	int j = r[idx] + 1;
	for(int i = up[idx]; i<= down[idx]; i ++){
		if(grid[i][j] != -1)
			return false;
	}
	return true;
}
void expand_r(int idx){
	r[idx] ++;
	int j = r[idx];
	for(int i = up[idx]; i <= down[idx]; i ++){
		grid[i][j] = idx;
	}
}
void fill(int idx){
	for(int i = up[idx]; i <= down[idx]; i ++){
		for(int j = l[idx]; j<= r[idx]; j ++)
			grid[i][j] = idx;
	}
}
int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "r+", stdout);
#endif

	int t; cin >> t;
	int case_num = 1;
	while(t--){
		cin >> n >> m;
		memset(up, 0x3F, sizeof up);
		memset(down, -1, sizeof down);
		memset(l, 0x3F, sizeof l);
		memset(r, -1, sizeof r);
		memset(grid, -1, sizeof grid);
		bool exists[50];
		memset(exists, false, sizeof exists);
		for(int i=  0; i < n; i ++){
			for(int j = 0; j < m; j ++){
				char c; cin >> c;
				grid[i][j] = (c == '?') ? -1 : c - 'A';
				if(grid[i][j] != -1){
					up[grid[i][j]] = min(up[grid[i][j]], i);
					down[grid[i][j]] = max(down[grid[i][j]], i);
					l[grid[i][j]] = min(l[grid[i][j]], j);
					r[grid[i][j]] = max(r[grid[i][j]], j);
					exists[grid[i][j]] = true;
				}
			}
		}
		for(int i = 0; i < 50; i ++){
			if(exists[i]) fill(i);
		}
		for(int i = 0; i < 50; i ++){
			if(exists[i]){
				while(can_expand_r(i)) expand_r(i);
			}
		}
		for(int i = 0; i < 50; i ++){
			if(exists[i]){
				while(can_expand_l(i)) expand_l(i);
			}
		}
		for(int i = 0; i < 50; i ++){
			if(exists[i]){
				while(can_expand_down(i)) expand_down(i);
			}
		}
		for(int i = 0; i < 50; i ++){
			if(exists[i]){
				while(can_expand_up(i)) expand_up(i);
			}
		}
		cout << "Case #" << case_num ++ << ":"<< endl;
		for(int i = 0; i < n; i ++){
			for(int j = 0; j < m; j ++){
				cout << char(grid[i][j] + 'A');
			}
			cout << endl;
		}
	}
	return 0;
}
