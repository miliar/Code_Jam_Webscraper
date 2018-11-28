#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <algorithm> 
#include <set>
#include <vector>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

unsigned long long tidy_number(unsigned long long n)
{
  string s = to_string(n);

  while (prev_permutation(s.begin(), s.end()))
  {
    n--;
    s = to_string(n);
  }

  return n;
}

int main() 
{ 
  int t, n, m;
  unsigned long long x;

  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  //cout << "Number of test cases : " << t << endl;

  for (int i = 1; i <= t; ++i) 
  {
    cin >> x;  // read n and then m.
    cout << "Case #" << i << ": " <<  tidy_number(x) << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }


  return 0;
}

