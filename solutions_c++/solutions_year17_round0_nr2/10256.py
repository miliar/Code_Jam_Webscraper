#include <iostream>  // includes cin to read from stdin and cout to write to stdout

using namespace std;  // since cin and cout are both in namespace std, this saves some text

bool IsSorted(long long n){
    int arry[200];
    int idx=0;

    while(n > 9){
        arry[idx] = n%10;
        n = n/10; 
        if ((n%10 > arry[idx++]))
            return false;
    }
    
    return true;
}



long long tidy(long long n) {
   
   for (long long i=n; i >= 0; --i) {
        if(IsSorted(i))
            return i;
   } 
    
    return 0;
}

int main() {
  int t;
  long long n;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> n;  // read n and then m.
    cout << "Case #" << i << ": " << tidy(n) << " "<< endl;
  }

  return 0;
}


