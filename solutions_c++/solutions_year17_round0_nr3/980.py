#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <cstdint>
using namespace std;

#define min(a,b) ((a) < (b) ? (a) : (b))
#define max(a,b) ((a) > (b) ? (a) : (b))

typedef pair<uint64_t, uint64_t> uint2;

void solve() {
  uint64_t N, K;
  cin >> N >> K;

  queue<uint2> q;

  q.push(uint2(N,1));
  uint64_t count = 0;
  
  do {
    uint64_t l = q.front().first;
    uint64_t n = q.front().second;
    q.pop();
    while (!q.empty() && q.front().first == l) {
      n += q.front().second;
      q.pop();
    }

    uint64_t l1, l2;
    if (l % 2 == 1)
      l1 = l2 = (l-1)/2;
    else {
      l2 = (l-1)/2;
      l1 = l2 + 1;
    }
    count += n;
    if (K <= count) {
      cout << l1 << " " << l2 << endl;
      return;
    } else {
      if (l1 == l2)
	q.push(uint2(l1,2*n));
      else {
	q.push(uint2(l1,n));
	q.push(uint2(l2,n));
      }
    }
  } while (true);
}
       
int main(){
  int T;
  cin >> T; 
  string s; 

  for (int i = 0; i < T; i++) {
    cout << "Case #" << i+1 << ": ";
    solve();
  }
  return 0;
}


