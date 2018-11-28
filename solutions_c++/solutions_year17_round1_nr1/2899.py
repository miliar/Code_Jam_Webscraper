#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
#define endl '\n'
int main(){
		cin.tie(0);
	ios::sync_with_stdio(false);
	int t;
	cin >> t;

	for(int z = 1; z <= t; z++){
		char grid[27][27];
		int r=0,c=0;
		cin >> r >> c;
		vector<pair<int,int> > start;
		for(int i = 0; i < r; i++){
			string s;
			cin >> s;
			for(int j = 0; j < c; j++){
				grid[i][j] = s[j];
				if(s[j] != '?'){
					start.push_back({i,j});
				}
			}
		}
		for(int o = 0; o < start.size(); o++){
			pair<int,int> current = start[o];
			int down = 1,up = 1, left = 1, right = 1;
			bool right_continue = true;
			bool up_continue = true;
			bool left_continue = true;
			char paint_with = grid[current.first][current.second];
			//down
			while(current.first+down < r && grid[current.first+down][current.second] == '?'){
				grid[current.first+down][current.second] = paint_with;
				down++;
			}
			while(right_continue && right+current.second <= c){
				for(int i = 0; i < down; i++){
					if(grid[current.first+i][current.second+right] != '?'){
						right_continue = false;
						break;
					}
				}
				if(right_continue)right++;
			}
			for(int i = 0; i < down; i++){
				for(int j = 0; j < right; j++){
					grid[current.first+i][current.second+j] = paint_with;
				}
			}

			while(up_continue && current.first-up >= 0){
				for(int i = 0; i < right; i++){
					if(grid[current.first-up][current.second+i] != '?'){
						up_continue = false;
						break;
					}
				}
				if(up_continue)up++;
			}
			for(int i = 0; i < right; i++){
				for(int j = 0; j < up; j++){
					grid[current.first-j][current.second+i] = paint_with;
				}
			}
			while(left_continue && current.second-left >= 0){
				for(int i = -up+1; i < down; i++){
					if(grid[current.first+i][current.second-left] != '?'){
						left_continue = false;
						break;
					}
				}
				if(left_continue)left++;
			}
			for(int i = -up+1; i < down; i++){
				for(int j = 0; j < left; j++){
					grid[current.first+i][current.second-j] = paint_with;
				}
			}
		}
		cout << "Case #" << z << ":" << endl;
		for(int i = 0; i < r; i++){
			for(int j = 0; j < c; j++){
				cout << grid[i][j];
			}
			cout << endl;
		}
	}
	return 0;
}