#include <bits/stdc++.h>
using namespace std;
#define ll long long


struct Rec{
  int xl, yl, xu, yu;
};


int main() {
  int T;
  cin >> T;

  for(int t = 0; t < T; t++) {
      int R, C;
      cin >> R >> C;
      vector<string> original(R);;

      vector<char> appeared;
      vector< pair<int, int> > nd;
      for(int r = 0; r < R; r++) {
        string s;
        cin >> s;
        original[r] = s;
        for(int c = 0; c < C; c++) {

          if(s[c] == '?')
            nd.push_back(make_pair(r, c));
          else
            appeared.push_back(s[c]);
        }
      }

      while(1) {
        vector<string> cp(R);
        for(int r = 0; r < R; r++) {
          cp[r] = original[r];
        }
        for(auto loc: nd) {
          cp[loc.first][loc.second] = appeared[rand() % appeared.size()];
        }
        map<char, Rec> m;

        for(int i = 0; i < R; i++) {
          string s = cp[i];
          for(int k = 0; k < C; k++) {
            if(m.find(s[k]) == m.end()) {
              Rec r;
              r.xl = r.xu = i;
              r.yl = r.yu = k;
              m[s[k]] = r;
            }else {
              Rec r = m[s[k]];
              r.xl = min(r.xl, i);
              r.xu = max(r.xu, i);
              r.yl = min(r.yl, k);
              r.yu = max(r.yu, k);
              m[s[k]] = r;
            }
          }
        }

        int cnt[R][C];

        for(int r = 0; r < R; r++) {
          for(int c = 0; c < C; c++) {
            cnt[r][c] = 0;
          }
        }

        for(auto i: m) {
          Rec r = i.second;
          for(int x = r.xl; x <= r.xu; x++) {
            for(int y = r.yl; y <= r.yu; y++) {
              cnt[x][y]++;
              if(cnt[x][y] > 1)
                goto next_big_loop;
            }
          }
        }
        cout << "Case #" << t + 1 << ":" << endl;
        for(auto s: cp) {
          cout << s << endl;
        }
        break;

        next_big_loop:
          0;

      }
  }
}
