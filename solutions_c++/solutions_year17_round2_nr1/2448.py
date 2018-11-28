#include <stdio.h>
#include <iostream>
#include <vector>
#include <set>
#include <unordered_set>
#include <unordered_map>
#include <limits.h>
#include <iomanip>

using namespace std;

int main(){

   int T;

   scanf("%d", &T);

   for(int t=1; t<=T; t++){

      int D, N;
      double y;

      scanf("%d %d", &D, &N);

      double maxTime = 0;

      for(int i=0; i<N; i++){
         int k, s;
         scanf("%d %d", &k, &s);
         maxTime = max(maxTime, (D-k)/(double) s);
      }

      printf("Case #%d: ", t);
      cout << std::fixed;
      cout << std::setprecision(6);
      cout << D/maxTime << endl;
   }

   return 0;
}
