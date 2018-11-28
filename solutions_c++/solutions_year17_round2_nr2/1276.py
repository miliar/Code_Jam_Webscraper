#include<cstdio>
#include<cstdint>
#include<cassert>
#include<cmath>
#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<unordered_map>
#include<unordered_set>
#include<string>
#include<algorithm>
#include<utility>
#include<functional>

using namespace std;

bool check(int V, int Y, int R, int B, char cV, char cY) {
  if (V > 0 && V == Y) {
    if (R > 0 || B > 0) {
      cout << "IMPOSSIBLE"; 
    } else {
      for (int i = 0; i < V; i++) {
        cout << cV << cY;
      }
    }
    cout << endl;
    return true;
  } else {
    return false;
  }
}

void emit(char c, int &G, int &O, int &V) {
  if (c == 'R' && G > 0 && G--) cout << "RGR";
  else if (c == 'B' && O > 0 && O--) cout << "BOB";
  else if (c == 'Y' && V > 0 && V--) cout << "YVY";
  else cout << c;
}

void single(int i, bool run) {
  // Input
  int N, R, O, Y, G, B, V;
  cin >> N >> R >> O >> Y >> G >> B >> V;
  if (! run) return;
  cout << "Case #" << i << ": ";
  // Solve
  int RR = R - G;
  int BB = B - O;
  int YY = Y - V;
  if (RR < 0 || BB < 0 || YY < 0) {
    cout << "IMPOSSIBLE" << endl; 
    return;
  }
  if (check(V, Y, R, B, 'V', 'Y')) return;
  if (check(G, R, Y, B, 'G', 'R')) return;
  if (check(O, B, R, Y, 'O', 'B')) return;
  std::vector<pair<int, char> > vals;
  vals.push_back({RR, 'R'});
  vals.push_back({BB, 'B'});
  vals.push_back({YY, 'Y'});
  sort(vals.begin(), vals.end());
  int n = vals[0].first;
  int m = vals[1].first;
  int k = vals[2].first;
  char cN = vals[0].second;
  char cM = vals[1].second;
  char cK = vals[2].second;
  //int k = max(RR, max(BB, YY));
  //int n = min(RR, min(BB, YY));
  //int m = RR + BB + YY - k - n;
  int a = k > m ? k - m : 0;
  int kp = k - 2 * a;
  int mp = m - 1 * a;
  int np = n - 1 * a;
  //cerr << k << " " << m << " " << n << endl;
  //cerr << kp << " " << mp << " " << np << endl;
  if (mp < 0 || np < 0 || kp < 0) {
    cout << "IMPOSSIBLE" << endl; 
    return;
  }
  assert(mp == kp);
  int b = kp - np;
  int kpp = kp - 1 * b;
  assert(kpp == np);
  assert(a > 0 || b > 0 || kpp > 0);
  //char cM = RR == m ? 'R' : BB == m ? 'B' : 'Y';
  //char cN = BB == n ? 'B' : YY == n ? 'Y' : 'R';
  //char cK = YY == k ? 'Y' : RR == k ? 'R' : 'B';
  for (int i = 0; i < a; i++) {
    emit(cK, G, O, V); 
    emit(cM, G, O, V);
    emit(cK, G, O, V);
    emit(cN, G, O, V);
  }
  for (int i = 0; i < b; i++) {
    emit(cK, G, O, V); 
    emit(cM, G, O, V);
  }
  for (int i = 0; i < kpp; i++) {
    emit(cK, G, O, V); 
    emit(cM, G, O, V);
    emit(cN, G, O, V);
  }
  cout << endl;
}

int main(int argc, char ** argv) {
  FILE * ret;
  ret = freopen(argv[1], "r", stdin);
  assert(ret != nullptr);
  int testcases;
  cin >> testcases;
  int first_testcase = 1;
  int last_testcase = testcases;
  if (argc >= 3) first_testcase = atoi(argv[2]);
  if (argc >= 4) last_testcase = atoi(argv[3]);
  for (int i = 1; i <= testcases; i++) {
    single(i, i >= first_testcase && i <= last_testcase);
  }
  return EXIT_SUCCESS;
}
