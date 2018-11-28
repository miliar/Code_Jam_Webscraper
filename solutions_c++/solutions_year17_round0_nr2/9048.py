 #include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string.h>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
int  main() {
  int t;
  unsigned long long a,k;
  cin >>t;
  for (int i = 1; i <= t; i++) {
    cin >> k;  // read s and then k.
    for(unsigned long long j = k; j>=1;j--)
    {
      a=j;
      while(a)
        {
            if(a%10 < (a/10)%10){ break;}
            a = a / 10;
        }
         if(a == 0)
         {
            cout << "Case #" << i << ": " << j << endl;
            break;
         }
    }
    }
    return 0;
}
