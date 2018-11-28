#include<iostream>
using namespace std;

int main()
{
  int t;
  cin >> t;
  for( int tc = 1 ; tc <= t ; ++tc )
  {
    cout << "Case #"<<tc<<": ";
    string s;
    int k;
    cin >> s >> k;
    bool ok = true;
    int minSteps = 0;
    for( int i = 0 ; i < s.size() ; ++i )
    {
      if( i + k <= s.size() and s[i] == '-' )
      {
	++minSteps;
	for( int j = 0 ; j < k ; ++j )
	  s[i+j] = (s[i+j] == '+')? '-':'+';
      }

      ok = ok and s[i] == '+';
    }
    if( ok )
      cout << minSteps <<endl;
    else 
      cout << "IMPOSSIBLE" <<endl;
  }
  return 0;
}
