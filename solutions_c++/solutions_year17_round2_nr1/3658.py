#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;
int main() {
   int test; 
   cin >> test;
   int ith=1;
   while(test--){
      double dest, n;
      cin >> dest >> n;
      vector<double> pos(n);
      vector<double> speed(n);
      vector<double> hr(n);
      for (int i=0; i<n; i++) {
         cin>>pos[i] >>speed[i];
         //printf("%lf", pos[i]);
         hr[i] = ((double)(dest-pos[i])) / ((double)(speed[i]));
         //cout << hr[i];
      }
      double h = *max_element(hr.begin(), hr.end());
      double  res = (double(dest))/h; 
      cout << "Case #" << ith << ": ";
      cout << res << setprecision(8);
      cout << endl;
      ith++;
   }
   return 0;
}
