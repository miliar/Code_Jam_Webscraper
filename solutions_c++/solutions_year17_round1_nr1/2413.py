#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
using namespace std;

const int N = 30;
char a[N][N];
int r, c;
int x[2], y[2];
bool chk[N];

bool get(char ch,int x,int y){
	if (a[x][y] == '?')return true;
	if (a[x][y] == ch)return true;
	return false;
}

void solve(){
	for (int i = 0; i < N; ++i)
		chk[i] = false;
	for (int i = 0; i < r; ++i){
		for (int j = 0; j < c; ++j){
			char ch = a[i][j];
			if (a[i][j] != '?' && !chk[ch-'A']){
				x[0] = x[1] = i;
				y[0] = y[1] = j;
				chk[ch - 'A'] = true;
				while (y[0]){
					bool ok = true;
					for (int k = x[0]; k <= x[1]; ++k){
						if (!get(ch, k, y[0] - 1)){
							ok = false;
						}
					}
					if (!ok)break;
					--y[0];
					for (int k = x[0]; k <= x[1]; ++k){
						a[k][y[0]] = ch;
					}
				}
				while (y[1] + 1 < c){
					bool ok = true;
					for (int k = x[0]; k <= x[1]; ++k){
						if (!get(ch, k, y[1] + 1)){
							ok = false;
						}
					}
					if (!ok)break;
					++y[1];
					for (int k = x[0]; k <= x[1]; ++k){
						a[k][y[1]] = ch;
					}
				}
				while (x[0]){
				
					bool ok = true;
					for (int k = y[0]; k <= y[1]; ++k){
						if (!get(ch, x[0] - 1, k)){
							ok = false;
						}
					}
					if (!ok)break;
					--x[0];
					for (int k = y[0]; k <= y[1]; ++k){
						a[x[0]][k] = ch;
					}
				}
				while (x[1] + 1 < r){
					bool ok = true;
					for (int k = y[0]; k <= y[1]; ++k){
						if (!get(ch, x[1] +1, k)){
							ok = false;
						}
					}
					if (!ok)break;
					++x[1];
					for (int k = y[0]; k <= y[1]; ++k){
						a[x[1]][k] = ch;
					}
				}
				
			}
		}
	}
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int i=1;i<=t;++i){
		scanf("%d%d", &r, &c);
		for (int i = 0; i < r; ++i){
			scanf("%s", a[i]);
		}
		solve();
		printf("Case #%d:\n", i);
		for (int i = 0; i < r; ++i){
			printf("%s\n", a[i]);
		}
	}
	return 0;
}