#include <cstdlib>
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <sstream>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

long long getModNumber(long long num) {
    int length,indx,pointer=0;
    bool isSmall = false, isRepeat = false;
    long long mod = 1,i;
    std::ostringstream ss;
    ss << num;
    string temp = ss.str();

    length = temp.length();

    for( indx = 0 ; indx < length - 1; indx++ ) {
        if(temp.at(indx) - '0' == temp.at(indx+1) - '0' ) {
            continue;
        } else if(temp.at(indx) - '0' < temp.at(indx+1) - '0' ) {
            pointer = indx + 1;
        } else if(temp.at(indx) - '0' > temp.at(indx+1) - '0' ) {
            pointer ++;
            pointer = length - pointer;
            for(i=1;i<=pointer;i++) {
                mod *= 10;
            }
            break;
        }
    }
    return mod;
}

int main() {
  int t, n;
  long long num, other;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    long long modValue = 0;
  	cin >> num;
    modValue = getModNumber(num);
    if(modValue != 1) {
        other = num % modValue + 1;
        num = num - other;
    }

 	cout << "Case #" << i << ": " << num << endl;

  }
  return 0;
}
