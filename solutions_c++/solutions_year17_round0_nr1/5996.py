#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <cmath>
#include <cstdlib>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

// Prototypes

string flipPancakes (string n, int k, int pos) {
  for (int i = 0; i < k; ++i)
  {
    if (n[pos + i] == '+')
    {
      n[pos + i] = '-';
    }
    else
    {
      n[pos + i] = '+';
    }
  }
  // cout << n << endl;
  return n;
}

string minFlips (string n, int k) {
  int flipcount = 0;
  int size = n.size();
  // cout << n << endl;
  // cout << size << endl;


  int i = 0;
  while (i <= (size - k))
  {
    // cout << n << endl;
    if (n[i] == '-')
    {
      n = flipPancakes(n, k, i); // Flip them pancakes
      flipcount++;
      // cout << "Flipped! " << n << endl;
    }
    i++;
  }



  for (int k = 0; k < size; ++k)
  {
    if (n[k] == '-')
    {
      string out = "IMPOSSIBLE";
      return out;
    }
  }


  string output = to_string(flipcount);
  return output;

}

int main() {
  int t, k;
  string n;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  
  for (int i = 1; i <= t; ++i) {
    cin >> n;  // read the string n from the input
    cin >> k;  // read the size of the pancake flipper
    cout << "Case #" << i << ": " << minFlips(n, k) << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }

  return 0;
}
