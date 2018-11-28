#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <vector>
using namespace std;  // since cin and cout are both in namespace std, this saves some text


  bool isTidy(int n) {
  	if (n < 10) return true;
  	int lastGeWei = n%10;
  	while (n >= 10)
  	{
  		n = n/10;
  		int geWei = n%10;
  		if (geWei > lastGeWei) return false;
  		lastGeWei = geWei;
  	}

  	return true;
  }

int lastTidy(int n) {
  	while (n != 0)
  	{
  		if(isTidy(n)) return n;
  		n--;
  	}
  	return n;
  }

int main() {
  int t, n;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> n;  // read n and then m.
    int answer = lastTidy(n);
    cout << "Case #" << i << ": " << answer << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
}