// INCLUDE LIST
#include <cstdio>
#include <bitset>
#include <iostream>
#include <queue>
#include <stack>
#include <string>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>
#include <list>
#include <vector>
#include <cstdlib>
#include <cctype>
#include <cmath>
using namespace std;

// DEFINE LIST
#define REP(_I, _J, _K) for(_I = (_J) ; _I < (_K) ; _I++)
#define input(_A)       freopen(_A, "r", stdin);
#define output(_A)      freopen(_A, "w", stdout);
#define INPUT           input("in.txt");
#define OUTPUT          output("out.txt");
#define CASE_LEFT(_A)   fprintf(stderr, "Cases left: %d\n", _A);
#define hold            {fflush(stdin); getchar();}
#define reset(_A, _B)   memset((_A), (_B), sizeof (_A));
#define debug           printf("<<TEST>>\n");
#define eps             1e-11
#define f_cmp(_A, _B)   (fabs((_A) - (_B)) < eps)
#define phi             acos(-1)
#define pb              push_back
#define value(_A)       cout << "Variabel -> " << #_A << " -> " << _A << endl;
#define st              first
#define nd              second

// TYPEDEF LIST
typedef pair<int, int>  ii;
typedef vector<int>     vi;
typedef vector<ii>      vii;
typedef long long       LL;

// VAR LIST
int MAX =               1000000;
int MIN =               -1000000;
int INF =               1000000000;
int x4[4] =             {0, 1, 0, -1};
int y4[4] =             {1, 0, -1, 0};
int x8[8] =             {0, 1, 1,  1,  0, -1, -1, -1};
int y8[8] =             {1, 1, 0, -1, -1, -1,  0,  1};
int i, j, k;

int arr[100010];

// MAIN CODE
int main () {
  input("C-small-1-attempt0.in");
  output("out.txt");
  int t, N, k, kasus = 0;
  cin >> t;
  while (t--) {
    cin >> N >> k;
    reset(arr, 0);
    for (int i = 1; i <= k; i++) {
      int minim = 1000000000;
      int maksi = -1;
      int ans = 0;
      for (int j = 1; j <= N; j++) {
        if (arr[j] == 1)
          continue;
        int kiri = 0;
        int kanan = 0;
        int now = j;
        while (now >= 1 && arr[now] == 0) {
          now--;
          kiri++;
        }
        kiri--;
        
        now = j;
        while (now <= N && arr[now] == 0) {
          now++;
          kanan++;
        }
        kanan--;
        
        if (min(kiri, kanan) > maksi) {
          maksi = min(kiri, kanan);
          minim = max(kiri, kanan);
          ans = j;
        } else if (min(kiri, kanan) == maksi && max(kiri, kanan) > minim) {
          minim = max(kiri, kanan);
          ans = j;
        }
      }
      arr[ans] = 1;
      if (i == k) {
        cout << "Case #" << ++kasus << ": " << minim << " " << maksi << endl;
      }
    }
  }
  return 0;
}

