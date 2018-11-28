#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<string>
#include<sstream>
#include<cmath>
#include<numeric>
#include<map>
using namespace std;
bool comp(pair< long long int, pair<long long int, long long  int> > lhs, pair< long long int, pair<long long int, long long int> > rhs) {
  if (lhs.first != rhs.first)return lhs.first < rhs.first;
  if (lhs.second.first != rhs.second.first) return lhs.second.first < rhs.second.first;
  return lhs.second.second < rhs.second.second;
}

int k, n;
vector< pair<long long int, pair<long long int, long long int> > > p;

int main(void) {

  int t;
  cin >> t;
  // cout << M_PI << endl;
  for(int loop=0; loop<t; loop++){
    cin >> n >> k;
    p.resize(n);
    for(int i=0; i<n; i++){
      cin >> p[i].second.first >> p[i].second.second;
      p[i].first = p[i].second.first * p[i].second.second;
    }
    sort(p.begin(), p.end());

    long long int ans = 0;
    for(int i=0; i<n; i++){
      long long int sum = 0;
      sum += p[i].second.first * p[i].second.first + ( 2 * p[i].first );
      int cnt = 0;
      for(int j=0; j<n; j++){
        if( cnt == k-1 ) break;
        int pos = n - j - 1;
        if( i == pos ) continue;
        cnt++;
        sum += 2 * p[pos].first;
      }
      ans = max(ans, sum);
    }
    double dans = ans * M_PI;

    printf("Case #%d: %.10lf\n", loop+1, dans);


  }

  return 0;
}
