#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cstring>
#include <cassert>
#include <utility>
#include <iomanip>

using namespace std;

int tn;
long long n, k;
priority_queue <long long> q;
map <long long, long long> mp;

int main() {
  //assert(freopen("input.txt","r",stdin));
  //assert(freopen("output.txt","w",stdout));

  scanf("%d\n", &tn);

  for (int test = 1; test <= tn; test++) {
    cin >> n >> k;

    while (!q.empty()) {
      q.pop();
    }

    mp.clear();
    q.push(n);
    mp[n] = 1;

    long long sum = 0;
    while (!q.empty()) {
      long long cur = q.top();
      q.pop();
      sum += mp[cur];
      long long l = (cur - 1) / 2, r = cur / 2;
      //cout << cur << " " << sum << " " << mp[cur] << " " << l << " " << r << endl;

      if (sum >= k) {
        printf("Case #%d: ", test);
        cout << max(l, r) << " " << min(l, r) << endl;
        break;
      }

      if (mp[l] == 0) {
        q.push(l);
      }
      mp[l] += mp[cur]; 
      if (mp[r] == 0) {
        q.push(r);
      }
      mp[r] += mp[cur];
    }
  }

  return 0;
}