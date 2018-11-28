#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>

using namespace std;

int main() 
{
  int t,Case = 0, n, m;
  cin >> t;
  string s;
  while(t != 0)
  {
  	t--;
  	cin >> s >> n;
  	//cout << s << " " << n << endl;
  	int count=0;
  	int flag = 1;
  	cout << "case #" << ++Case << ": " ;
  	for(int i = 0; i < s.length(); i++)
  	{
  		//cout << s << endl;
  		if(s[i] == '-')
  		{
			count++;
  			int upper = i+n;
  			if(upper > s.length())
  			{
  				flag = 0;
  				cout << "IMPOSSIBLE" << endl;
  				break;
  			}
  			else
	  		for(int j = i; j < i+n; j++)
  			{
  				flag = 1;
  				//cout <<s << " " << j;
  				if(s[j] == '+')
  					s[j] = '-';
  				else if(s[j] == '-')
  					s[j] = '+';

  			}
  			//cout << s << endl;
  		}
  	}
  	if(flag != 0)
	  	cout << count << endl;
  }
  return 1;
}
