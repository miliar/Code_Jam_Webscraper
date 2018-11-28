#include <bits/stdc++.h>

using namespace std;

void solve()
{
  int H, W;
  string S[25];

  cin >> H >> W;
  for(int i = 0; i < H; i++) {
    cin >> S[i];
  }


  int appear[25] = {};
  for(int i = 0; i < H; i++) {
    for(int j = 0; j < W; j++) {
      if(S[i][j] != '?') appear[i] = true;
    }
  }

  for(int i = 0; i < H; i++) {
    for(int j = 0; j < W; j++) {
      if(S[i][j] == '?') {
        if(appear[i]) {
          for(int k = j - 1; k >= 0; k--) {
            if(S[i][k] != '?') {
              S[i][j] = S[i][k];
              break;
            }
          }
          for(int k = j + 1; k < W; k++) {
            if(S[i][k] != '?') {
              S[i][j] = S[i][k];
              break;
            }
          }
        }
      }
    }
  }

  for(int i = 0; i < H; i++) {
    if(S[i][0] == '?') {
      if(i > 0 && S[i - 1][0] != '?') {
        for(int k = 0; k < W; k++) {
          S[i][k] = S[i - 1][k];
        }
      }
    }
  }


  for(int i = H - 1; i >= 0; i--) {
    if(S[i][0] == '?') {
      if(i != H - 1 && S[i + 1][0] != '?') {
        for(int k = 0; k < W; k++) {
          S[i][k] = S[i + 1][k];
        }
      }
    }
  }

  for(int i = 0; i < H; i++) {
    cout << S[i] << endl;
  }
}

int main()
{
  int T;
  cin >> T;
  for(int i = 1; i <= T; i++) {
    cout << "Case #" << i << ":" << endl;
    solve();
  }
}
