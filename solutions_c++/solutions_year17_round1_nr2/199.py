#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

vector<int> r;

bool comp(int i, int w1, int j, int w2) {
  return w1*r[j] < w2*r[i];
}

int minPortions(int i, int w) {
  return (10*w-1)/(11*r[i])+1;
}

int maxPortions(int i, int w) {
  return (10*w)/(9*r[i]);
}

int main() {
  int numCases;
  cin >> numCases;
  for (int testCase=1; testCase<=numCases; ++testCase) {
    cout << "Case #" << testCase << ": ";
    int n,p;
    cin >> n >> p;
    r.resize(n);
    for(int i=0;i<n;++i)
      cin >> r[i];
    vector<vector<int> > q(n, vector<int>(p)), q2;
    for(int i=0;i<n;++i)
      for(int j=0;j<p;++j)
        cin >> q[i][j];
    q2 = q;
    for(int i=0;i<n;++i)
      sort(q2[i].begin(), q2[i].end());
    vector<int> qi(n,0);
    int ret=0;
    while(true) {
      bool end=false;
      vector<int> cand(n);
      for(int i=0;i<n;++i)
        if(qi[i]==p)
          end=true;
        else
          cand[i]=q2[i][qi[i]];
      if(end)
        break;
      int portions = maxPortions(0,cand[0]);
      for(int i=1;i<n;++i)
        portions = min(portions, maxPortions(i, cand[i]));
      bool success = true;
      for(int i=0;i<n;++i)
        if (portions<minPortions(i, cand[i]))
          success = false;
      if(success) {
        ret++;
        for(int i=0;i<n;++i)
          qi[i]++;
      } else {
        for(int i=0;i<n;++i)
          if (maxPortions(i, cand[i]) == portions)
            qi[i]++;
      }
    }
    cout << ret << endl;
  }
}