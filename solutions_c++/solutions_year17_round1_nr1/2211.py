#include <bits/stdc++.h>
using namespace std;
int T, R, C;
char ch[30][30];
int s[50];
int num;
int hash[200];
int a[30][30][30];
int ff[30];
int dx[4] = {1, 0, 0, -1};
int dy[4] = {0, -1, 1, 0};
int left, right, up, down, k;

int main(){
	freopen("T1large.in", "r", stdin);
	freopen("T1large.out", "w", stdout);
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> T;
	for(int l = 1; l <= T; l++){
			
      cin >> R >> C;
      for(int i = 1; i <= R; i++){
        for(int j = 1; j <= C; j++){
          cin >> ch[i][j];
        }
      }
      cout << "Case #" << l << ':' << endl;
      int flag;
      for(int i = 1; i <= R; i++){
        for(int j = 1; j <= C; j ++){
          	if(ch[i][j] == '?'){
              	flag = 0;
                for(int k = j - 1; k > 0; k--){
                    if(ch[i][k] != '?'){
                        ch[i][j] = ch[i][k];
                        flag = 1;
                        break;
                    }
                }
              	for(int k = j + 1; k <= C; k++){
              		if(flag != 0) break;
                  if(ch[i][k] != '?'){
                    ch[i][j] = ch[i][k];
                      flag = 1;
                      break;
                  }
                }
            }
        }
      }
    	for(int i = 1; i <= R; i++){
        for(int j = 1; j <= C; j++){
            if(ch[i][j] == '?'){
              flag = 0;
              for(k = i - 1; k > 0; k--){
                if(ch[k][j] != '?'){
                  flag = 1;
                  break;
                }
              }
              for(int G = 1; G <= C; G++){
                ch[i][G] = ch[k][G];
              }
              for(k = i + 1; k <= R; k++){
              	if(flag != 0) break;
                if(ch[k][j] != '?'){
                  flag = -1;
                  break;
                }
              }
              if(flag == -1){
                for(int G = 1; G <= C; G++)
                  ch[i][G] = ch[k][G];
              }
            }
        }
      }
        for(int i = 1; i <= R; i++){
            for(int j = 1; j <= C; j++){
                cout << ch[i][j];
            }
            cout << endl;
        }
	}


return 0;
}

