#include <iostream>
using namespace std;
int h[24*60+1];
int sc[101][2];
int sj[101][2];
int main() {
  int t, ac, aj;
  cin >> t;
  for(int z = 1; z <= t; z++) {
    cin >> ac >> aj;
    int j, k;
    for(int i =  0; i < 24*60+1; i++) {
      h[i] = 0;
    }
    int wc, wj;
    wc = 0;
    wj = 0;
    for(int i = 0; i < ac; i++) {
      cin >> sc[i][0] >> sc[i][1];
      /*
      cin >> j >> k;
      wc += k-j;
      for(int q = j; q < k; q++) {
        h[q] = 1;
      }*/
    }
    for(int i = 0; i < aj; i++) {
      cin >> sj[i][0] >> sj[i][1];
/*
      cin >> j >> k;
      wj += k-j;
      for(int q = j; q < k; q++) {
        h[q] = -1;
      }
      */
    }
    if(ac  <= 1 and aj <= 1) printf("Case #%d: %d\n", z, 2);
    else {
      if(ac == 2) {
        if(max(sc[0][1], sc[1][1]) - min(sc[0][0], sc[1][0]) > 720
        and min(sc[0][1], sc[1][1]) + 24*60 - max(sc[0][0], sc[1][0]) > 720 )
        printf("Case #%d: %d\n", z, 4);
        else printf("Case #%d: %d\n", z, 2);
      }
      else {
        if(max(sj[0][1], sj[1][1]) - min(sj[0][0], sj[1][0]) > 720
        and min(sj[0][1], sj[1][1]) + 24*60 - max(sj[0][0], sj[1][0]) > 720 )
        printf("Case #%d: %d\n", z, 4);
        else printf("Case #%d: %d\n", z, 2);
      }
    }
  }
}
