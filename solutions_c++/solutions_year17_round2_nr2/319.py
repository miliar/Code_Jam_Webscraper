#include <iostream>
#include <algorithm>
#include <map>
#include <string>
#include <set>
#include <vector>
#include <list>

#define TRACE(x) cerr << #x << " = " << x << endl
#define _ << " _ " << 

using namespace std;
string S = "ROYGBV";
const string NO = "IMPOSSIBLE";
int n;
int c[6];

string greedy() {
  string sol(n, '.');
  for (int i=0, j=0, k=0; i<n; i++) {
    while (c[j] == 0)
      j++;
    int cnt = 0;
    while (sol[k] != '.' || sol[(k+n-1)%n] == S[j] || sol[(k+1)%n] == S[j]) {
      k = (k+1)%n;
      cnt++;
      if (cnt > n)
        return NO;
    }
    sol[k] = S[j];
    c[j]--;
//    TRACE(sol);
  }
  return sol;
}

int main() {
  int t;
  cin >> t;
  for (int tt=0; tt<t; tt++) {
    S = "ROYGBV";
    cin >> n;
    for (int i=0; i<6; i++)
      cin >> c[i];
    for (int i=0; i<6; i++)
      for (int j=i+1; j<6; j++)
        if (c[j] > c[i])
          swap(c[i], c[j]), swap(S[i], S[j]);
          
    cout << "Case #" << tt+1 << ": " << greedy() << endl;
  }
  return 0;
}
