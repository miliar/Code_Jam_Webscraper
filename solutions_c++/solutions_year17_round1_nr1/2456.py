#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<iostream>
#include<queue>
#include<vector>
#include<set>
#include<stack>
#include<map>
#include<ctime>
#include<bitset>
#define LL long  long
#define db double
#define EPS 1e-8
#define inf 1e9
#define pi 3.1415926535898
using namespace std;

char mapp[30][30];
int width[36];
int skip[36];
void run(){
    int R,C;
	scanf("%d%d", &R, &C);
	for (int i = 0; i < R; i++){
		scanf("%s", mapp[i]);
	}

	for (int i = 0; i < 26; i++) {
		width[i] = 1;
		skip[i] = false;
	}

	for (int i = 0; i < R; i++)
		for (int j = 0; j < C; j++){
			if (mapp[i][j] != '?'){
				for (int k = j - 1; k >= 0; k--){
					if (mapp[i][k] == '?'){
						mapp[i][k] = mapp[i][j];
						width[mapp[i][j] - 'A']++;
					} else break;
				}
				for (int k = j + 1; k < C; k++){
					if (mapp[i][k] == '?'){
						mapp[i][k] = mapp[i][j];
						width[mapp[i][j] - 'A']++;
					} else break;
				}
			}
		}
	for (int i = 0; i < R; i++)
		for (int j = 0; j < C; j++){
			if (mapp[i][j] != '?' && skip[mapp[i][j] - 'A'] == false){
				skip[mapp[i][j] - 'A'] = true;
				for (int k = i - 1; k >= 0; k--){
					if (mapp[k][j] == '?'){
						bool can_go = true;
						for (int l = j; l < j + width[mapp[i][j] - 'A']; l++)
							if (mapp[k][l] != '?') {
								can_go = false;
								break;
							}
						if (can_go)
							for (int l = j; l < j + width[mapp[i][j] - 'A']; l++)
								mapp[k][l] = mapp[i][j];
						else break;
					} else break;
				}
				for (int k = i + 1; k < R; k++){
					if (mapp[k][j] == '?'){
						bool can_go = true;
						for (int l = j; l < j + width[mapp[i][j] - 'A']; l++)
							if (mapp[k][l] != '?') {
								can_go = false;
								break;
							}
						if (can_go)
							for (int l = j; l < j + width[mapp[i][j] - 'A']; l++)
								mapp[k][l] = mapp[i][j];
						else break;
					} else break;
				}
			}
		}
	puts("");
	for (int i = 0; i < R; i++)
		printf("%s\n", mapp[i]);
}

int main(){
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int T;
    scanf("%d", &T);
	for (int i=1; i<=T; i++){
		printf("Case #%d:", i);
		run();
	}
    return 0;
}
