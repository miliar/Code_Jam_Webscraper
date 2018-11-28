#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

long long power(int i){
  long long a = 1;
  for (int j = i; j > 0; j--){
    a = a * 10;
  }
  return a;
}

long long tn(long long n){
  int a[18];
  long long tempn = n;
  long long ans = 0;
  for (int d = 17; d >= 0; d--){
    a[17 - d] = tempn / power(d);
    tempn = tempn % power(d);
  }
  bool s9 = false;
  for (int d = 0;  d < 17; d++){
    if(s9){
      a[d] = 9;
    }
    if((s9 == false) && (a[d] > a[d+1])){
      a[d] = a[d] - 1;
      for(int e = d - 1; e > 1; e--){
        if(a[e] == a[e+1]+1){
          a[e] = a[e] - 1;
          a[e+1] = 9;
        } 
      } 
      s9 = true; 
    }
  }
  if(s9) a[17] = 9;
  for (int d = 17; d >= 0; d--){
    ans = ans + a[17 - d] * power(d);
  }
  return ans;  
}

int main(){
  int t = 0;
  cin >> t;
  for(int i = 1; i <= t; i++){
    long long n = 0;
    cin >> n;
    cout << "Case #" << i << ": " << tn(n) << "\n";
  }
}
