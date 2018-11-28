#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std;
#define lli long long int
#define li long int
void solve(int tc) {
     priority_queue<lli, deque<lli>, less<lli> > pq;
     lli n, k, n1, ans1, ans2;
     cin >> n >>  k;
     if(n == k) {
          ans1 = 0;
          ans2 = 0;
     }
     else {
          pq.push(n);
          while(k != 0) {
               n = pq.top();
               pq.pop();
               //cout << "top = " << n << "\n";
               n1 = n >> 1;
               if(n & 1) {
                    //printf("X1\n");
                    ans1 = n1;
                    ans2 = n1;
                    pq.push(n1);
                    //cout <<"Before" <<  pq.size();
                    pq.push(n1);
                    //cout <<" After" << pq.size();
               }
               else {
                    //printf("X2\n");
                    ans1 = n1;
                    ans2 = n1 - 1;
                    pq.push(n1);
                    pq.push(n1 - 1);
               }
               k--;
          }
     }
     pq = priority_queue<lli, deque<lli>, less<lli> >();
     printf("Case #%d: ", tc);
     cout << ans1 << " " << ans2 << "\n";
}
int main() {
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; i++) {
    	    solve(i);
    }
    return 0;
}