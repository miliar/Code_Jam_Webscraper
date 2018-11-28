#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const int MX = 1010;
int T, C = 1;

const int RED = 1<<0, YELLOW = 1<<1, BLUE = 1<<2;
const int ORANGE = RED | YELLOW, GREEN = YELLOW | BLUE, VIOLET = RED | BLUE;
int N, R, O, Y, G, B, V;

char get_char(int v) {
  if(v == RED)    return 'R';
  if(v == GREEN)  return 'G';
  if(v == YELLOW) return 'Y';
  if(v == ORANGE) return 'O';
  if(v == BLUE)   return 'B';
  if(v == VIOLET) return 'V';
}

int get_code(char& v) {
  if(v == 'R') return RED;
  if(v == 'G') return GREEN;
  if(v == 'Y') return YELLOW;
  if(v == 'O') return ORANGE;
  if(v == 'B') return BLUE;
  if(v == 'V') return VIOLET;
}

bool valid(string& ans) {
  if(N != (int) ans.size()) return 0;
  for(int i = 0; i < ans.size(); i++) {
    if(get_code(ans[i]) & get_code(ans[(i - 1 + N) % N])) return 0;
  }
  return 1;
}

int main() {
	freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  scanf("%d", &T);
  while(T--) {
    printf("Case #%d: ", C++);
    scanf("%d %d %d %d %d %d %d", &N, &R, &O, &Y, &G, &B, &V);
    vector<pair<int, int> > V({{R, RED}, {Y, YELLOW}, {B, BLUE}});
    sort(V.begin(), V.end());

    string ans = "";
    for(int i = 0; i < V[0].first; i++) {
      for(int j = 2; j >= 0; --j)
        ans.push_back(get_char(V[j].second));
    }

    for(int i = 0; i < V[1].first - V[0].first; i++) {
      for(int j = 2; j >= 1; --j)
        ans.push_back(get_char(V[j].second)); 
    }
    V[2].first -= V[1].first;
    for(int j = 0; j < V[2].first; j++) {
      for(int i = 1; i < int(ans.size()); i++) {
        if(get_code(ans[i]) & V[2].second) continue;
        if(get_code(ans[i - 1]) & V[2].second) continue;
        ans = ans.substr(0, i) + string(1, get_char(V[2].second)) + ans.substr(i);
        break;
      }
    }
    if(get_code(ans[0]) & get_code(ans.back())) {
      char c = ans.back(); ans.pop_back();
      for(int i = 1; i < int(ans.size()); i++) {
        if(get_code(ans[i]) & get_code(c)) continue;
        if(get_code(ans[i - 1]) & get_code(c)) continue;
        ans = ans.substr(0, i) + string(1, c) + ans.substr(i);
        break;
      }
    }
    if(valid(ans)) puts(ans.c_str());
    else puts("IMPOSSIBLE");
  }
}
