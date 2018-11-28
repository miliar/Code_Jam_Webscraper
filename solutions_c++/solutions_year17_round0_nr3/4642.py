#include<stdio.h>
#include<iostream>
#include<queue>
#include<map>
using namespace std;

//int j, m, mf;
//long long aux[1000];

int main() {
   int t, x, i;
   long long n, k, a, l, r, y, z, fa;
   priority_queue<long long> pq;
   map<long long, long long> f;
   cin >> t;
   for (x = 1; x <= t; x++) {
      cin >> n >> k;
      pq.push(n);
      f[n] = 1;
      i = 0;
      
      //m = mf = 1;
      
      while (i < k) {
         /*
         for (j = 0; j <= n; j++) {
            if (f[j] != 0) {
               printf("%d %d, ", j, f[j]);
            }
         }
         printf("\n");
         */
         a = pq.top();
         fa = f[a];
         f[a] = 0;
         pq.pop();
         l = (a-1)/2;
         r = (a-1)/2 + (a-1)%2;
         if (f[l] == 0) {
            pq.push(l);
         }
         f[l] = f[l] + fa;
         if (f[r] == 0) {
            pq.push(r);
         }
         f[r] = f[r] + fa;
         i = i + fa;
         
         //m = m < pq.size() ? pq.size() : m;
         //mf = mf < fa ? fa : mf;
      }
      z = l;
      y = r;
      while (!pq.empty()) {
         f[pq.top()] = 0;
         pq.pop();
      }
      cout << "Case #" << x << ": " << y << " " << z << endl;
      
      //cout << m << " " << mf << endl;
   }
   return 0;
}
