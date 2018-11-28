#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <cstring>


using namespace std;


int main(){
   int n_case;
   cin >> n_case;
   map<long long, long long> M;
   for( int loop = 0 ; loop < n_case ; loop++ ){
      long long N, K;
      cin >> N >>K;
      M.clear();
      M[N] = 1;
      priority_queue<long long> pq = priority_queue<long long>();
      pq.push(N);
      long long L=N;
      long long R=N;
      while( K > 0 ){
         long long next = pq.top();
         pq.pop();
         long long num = M[next];
         long long left = (next-1)/2;
         long long right = next/2;
         if(M[left]==0) pq.push(left);
         if(left != right && M[right]==0) pq.push(right);
         //cout << next << "-> " << left << "&"<< right <<"..." << M[next]<<endl;
         L=left;R=right;
         M[left] += num;
         M[right] += num;
         M.erase(next);
         K-=num;
      }
      cout << "Case #" << loop+1 << ": " <<R << " " << L<< endl;
   }
   return 0;
}
