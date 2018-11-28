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
    cin >> s;
    if( s.size() == 1 )
      cout << s <<endl;
    else
    {
      string mini = string( s.size() , '1');
      string ans;
      if( mini > s )
	ans = string( s.size() - 1 , '9');
      else
      {
	for( int i = 1 ; i < s.size() ; ++i )
	{
	  if( s[i] < s[i-1] ){
	    s[i-1]--;
	    for(int j = i ; j < s.size() ; ++j )
	      s[j] = '9'; 
	    i-=2;
	   }

	}
	ans = s;
      }
      cout << ans <<endl;
    }
  }
  return 0;
}
