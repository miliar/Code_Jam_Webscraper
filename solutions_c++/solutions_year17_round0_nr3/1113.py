#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <map>
#include <climits>
#include <stack>
#include <string>
#include <stdio.h>
#include <ctype.h>
#include <cstdint>
#include <unordered_set>
#include <unordered_map>
#include <utility>
#include <math.h>

using namespace std;

int main() {
  int t;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.

  for (int i = 1; i <= t; ++i) {
    long long k;
    long long n;
    cin >> n >> k;
    pair<long long, long long> odd(0,0);
    pair<long long, long long> even(0,0);
    if(n&1){
      odd.first = 1;
      odd.second = n;
    }else{
      even.first = 1;
      even.second = n;
    }
    
    while(even.first + odd.first < k){
      k = k - even.first - odd.first;
      pair<long long, long long> odd_next(0,0);
      pair<long long, long long> even_next(0,0);
      if((odd.second/2) & 1){
        odd_next.first += odd.first * 2;
        odd_next.second = odd.second/2;
      }
      else{
        even_next.first += odd.first * 2;
        even_next.second = odd.second/2;
      }
      
      odd_next.first += even.first;
      even_next.first += even.first;
      if(even.first > 0){
        if((even.second/2)&1){
            odd_next.second = even.second/2;
            even_next.second = (even.second - 1) / 2;
        }else{
            odd_next.second = (even.second - 1)/2;
            even_next.second = even.second/2;
        }
      }
      even = even_next;
      odd = odd_next;
    }
    
    long long min_value;
    long long max_value;
    if(even.second < odd.second){
      if(k <= odd.first){
        min_value = odd.second/2;
        max_value = odd.second/2;
      }else{
        min_value = (even.second - 1)/2;
        max_value = even.second / 2;
      }
    }else{
      if(k <= even.first){
        min_value = (even.second - 1)/2;
        max_value = even.second / 2;
      }else{
        min_value = odd.second/2;
        max_value = odd.second/2;        
      }
    }
    
    cout << "Case #" << i << ": " << max_value << " " << min_value << endl;
  }
  
  return 0;
}