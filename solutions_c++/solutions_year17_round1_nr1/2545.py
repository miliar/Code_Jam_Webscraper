#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;
typedef long long ll;

bool state[25][25];

int main(){
  int T;  cin >> T;
  for(int ii = 1; ii <= T; ii++){
    int R, C; cin >> R >> C;
    char a[25][25];
    for(int i = 0; i < R; i++){
      for(int j = 0; j < C; j++) {
        cin >> a[i][j];
        state[i][j] = false;
      }
    }
    for(int i = 0; i < R; i++){
      for(int j = 0; j < C; j++){
        if(a[i][j] != '?' && !state[i][j]){
          state[i][j] = true;
          int si = i-1, ei = i+1;
          int sj = j-1, ej = j+1;
          while(sj >= 0 && a[i][sj] == '?'){
            state[i][sj] = true;
            a[i][sj--] = a[i][j];
          }
          while(ej < C && a[i][ej] == '?'){
            state[i][ej] = true;
            a[i][ej++] = a[i][j];
          }
          //cout << a[i][j] << " " << si << " " << ei << endl;
          while(si >= 0){
            int res = 0;
            for(int k = sj+1; k < ej; k++){
              if(a[si][k] != '?' || state[si][k]){res = 1;  k = ej;}
            }
            if(res == 0){
              for(int k = sj+1; k < ej; k++){
                state[si][k] = true;
                a[si][k] = a[i][j];
              }
              si--;
            }
            else break;
          }
          while(ei < R){
            int res = 0;
            for(int k = sj+1; k < ej; k++){
              if(a[ei][k] != '?' || state[ei][k]){res = 1;  k = ej;}
            }
            if(res == 0){
              for(int k = sj+1; k < ej; k++){
                state[ei][k] = true;
                a[ei][k] = a[i][j];
              }
              ei++;
            }
            else break;
          }
        }
      }
    }
    cout << "Case #" << ii << ":" << endl;
    for(int i = 0; i < R; i++){
      for(int j = 0; j < C; j++)  cout << a[i][j];
      cout << endl;
    }
  }

  return 0;
}
