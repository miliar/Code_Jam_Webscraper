#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

void nuru (char str[26][26], int j,int k, int jj, int kk,char c) {
  // cout << j << k << jj << kk << endl;
  for (int jjj = j; jjj <= jj; jjj++) {
    for (int kkk = k; kkk <= kk; kkk++) {
      str[jjj][kkk] = c;
    }
  }
}


int main()
{
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    int R,C;
    cin >> R >> C;
    char str[26][26];
    for (int j = 0; j < R; j++) {
      cin >> str[j];
    } 
    
    // make rect
    for (int j = 0; j < R; j++) {
      for (int k = 0; k < C; k++) {
        if (str[j][k] == '?') continue;
        for (int jj = j; jj < R; jj++) {
          for (int kk = k+1; kk < C; kk++) {
            if (str[j][k] == str[jj][kk]) {
              nuru(str,j,k,jj,kk, str[j][k]);
            }
          }
        } 
      }
    }

    bool running = true;
    while (running) {
      running = false;
      for (int j = 0; j < R; j++) {
        for (int k = 0; k < C; k++) {
          if (str[j][k] == '?') {
            running = true;
            if (k != 0 && str[j][k-1] != '?') {
              int min_j,max_j;
              for (min_j = 0; min_j < j; min_j++) {
                if (str[j][k-1] == str[min_j][k-1])
                  break;
              }
              for (max_j = R - 1; max_j > j; max_j--) {
                if (str[j][k-1] == str[max_j][k-1])
                  break;
              }
              for (int jj = min_j; jj <= max_j; jj++) {
    //             cout << min_j << j << max_j<< endl;
    //             cout << jj << k << str[j][k]<< endl;
    // for (int j = 0; j < R; j++) {
    //   cout << str[j] << endl;
    // }
                if (str[jj][k] != '?' && str[jj][k] != str[j][k-1]) goto eli0;
              }
              nuru (str, min_j,k-1, max_j,k, str[j][k-1]);
              continue;
            }
          eli0:
            if (j != 0  && str[j-1][k] != '?') {
              int min_k,max_k;
              for (min_k = 0; min_k < k; min_k++) {
                if (str[j-1][k] == str[j-1][min_k])
                  break;
              }
              for (max_k = C - 1; max_k > k; max_k--) {
                if (str[j-1][k] == str[j-1][max_k])
                  break;
              }
              for (int kk = min_k; kk <= max_k; kk++) {
                if (str[j][kk] != '?' && str[j][kk] != str[j-1][k]) goto eli1;
              }
              nuru (str, j-1,min_k,j, max_k, str[j-1][k]);
              running = true;
              continue;
            }
          eli1:
            if (k != C - 1  && str[j][k+1] != '?') {
              int min_j,max_j;
              for (min_j = 0; min_j < j; min_j++) {
                if (str[j][k+1] == str[min_j][k+1])
                  break;
              }
              for (max_j = R - 1; max_j > j; max_j--) {
                if (str[j][k+1] == str[max_j][k+1])
                  break;
              }
              for (int jj = min_j; jj <= max_j; jj++) {
                if (str[jj][k] != '?' && str[jj][k] != str[j][k+1]) goto eli2;
              }
              nuru (str, min_j,k, max_j,k+1, str[j][k+1]);
              running = true;
              continue;
            }
          eli2:
            if (j != R - 1 && str[j+1][k] != '?') {
              int min_k,max_k;
              for (min_k = 0; min_k < k; min_k++) {
                if (str[j+1][k] == str[j+1][min_k])
                  break;
              }
              for (max_k = C - 1; max_k > k; max_k--) {
                if (str[j+1][k] == str[j+1][max_k])
                  break;
              }
              for (int kk = min_k; kk <= max_k; kk++) {
                if (str[j][kk] != '?' && str[j][kk] != str[j+1][k]) goto eli3;
              }
              nuru (str, j,min_k,j+1, max_k, str[j+1][k]);
              running = true;
              continue;
            }
          eli3:
            int a;
          }
        }
      }
    }
    cout << "Case #" << i << ":" << endl;
    for (int j = 0; j < R; j++) {
      cout << str[j] << endl;
    }
  }
  return 0;
}
