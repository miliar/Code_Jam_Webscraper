#include <iostream>
#include <string>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int main() {
  int T;

  cin >> T;

  for (int t=1;t<=T;t++) {
    int N, C, M;
    cin >> N >> C >> M;

    vector<int> nt(C, 0);
    vector<int> ns(N, 0);
    for (int i=0;i<M;i++) {
      int p, b;
      cin >> p >> b;
      b--;
      nt[b]++;
      p--;
      ns[p]++;
    }

    int num = 0;
    for (int i=0;i<C;i++) {
      num = max(num, nt[i]);
    }

    int total=0;
    for (int i=0;i<N;i++) {
      total += ns[i];

      num = max(num, (total+i)/(i+1));
    }

    int promo = 0;
    for (int i=0;i<N;i++) {
      promo += max(0, ns[i] - num);
    }

    printf("Case #%d: %d %d\n", t, num, promo);
  }

}

