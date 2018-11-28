#include <bits/stdc++.h>

using namespace std;

int main() {
  int tests;
  int ngroups;
  int p;
  cin >> tests;
  for(int t = 1; t <= tests; t++) {
    cin >> ngroups >> p;
    int* buckets = new int[4];
    buckets[0] = buckets[1] = buckets[2] = buckets[3] = 0;
    int fresh = 0;
    for(int i = 0; i < ngroups; i++) {
      int temp;
      cin >> temp;
      if(temp % p == 0) {
        fresh++;
      }
      else {
        buckets[temp % p]++;
      }
    }
    if(p == 2) {
      fresh += buckets[1] / 2;
      buckets[1] =  (buckets[1] % 2);
    }
    else if (p == 3) {
      int wow = min(buckets[1], buckets[2]);
      fresh += wow;
      buckets[1] -= wow;
      buckets[2] -= wow;
      fresh += (buckets[1]) / 3;
      fresh += (buckets[2]) / 3;
      buckets[1] = buckets[1] % 3;
      buckets[2] = buckets[2] % 3;

    }
    else if (p == 4) {
      fresh += buckets[2] / 2;
      buckets[2] -= buckets[2] / 2;
      int wow = min(buckets[1], buckets[3]);
      fresh += wow;
      buckets[1] -= wow;
      buckets[3] -= wow;
      fresh += (buckets[1] ) / 4;
      buckets[1] = (buckets[1] % 4);
      fresh += (buckets[3] ) / 4;
      buckets[3] = (buckets[3] % 4);
      if(buckets[1] >= 2 && buckets[2] == 1) {
        fresh += 1;
        buckets[1] -= 2;
        buckets[2] -= 1;
      }
      else if (buckets[3] >= 2 && buckets[2] == 1) {
        fresh += 1;
        buckets[3] -= 2;
        buckets[2] -= 1;
      }
    }
    bool extra = false;
    for(int i = 0; i <= 3; i++) {
      if(buckets[i] != 0) {
        extra = true;
      }
    }
    if(extra)
      fresh++;
    cout << "Case #" << t << ": " << fresh << endl;
  }

}
