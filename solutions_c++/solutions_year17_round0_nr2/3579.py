#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <deque>
#include <cmath>
#include <map>
#include <set>
#define MOD 1000000007
using namespace std;

long long n;
vector<long long> ans;

bool isTidy(long long n) {
   vector<int> d;
   while (n > 0) {
      d.push_back(n%10);
      n /= 10;
   }
   reverse(d.begin(), d.end());

   int f = 0;
   for (int i = 0; i < (int)d.size(); i++) {
      if (f > d[i]) {
         return false;
      } else {
         f = d[i];
      }
   }
   return true;
}

void findlast(long long n) {
   long long tmp = n;

   if (isTidy(n)) {
      ans.push_back(n);
      return;
   } else {
      ans.push_back(9);
      findlast(n/10-1);
   }
}

void solve() {
   cin >> n;
   ans.clear();

   findlast(n);
   reverse(ans.begin(), ans.end());
   for (long long ll : ans) {
      if (ll > 0) cout << ll;
   }
   cout << endl;
}

int main() {
   int t; int tc = 1;
   cin >> t;
   while (t--) {
      cout << "Case #" << tc++ << ": ";
      solve();
   }
}
