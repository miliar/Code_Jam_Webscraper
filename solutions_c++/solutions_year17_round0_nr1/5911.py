#include <bits/stdc++.h>

using namespace std;

char s[1002];
int k;

void reversar(int inicial) {
  int cont = 0;
  for(int i = inicial ;cont < k; ++i){
    if(s[i] == '-') s[i]= '+';
    else  s[i] = '-';
    ++cont;
  }
}

int can() {
  int len = strlen(s), ans = 0;
  for(int i = 0; i + k <= len ; ++i) {
    // cout << i << endl;
    if(s[i] == '-'){
      // cout << "Reversando " << i << endl;
      ++ans;
      reversar(i);
    }
  }
  for(int i = 0 ; i < len ; ++i)
    if(s[i] == '-') return -1;
  return ans;
}

int main() {
  int c = 0;
  cin >> c;
  for(int p = 1 ; p <= c ; ++p){
    cin >> s >> k;
    cout << "Case #" << p << ": ";
    int ans = can();
    if(ans == -1){
      puts("IMPOSSIBLE");
    }
    else{
      printf("%d\n", ans);
    }
  }
  return 0;
}
