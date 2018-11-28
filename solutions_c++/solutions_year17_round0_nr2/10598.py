#include <iostream>
using namespace std;

bool isTidy(int n) {
    int last = 11;
    while(n>0) {
     int m=n%10;
     n=n/10;
     if(m<=last) last = m;
     else return false;
    }
    return true;
    
    
}



int main() {
 
    int T;
    cin >> T;
    
    for (int i=0; i<T; ++i) {
      int n;
      cin >> n;
      bool end = false;
      while (not end) {
       end =isTidy(n);
       --n; 
      }
      cout << "Case #" << i+1 <<": " << n+1 << endl;
        
        
    }
    
}
