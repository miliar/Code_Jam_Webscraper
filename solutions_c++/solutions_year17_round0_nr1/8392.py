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

int tc, n;
string s;

int main() {
  freopen("A.in","r",stdin);
  freopen("A.out","w",stdout);
  cin >> tc;
  for(int i = 1; i <= tc; i++) {
    printf("Case #%d: ", i);
    cin >> s >> n;
    int cnt = 0;
    int len = s.length();
    int j = 0;
    for (; j <= len - n; j++) {
      if (s[j] == '-') {
        cnt++;
        for (int k = j; k < j + n; k++) {
          if (s[k] == '+') {
            s[k] = '-';
          } else {
            s[k] = '+';
          }
        }
      }
    }
    for(; j < len; j++) {
      if (s[j] == '-') {
        printf("IMPOSSIBLE\n");
        break;
      }
    }
    if (j == len)
      printf("%d\n", cnt);
  }
  return 0;
}