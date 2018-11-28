#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <algorithm> 
#include <set>
#include <vector>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

int convert(string input, int k)
{
  //cout << input << "   " << k << endl;
  //reverse(input.begin(), input.end());
  int size = input.size();
  vector<int> v;

  for (auto x : input)
  {
    if (x == '+')
    {
      v.push_back(1);
    }
    else
    {
      v.push_back(0);
    }
  }

  int count = 0;
  for (int j=0; j < size; ++j)
  {
    if (v[j] == 0)
    {
      count++;
      if (j+k <= size)
      {
        for (int i=0; i < k; ++i)
          v[j+i] = !v[j+i];
        //v[j] = !v[j];
        //v[j+1] = !v[j+1];
        //v[j+2] = !v[j+2];
      }
    }
  }

  //for (int j=0; j<size; ++j)
  //  cout << v[j];
  //cout << endl;

  for (int j=0; j<size;++j)
    if (v[j] == 0)
      count = -1;

  //cout << "count is " << count << endl;

  return count;
}

int main() 
{ 
  int t, k;
  string s;
  int c = 0;

  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  //cout << "Number of test cases : " << t << endl;

  for (int i = 1; i <= t; ++i) 
  {
    cin >> s;  // read n and then m.
    cin >> k;
    c = convert(s, k);
    if ( c >= 0 )
      cout << "Case #" << i << ": " << c << endl;
    else
      cout << "Case #" << i << ": " <<  "IMPOSSIBLE" << endl;
    //cout << "Case #" << i << ": " << convert(s) << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
    c = 0;
  }


  return 0;
}

