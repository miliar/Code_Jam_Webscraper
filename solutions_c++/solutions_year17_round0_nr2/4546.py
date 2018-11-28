#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
  long long T, k, n, res;
  vector<long long> digits;
  bool sorted;
  
  scanf("%lld",&T);
  for (long long t=1; t<=T; t++) {
    scanf("%lld",&n);
    
    digits.clear();
    
    k = n;
    while (k>0) {
      digits.push_back(k%10);
      k/=10;
    }
    
    for (long long i=1; i<digits.size(); i++) {
      sorted = true;
      for (long long j=1; j<digits.size(); j++) {
        if (digits[j] > digits[j-1]) {
          sorted = false;
          break;
        }
      }
      if (sorted) {
        break;
      }
      digits[i-1] = 9;
      digits[i]--;
    }
    
    reverse(digits.begin(), digits.end());
    
    res = 0;
    for (int i=0; i<digits.size(); i++) {
      res*=10;
      res+=digits[i];
    }
    
    printf("Case #%lld: %lld\n",t,res);
  }
  
  return 0;
}
