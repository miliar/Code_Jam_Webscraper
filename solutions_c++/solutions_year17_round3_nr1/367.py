#include <bits/stdc++.h>

using namespace std;

const double pi = 3.1415926535897932384626433832795028841971;

long long score(priority_queue<pair<long long,int>> heap, int k) {
   long long ans = 0;
   for(int i = 0; i < k; ++i) {
      if(!heap.empty()) {
         long long x = heap.top().first;
         ans += x;
         heap.pop();
      }
   }
   return ans;
}

int main() {
   int T;
   cin >> T;
   for(int testcase = 1; testcase <= T; testcase++) {
      int N, K;
      long long best = 0;
      cin >> N >> K;
      vector<pair<long long,long long>> tab(N);
      for(int i = 0; i < N; ++i)
         cin >> tab[i].first >> tab[i].second;
      sort(tab.begin(),tab.end());
      priority_queue<pair<long long,int>> heap;
      for(int i = 0; i < N; ++i) {
         long long x = tab[i].first, y = tab[i].second;
         best = max(best, (x*x) + (2* ((x*y) + score(heap,K-1)))); 
         heap.push({x*y,i});
      }
      double ans = ((double) best) * pi;
      cout << setprecision(30) << "Case #" << testcase << ": " << ans << endl;
   }
}
