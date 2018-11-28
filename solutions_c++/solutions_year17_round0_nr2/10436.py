#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;
bool areSorted( int n)
{

    bool x=false;// Note that digits are traversed from last to first
    int next_digit = n%10;
    n = n/10;
    while (n)
    {
        int digit = n%10;
        if (digit >next_digit){x=false;
            return x;}
        next_digit = digit;
        n = n/10;
    }
     x=true;
    return x;
} // since cin and cout are both in namespace std, this saves some text
int main() {
  int t, n;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
        cin>>n;
        while(1)
        {
          bool y= areSorted(n);
          if(y==true)
                break;
          else
            n=n-1;
        }
     cout<<"Case #"<<i<<": "<<n<<endl;
  }
return 0;
}
