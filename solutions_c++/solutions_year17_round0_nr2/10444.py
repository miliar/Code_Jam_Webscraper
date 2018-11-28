#include <iostream.h>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text
long long int isTidy(long long int inp){
    long long int result = 1;
    while(inp > 0){
        if(inp%10 < (inp/10)%10)
            result = 0;
        inp = inp/10;
    }
    return result;
}
long long int lastTidy(long long int inp){
    long long int result = inp;
    while(!isTidy(inp--))
        result = inp;
    return result;
}
int main() {
  long long int t, inp;
  cin >> t;
  for (long long int i = 1; i <= t; ++i) {
    cin >> inp;  // read n and then m.
    cout << "Case #" << i << ": " << lastTidy(inp) <<endl;
    
  }
  return 0;
}