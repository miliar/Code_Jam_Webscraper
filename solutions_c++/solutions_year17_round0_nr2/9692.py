#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text
int main() {
  int t, n;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> n;
    for(int j=n;j>=0;j--){
        int x=j,k=9,flag=0;
        while(x!=0){
            if(x%10<=k){
                k=x%10;
                x/=10;
            }
            else {
                    flag=1;
                    break;
            }
        }
        if(flag==0){
        cout << "Case #" << i << ": "<<j<<endl;
            break;
        }
    }

  }
  return 0;
}
