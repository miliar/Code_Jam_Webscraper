#include<bits/stdc++.h>
#include<unordered_set>
#include<unordered_map>
using namespace std;
int cnt_t;
void outt(){
	cnt_t++;
	printf("Case #%d: ", cnt_t);
}

int r;
int c;

vector<string> v;
bool flag[26];
int x_min[26];
int x_max[26];
int y_min[26];
int y_max[26];
int main(){
	int t;
	scanf("%d", &t);
	while (t--){
		for (int i = 0; i < 26; i++){
			x_min[i] = y_min[i] = INT_MAX;
			x_max[i] = y_max[i] = -1;
		}
		cin >> r >> c;
		v.clear();
		for (int i = 0; i < r; i++){
			string s;
			cin >> s;
			v.push_back(s);
			for (int j = 0; j < c; j++){
				if (v[i][j] == '?')continue;
				int id = v[i][j] - 'A';
				x_min[id] = min(x_min[id], i);
				x_max[id] = max(x_max[id], i);
				y_min[id] = min(y_min[id], j);
				y_max[id] = max(y_max[id], j);
			}
		}
		for (int i = 0; i < 26; i++){
			if (x_min[i] != INT_MAX){
				for (int j = x_min[i]; j <= x_max[i]; j++){
					for (int kk = y_min[i]; kk <= y_max[i]; kk++){
						v[j][kk] = i + 'A';
					}
				}
			}
		}
		for (int i = 0; i < v.size(); i++){
			bool ok = false;
			for (int j = 0; j < c; j++){
				if (v[i][j] != '?'){
					ok = true;
					break;
				}
			}
			flag[i] = ok;
		}
		for (int i = 0; i < v.size(); i++){
			for (int j = 0; j < c; j++){
				if (v[i][j] != '?'){
					for (int jj = j - 1; jj >= 0; jj--){
						if (v[i][jj] == '?'){
							v[i][jj] = v[i][j];
						}
						else{
							break;
						}
					}
					for (int jj = j + 1; jj < c; jj++){
						if (v[i][jj] == '?'){
							v[i][jj] = v[i][j];
						}
						else{
							break;
						}
					}
				}
			}
		}
		for (int i = 0; i < v.size(); i++){
			if (flag[i]){
				for (int j = i - 1; j >= 0; j--){
					if (flag[j] == false){
						flag[j] = true;
						v[j] = v[i];
					}
					else{
						break;
					}
				}
				for (int j = i + 1; j < r; j++){
					if (flag[j] == false){
						flag[j] = true;
						v[j] = v[i];
					}
					else{
						break;
					}
				}
			}
		}
		outt();
		puts("");
		for (int i = 0; i < v.size(); i++){
			cout << v[i] << endl;
		}
	}
	return 0;
}