#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <string>
#include <queue>
#include <deque>
#include <map>

using namespace std;

void solve(){
	int m, n;
	scanf("%d %d", &m, &n);
	char a[m][n];
	for(int i=0;i<m;i++) scanf("%s", a[i]);

	int f[256][4];
	for(int i='A'; i<='Z'; i++)
		for(int j=0;j<4;j++) f[i][j] = -1;

	for(int i=0;i<m;i++)
		for(int j=0;j<n;j++) 
			if(a[i][j] != '?'){
				if(f[a[i][j]][0] == -1 || i<f[a[i][j]][0]) f[a[i][j]][0] = i;
				if(f[a[i][j]][1] == -1 || j<f[a[i][j]][1]) f[a[i][j]][1] = j;
				if(f[a[i][j]][2] == -1 || i>f[a[i][j]][2]) f[a[i][j]][2] = i;
				if(f[a[i][j]][3] == -1 || j>f[a[i][j]][3]) f[a[i][j]][3] = j;
			}

	for(int i='A'; i<='Z'; i++) if(f[i][0] != -1)
		for(int x = f[i][0]; x<=f[i][2]; x++)
			for(int y = f[i][1]; y<=f[i][3]; y++) a[x][y] = i;

	for(int i='A'; i<='Z'; i++) if(f[i][0] != -1){
		bool b = true;
		while(b){
			b = false;
			if(f[i][0] > 0){
				bool t = true;
				for(int j = f[i][1]; j<= f[i][3]; j++) if(a[f[i][0] -1][ j ] != '?'){
					t = false;
					break;
				}
				if(t){
					b = true;
					f[i][0]--;
					for(int j = f[i][1]; j<= f[i][3]; j++) a[f[i][0]][ j ] = i;
				}
			}
			if(f[i][1] > 0){
				bool t = true;
				for(int j = f[i][0]; j<= f[i][2]; j++) if(a[j][f[i][1] -1] != '?'){
					t = false;
					break;
				}
				if(t){
					b = true;
					f[i][1]--;
					for(int j = f[i][0]; j<= f[i][2]; j++) a[j][f[i][1]] = i;
				}
			}
			if(f[i][2] < m-1){
				bool t = true;
				for(int j = f[i][1]; j<= f[i][3]; j++) if(a[f[i][2]+1][j] != '?'){
					t = false;
					break;
				}
				if(t){
					b = true;
					f[i][2]++;
					for(int j = f[i][1]; j<= f[i][3]; j++) a[f[i][2]][j] = i;
				}
			}
			if(f[i][3] < n-1){
				bool t = true;
				for(int j = f[i][0]; j<= f[i][2]; j++) if(a[j][f[i][3]+1] != '?'){
					t = false;
					break;
				}
				if(t){
					b = true;
					f[i][3]++;
					for(int j = f[i][0]; j<= f[i][2]; j++) a[j][f[i][3]] = i;
				}
			}
		}
	}

	for(int i=0;i<m;i++){
		for(int j=0;j<n;j++) printf("%c", a[i][j]);
		printf("\n");
	}
}

int main(){
	int cs, lp;
	scanf("%d", &cs);
	for(int lp = 1; lp <=cs; lp++){
		printf("Case #%d:\n", lp);
		solve();
	}
	return 0;
}
