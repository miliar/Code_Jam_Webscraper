#include <cstdio>
#include <algorithm>
#include <map>
#include <vector>
#include <string>
#include <cstdlib>
using namespace std;

void add(vector<string> &v, int N, string S) {
    for(int i = 0;i < (int) S.size();++i) S[i] = toupper(S[i]);
    while(N--) v.push_back(S);
}

int main() {
  int T; scanf("%d", &T);
  for(int tc = 1;tc <= T;++tc) {
    printf("Case #%d: ", tc);
    int n;
    int R, o, Y, g, B, v;

    scanf("%d", &n);
    scanf("%d%d%d%d%d%d", &R, &o, &Y, &g, &B, &v);

    bool ok = 1;
    if(B < 2*o || R < 2*g || Y < 2*v) {
      ok = 0;
      puts("IMPOSSIBLE");
    } else {
      int r = R, y = Y, b = B; // ASLI

      B -= o;
      R -= g;
      Y -= v;

      int a[3] = {R, Y, B};
      sort(a,a+3);
      // printf("%d %d %d | a\n", a[0], a[1], a[2]);
      if(a[2] > a[1]+a[0]) {
        puts("IMPOSSIBLE");
      } else {
        int m = a[2]-a[1], k = a[0]-m;

        // sebanyak a[1], a[2]-a[1]-(a[0]?)
        // sebanyak m, a[2]-a[0]

        // maka, sebanyak k pertama: a[2]-a[1]-a[0]
        // sebanyak a[1]-k, a[2]-a[1]
        // sebanyak m, a[2]-a[0]

        pair<int,int> p[3] = {make_pair(R, 0), make_pair(Y, 1), make_pair(B, 2)};
        vector<string> S[3];
        S[0].clear(); add(S[0], r-2*g, "r"); add(S[0], g, "rgr");
        S[1].clear(); add(S[1], y-2*v, "y"); add(S[1], v, "yvy");
        S[2].clear(); add(S[2], b-2*o, "b"); add(S[2], o, "bob");

        // for(int i = 0;i < 3;++i) for(int j = 0;j < S[i].size();++j) { printf("%s ",S[i][j].c_str()); printf("| \n"); }
        // printf("m = %d, k = %d\n", m, k);

        sort(p, p+3);
        int i = 0;
        for(;i < k;++i) printf("%s%s%s", S[p[2].second][i].c_str(), S[p[1].second][i].c_str(), S[p[0].second][i].c_str());
        int j = i;
        for(int tmp = 0, tj = j;tmp < a[1]-k;++tmp,++tj,++i)
          printf("%s%s", S[p[2].second][i].c_str(), S[p[1].second][tj].c_str());
        for(int tmp = 0, tj = j;tmp < m;++tmp, ++tj, ++i)
          printf("%s%s", S[p[2].second][i].c_str(), S[p[0].second][tj].c_str());
        printf("\n");
      }
    }
  }
}
