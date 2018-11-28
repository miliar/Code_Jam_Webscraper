#include<iostream>
#include<algorithm>
#include<sstream>
#include<string>
#include<vector>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<fstream>
#include<cassert>
#include<numeric>
#include<set>
#include<map>
#include<queue>
#include<list>
#include<deque>
using namespace std;

int n;
long long dist[100];
double speed[100];
long long graph1[100][100];
double graph2[100][100];

int main() {
  int cases;
  cin >> cases;
  for(int cc = 0; cc < cases; ++cc) {
    int q;
    cin >> n >> q;
    for(int i = 0; i < n; ++i) {
      cin >> dist[i] >> speed[i];
    }
    for(int i = 0; i < n; ++i) 
      for(int j = 0; j < n; ++j) {
        long long dist;
        cin >> dist;
        if(i == j) dist = 0;
        if(dist == -1) dist = numeric_limits<long long>::max() / 3;
        graph1[i][j] = dist;
        graph2[i][j] = 1e20;        
      }
    for(int k = 0; k < n; ++k) 
      for(int i = 0; i < n; ++i) 
        for(int j = 0; j < n; ++j) {
          graph1[i][j] = min(graph1[i][k] + graph1[k][j], graph1[i][j]);
        }
    for(int a = 0; a < n; ++a) 
      for(int b = 0; b < n; ++b) {
        if(graph1[a][b] <= dist[a]) {
          graph2[a][b] = graph1[a][b] / speed[a];
        }
      }
    for(int k = 0; k < n; ++k) 
      for(int i = 0; i < n; ++i) 
        for(int j = 0; j < n; ++j) {
          graph2[i][j] = min(graph2[i][k] + graph2[k][j], graph2[i][j]);
        }
    printf("Case #%d:", cc+1);
    for(int i = 0; i < q; ++i) {
      int a, b;
      cin >> a >> b;
      --a; --b;
      printf(" %.10lf", graph2[a][b]);
    }
    printf("\n");
  }
}
