#include <bits/stdc++.h>
using namespace std;

inline odd(int x) {
  return(x&1);
}

int main() {
  long long t,n,k,curr,ans1,ans2;
  multiset<long long, greater<long long> > rooms;
  cin >> t;
  for(int i = 1; i <= t; i++) {
    rooms.clear();
    cin >> n >> k;
    rooms.insert(n);
    for(long long j = 1; j < k; j++) {
      curr = *(rooms.begin());
      rooms.erase(rooms.begin());
      if(curr == 1) {
        continue;
      } else if(odd(curr)) {
        rooms.insert(curr/2);
        rooms.insert(curr/2);
      } else {
        rooms.insert(curr/2);
        rooms.insert((curr/2)-1);
      }
    }
    curr = *(rooms.begin());
    ans1 = curr/2;
    if(odd(curr)) {
      ans2 = ans1;
    } else {
      ans2 = ans1 - 1;
    }
    cout << "Case #" << i << ": " << ans1 << " " << ans2 << endl;
  }

  return 0;
}