#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <fstream>
#include <cmath>
#include <cstdio>
using namespace std;
#define forn(a, b) for (int i = a; i < b; ++i)
#define fore(i, a, b) for (int i = a; i < b; ++i)
#define fork(i, a, b) for (i = char(a); i < char(b); ++i)
#define mp(a, b) make_pair(a, b)
#define pb(a) push_back(a)
#define all(a) a.begin(), a.end()
#define sz(a) a.size()
#define x first
#define y second
#define LINF 9000000000000000000
#define INF 2000000000
typedef long long ll;
char num[20];
int n;
ofstream out;
void print() {
  for (int i = 0; i < n; ++i)
    out << char(char(num[i]) + '0');
  out << endl;
}
void run(int size, int p) {
  if (p == size) {
    n = size;
    print();
  } else if (p == 0) {
    char chr;
    fork (chr, 1, 10) {
      num[p] = chr;
      run(size, p + 1);
    }
  } else
    fork (num[p], num[p - 1], 10)
      run(size, p + 1);
}
void solve() {
  out.open("nums.txt", ios::app);
  forn (1, 19)
    run(i, 0);

}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    solve();

    return 0;
}
