#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;

#define Loop(i, a, b) for (int i = (a); i < (b); ++i)

bool letter(char ch) {return (ch >= 'A') && (ch <= 'Z');}

void make_par(int v, int h, vector<string> &cake) {
  if(letter(cake[v][h])) {
    cake[v][h] -= 30;
    char ch = cake[v][h];
    int sth = h, fih = h, stv = v, fiv = v;
    while(stv > 0 && cake[stv-1][h] == '?') { --stv; cake[stv][h] = ch;}
    //while(fiv < cake.size() - 1 && cake[fiv+1][h] == '?') { ++fiv; cake[fiv][h] = ch;}
    bool ok = true;
    while(sth > 0) {
      --sth;
      Loop(i, stv, fiv + 1) if (cake[i][sth] != '?') ok = false;
      if (ok) Loop(i, stv, fiv + 1) cake[i][sth] = ch;
    }
    ok = true;
    while(fih < cake[0].size() - 1) {
      ++fih;
      Loop(i, stv, fiv + 1) if (cake[i][fih] != '?') {ok = false; break;}
      if (ok) Loop(i, stv, fiv + 1) cake[i][fih] = ch;
    }
  }
}

int main() {

#ifdef LocalHost
  //freopen("input", "rt", stdin);
  //freopen("A-small-attempt2.in", "rt", stdin);
  freopen("A-large.in", "rt", stdin);
  freopen("outputA.txt", "w", stdout);
#endif

  int line_num;
  cin >> line_num;
  for (int line = 1; line <= line_num; ++line) {
    int n, m;
    cin >> n >> m;

    vector<string> cake(n);
    Loop(i, 0, n) { cin >> cake[i]; }

    Loop(i, 0, n) { Loop(j, 0, m) make_par(i, j, cake);}
    Loop(i, 0, n) {Loop(j, 0, m) cake[i][j] += 30;}
    Loop(i, 0, n) {if (!letter(cake[i][0])) cake[i] = cake[i - 1]; }
    printf("Case #%d:\n", line);
    Loop (i, 0, n) cout << cake[i] << "\n";
  }

  return 0;
}
