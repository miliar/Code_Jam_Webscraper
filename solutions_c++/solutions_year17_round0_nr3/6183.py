#include <bits/stdc++.h>
using namespace std;

struct dat {
   int b, m, e;
   dat(int b_, int e_) : b(b_), e(e_) {
      m = (b + e) / 2;
   }
   bool operator<(dat d) const {
      // cerr << "cmp((" << b << ", " << e << "), (" << d.b << ", " << d.e << "))\n";
      if(e-b != d.e-d.b) return e-b < d.e - d.b;
      // cerr << e-b << " == " << d.e-d.b << "\n";
      return m > d.m;
   }
};

int N, K;

void work() {
   priority_queue<dat> pq; pq.push(dat(0, N+1));
   while(K > 1) {
      auto u = pq.top(); pq.pop();
      if(u.b+1 < u.m) {
         // cerr << "(" << u.b << ", " << u.m << ") pushed\n";
         pq.push(dat(u.b, u.m));
      }
      if(u.m+1 < u.e) {
         // cerr << "(" << u.m << " " << u.e << ") pushed\n";
         pq.push(dat(u.m, u.e));
      }
      K--;
   }
   auto p = pq.top();
   int l = p.m - p.b - 1, r = p.e - p.m - 1;
   // cerr << p.b << " " << p.e << "\n";
   printf("%d %d\n", max(l,r), min(l,r));
}

int main() {
   int T; scanf("%d", &T);
   for(int cs = 1; cs <= T; cs++) {
      scanf("%d%d", &N, &K);
      printf("Case #%d: ", cs);
      work();
   }
}
