#include <iostream>
#include <vector>
#include <string>
using namespace std;
int main() {
   int test;
   cin >> test;
   int c=1;
   while(test--){
      long long n, k;
      cin >> n >> k;
      int level=0;
      long long temp = 1;
      long long sum = n;
      while((temp<<1)-1 < k) {
         sum -= temp;
         level++;
         temp <<= 1;
      }
      //cout << level << " " << temp << " sum:" << sum << endl;
      //temp >>= 1;
      //sum -= temp;
      long long small = sum/temp;
      long long large = small +1;
      long long n_large = sum - small*temp;
      long long n_small = temp - n_large;
      long long nth = k-temp+1;
      long long target;
      if(nth <= n_large){
         target = large;
      } else {
         target = small;
      }
      //cout << level << " " << temp << " sum:" << sum << " nth:" << nth << " target:" << target << endl;
      long long maxv = target/2;
      cout << "Case #" << c <<": "<< maxv << " " << target-maxv-1  << endl;
      c++;
   }
   return 0;
}
