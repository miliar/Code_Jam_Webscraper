#include <iostream>
#include <algorithm>
#include <map>
#include <string>
#include <set>
#include <vector>
#include <list>
#include <iomanip>
#include <queue>

#define TRACE(x) cerr << #x << " = " << x << endl
#define _ << " _ " << 

using namespace std;

const int MAX = 100;

typedef pair<double, int> qelem;

int n;
int q;
int e[MAX];
int s[MAX];
long long d[MAX][MAX];

double solve(int a, int b) {
  priority_queue<qelem, vector<qelem>, greater<qelem>> q;
  vector<int> done(n, 0);
  q.push({0, a});
  while (!q.empty()) {
    double x = q.top().first;
    int i = q.top().second;
    q.pop();
    //TRACE(x _ i);
    if (done[i])
      continue ;
    done[i] = 1;
    if (i == b)
      return x;
    for (int j=0; j<n; j++)
      if (!done[j])
        if (d[i][j] != -1 && d[i][j] <= e[i]) {
          double y = x + d[i][j]/double(s[i]);
          q.push({y, j});
        }
  }
  return -1;
}

int main() {
  int t;
  cin >> t;
  for (int tt=0; tt<t; tt++) {
    cin >> n >> q;
    for (int i=0; i<n; i++)
      cin >> e[i] >> s[i];
    
    for (int i=0; i<n; i++)
      for (int j=0; j<n; j++)
        cin >> d[i][j];
    
    for (int i=0; i<n; i++)
      for (int j=0; j<n; j++)
        if (d[j][i] != -1)
          for (int k=0; k<n; k++)
            if (d[i][k] != -1) {
              long long temp = d[j][i]+d[i][k];
              if (d[j][k] == -1 || d[j][k] > temp)
                d[j][k] = temp;
            }
    
    cout << "Case #" << tt+1 << ":";
    for (int i=0; i<q; i++) {
      int a, b;
      cin >> a >> b;
      cout << " " << setprecision(10) << solve(a-1, b-1);
    }
    cout << endl;
  }
  return 0;
}
