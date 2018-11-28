#include <iostream>
#include <math.h>
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)
using namespace std;

typedef long int uli;

uli tidyNum(uli m);
bool isNonDescending(uli m);
uli getPreviousTidyNum(uli m);

int main() {
  int t;
  uli n;
  cin >> t;
  for1(i,t) {
    cin >> n;
    uli N = tidyNum(n);
    cout << "Case #" << i << ": " << (N) << endl;
  }
  return 0;
}

uli tidyNum(uli m){
uli n = m;
  if(n<9){
    return n;
  }
  else {
    while(n>=10){
      if(isNonDescending(n)){
        return n;
      }
      --n;
    }
    return n;
  }
}

bool isNonDescending(uli m){
  if(m<10){
    return true;
  }
  else{
    int a = m % 10, b = (m/10) % 10;
    if(a<b){
      return false;
    }
    else{
      return isNonDescending(m/10);
    }
  }
}