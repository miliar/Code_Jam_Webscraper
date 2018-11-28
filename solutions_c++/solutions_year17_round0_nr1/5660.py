#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

int main() {
  int t;
  int cases = 0;
  scanf("%d", &t);
  while(t > 0) {
    cases++;
    t--;
    string str;
    int k;
    cin >> str >> k;
    
    int count = 0;
    for(int i = 0; i < str.size(); i++) {
      if(str[i] == '-' && str.size() - i >= k) {
        count++;
        for(int j = 0; j < k; j++) {
          int pos = i+j;
          str[pos] = str[pos] == '-' ? '+' : '-';
        }
      } 
    }

    bool is_valid = true;
    for(int i = 0; i < str.size(); i++) {
      if(str[i] == '-') {
        is_valid = false;
      }
    }
  
    if(is_valid) {
      printf("Case #%d: %d\n", cases, count); 
    } else {
      printf("Case #%d: IMPOSSIBLE\n", cases);
    }
  }

  return 0;
}
