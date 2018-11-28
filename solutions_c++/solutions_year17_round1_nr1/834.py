#include<bits/stdc++.h>
using namespace std;

const int N = 30;

int T, n, m, last;
char s[N][N];
bool X[N], Y[N];

void solve(int x, int y){
    int x0=0, y0=-1;
    for(int i=x-1; i>=0; i--){
		if(X[i]){
			x0 = i+1;
			break;
		}
    }
    for(int i=y-1; i>=0; i--){
		for(int j=x0; j<=x; j++){
			if(s[j][i] != '?'){
				y0 = i;
				break;
			}
		}
		if(y0 != -1){
			break;
		}
    }
    y0++;
    char g = s[x][y];
    if(x == last){
		x = n - 1;
    }
    for(int i=x0; i<=x; i++){
		for(int j=y0; j<=y; j++){
			s[i][j] = g;
		}
    }
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	for(int t=1; t<=T; t++){
		scanf("%d %d", &n, &m);
		memset(X, 0, sizeof(X));
		memset(Y, 0, sizeof(Y));
		for(int i=0; i<n; i++){
			scanf("%s", s[i]);
			for(int j=0; j<m; j++){
				if(s[i][j] != '?'){
					last = i;
					Y[j] = 1;
					X[i] = 1;
				}
			}
		}
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
				if(s[i][j] != '?'){
					solve(i, j);
				}
            }
        }
        printf("Case #%d:\n", t);
        for(int i=0; i<n; i++){
			for(int j=0; j<m; j++){
				if(s[i][j] == '?'){
					s[i][j] = s[i][j-1];
				}
				printf("%c", s[i][j]);
			}
			puts("");
        }
	}
	return 0;
}
