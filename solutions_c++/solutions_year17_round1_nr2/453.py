#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <queue>
#include <set>
#include <map>

using namespace std;

#define ll long long
#define pii pair<int,int>

int N,P,T;

ifstream fin("B.in");
ofstream fout("B.out");

priority_queue<int> vals[55];
ll reqs[55];

int main() {
  fin >> T;
  for (int tt = 1; tt <= T; tt++) {
    cout << "Working on Case #" << tt << "\n";
    fin >> N >> P;
    for (int i = 0; i < N; i++) fin >> reqs[i];
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < P; j++) {
        int a;
        fin >> a;
        vals[i].push(-a);
      }
    }
    bool flag = true;
    int ans=0;
    while (flag) {
      int minind = -1; 
      int minval = 0;
      int minserv = -1;
      int maxserv = 9999999;
      for (int i = 0; i < N; i++) {
        int v = -vals[i].top();
        int h = (10*v)/(reqs[i]*9);
        int l = (10*v+reqs[i]*11-1)/(reqs[i]*11);
        //cout << reqs[i] << " " << v << " " << l << " " << h << "\n";
        if (minind == -1 || h < minval) {
          minval = h;
          minind = i;
        }
        minserv = max(minserv,l);
        maxserv = min(maxserv,h);
      }
      if (minserv <= maxserv) {
        ans++;
        for (int i = 0; i < N; i++) vals[i].pop();
      }
      else {
        vals[minind].pop();
      }
      for (int i = 0; i < N; i++) {
        if (vals[i].empty()) flag = false;
      }
    }
    for (int i = 0; i < N; i++) {
      while (!vals[i].empty()) vals[i].pop();
    }
    fout << "Case #" << tt << ": " << ans << "\n";
  }
  return 0;
}