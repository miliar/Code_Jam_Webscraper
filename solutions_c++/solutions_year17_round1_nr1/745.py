/*
ID: jeffrey31
LANG: C++
TASK: A
*/
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <cstdlib>
using namespace std;
#define mp make_pair
#define pb push_back
#define ff first
#define ss second
typedef long long ll;
const int N = 30;
int tc;
int r,c;
string a[N];

int main() {
  freopen("A.in","r",stdin);
  freopen("A.out","w",stdout);
  cin >> tc;
  for(int t = 1; t <= tc; t++) {
    cout << "Case #" << t << ":\n";
    cin >> r >> c;
    string s;
    for(int i = 0; i < r; i++) {
      cin >> s;
      a[i] = s;
      char cur = '?';
      
      for(int j = 0; j < c; j++) {
        if (s[j] != '?') {
          cur = s[j];
          break;
        }
      }
      for(int j = 0; j < c; j++) {
        if (s[j] != '?') {
          cur = s[j];
        } else {
          a[i][j] = cur;
        }
      }
      //cout << a[i] << endl;
    }
    for(int i = 0; i < c; i++) {
      char cur = '?';
      
      for(int j = 0; j < r; j++) {
        if (a[j][i] != '?') {
          cur = a[j][i];
          break;
        }
      }
      for(int j = 0; j < r; j++) {
        if (a[j][i] != '?') {
          cur = a[j][i];
        } else {
          a[j][i] = cur;
        }
      }
      
    }
    for(int i = 0; i < r; i++) {
      cout << a[i] << "\n";
    }
  }
  return 0;
}