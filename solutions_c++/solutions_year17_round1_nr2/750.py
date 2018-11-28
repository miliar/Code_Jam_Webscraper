/*
ID: jeffrey31
LANG: C++
TASK: B
*/
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <map>
#include <set>
using namespace std;
#define mp make_pair
#define pb push_back
#define ff first
#define ss second
typedef long long ll;
typedef pair<int, int> pii;

const int N = 55, M = 1000010;
int tc;
int n, p, a[N][N], r[N], q[N], l[N][N], u[N][N];


int main() {
  freopen("B.in","r",stdin);
  freopen("B.out","w",stdout);
  scanf("%d\n", &tc);
  
  for(int t = 1; t <= tc; t++) {
    int ans = 0;
    printf("Case #%d: ", t);
    scanf("%d %d", &n, &p);
    for(int i = 0; i < n; i++) {
      scanf("%d", r + i);
    }
    
    map<int, vector<int> > v[n];
    set<int> x;
    for(int i = 0; i < n; i++) {
      for(int j = 0; j < p; j++) {
        scanf("%d", &a[i][j]);
        u[i][j] = floor(a[i][j] * 1.0 / (r[i] * .9));
        l[i][j] = ceil(a[i][j] * 1.0 / (r[i] * 1.1));
        if (u[i][j] < l[i][j]) {
          continue;
        }/*
        if(v[i][l[i][j]] == NULL) {
          vector<int> x;
          v[i][l[i][j]] = x;
        }
        */
        v[i][l[i][j]].pb(u[i][j]);
        x.insert(l[i][j]);

      }
    }
    
    priority_queue<int> pq[n];

    for(typeof(x.begin()) it = x.begin(); it != x.end(); it++) {
      int i = *it;
      int sm = 1 << 25;
      for(int j = 0; j < n; j++) {
        while(!pq[j].empty() && -pq[j].top() < i)
          pq[j].pop();
        for(int k = 0; k < v[j][i].size(); k++) {
          pq[j].push(-v[j][i][k]);
        }
        sm = min(sm, (int)pq[j].size());
      }
      if (sm > 0 && i != 0) {
        ans += sm;
        for(int j = 0; j < n; j++) {
          if (pq[j].size() < sm) printf("wtf %d %d\n", pq[j].size(), sm);
          for(int k = 0; k < sm; k++) {
            pq[j].pop();
          }
        }
      }
    }
    
    /*
    for(int i = 0; i < n; i++) {
      for(int j = 0; j < p; j++) {
        printf("(%d %d)", l[i][j], u[i][j]);
      }
      printf("\n");
    }
    */
    
    printf("%d\n", ans);
  }
    

  
  return 0;
}