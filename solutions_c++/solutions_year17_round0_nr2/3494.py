#include <cstdio>
#include <cstring>
#include <vector>

inline bool isTidy(long long n){
  int nowdigit = 10;
  while(n > 0){
    int d = n%10;
    if(d <= nowdigit)
      nowdigit = d;
    else
      return false;
    n /= 10;
  }
  return true;
}

inline long long checkTidy(long long n){
  long long originaln = n;
  std::vector<int> digits;
  while(n > 0){
    digits.push_back(n%10);
    n/=10;
  }
  for(int i = digits.size()-1; i > 0; i--){
    if(digits[i] > digits[i-1]){
      //long long minus = 1;
      //for(int j = 0; j < i-1; j++)
      //        minus *= 10;
      digits[i]--;
      for(int j = i-1; j >= 0; j--)
        digits[j] = 9;
      //printf("%lld , digit %d, minus %lld\n", originaln, i-1, minus);
      long long ans = 0, base = 1;
      for(int k = 0; k < digits.size(); k++){
        ans += base * digits[k];
        base *= 10;
      }
      //printf("%lld , digit %d, afterminus%lld\n", originaln, i, ans);
      return ans;
    }
  }
  return originaln;
  /*long long originaln = n;
  int digit = 0;
  int nowdigit = 10;
  while(n > 0){
    int d = n%10;
    if(d <= nowdigit)
      nowdigit = d;
    else{
      int minus = nowdigit+10-d;
      for(int i = 0; i < digit; i++)
        minus *= 10;
      printf("%lld , digit %d, minus %d\n", originaln, digit, minus);
      return originaln-minus;
    }
    n /= 10;
    digit++;
  }
  return 0;*/
}

long long getMaxTidy(long long n){
  while(n >= 0){
    long long nextn = checkTidy(n);
    if(nextn == n)
      return n;
    n = nextn;
  }
  return 0;
}

int main(){
  int T;
  long long N;
  scanf("%d", &T);
  int t = 1;
  while(t < T+1){
    scanf("%lld", &N);
    long long ans = getMaxTidy(N);
    printf("Case #%d: %lld\n", t, ans);
    t++;
  }
}
