#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <iterator>
using namespace std;

string str;

int
scan_input (int start, int end)
{

  for (int it = start; it < end; it++)
    {
      if (str[it] > str[it + 1])
	return 0;
    }
  return 1;
}

int
main ()
{
  int inputc;
  while (cin >> inputc)
    {
      int cases = 0;
      while (inputc--)
	{

	  cin >> str;
	  int len = (int) str.length ();
	  int pos = len - 1;
	  while (true)
	    {

	      if (scan_input (0, pos))
		break;

	      int it;
	      for (it = 0; it < pos; it++)
		{
		  if (str[it] > str[it + 1])
		    {
		      str[it]--;
		      for (int j = it + 1; j <= pos; j++)
			{
			  str[j] = '9';
			}
		      break;
		    }
		}
	      pos = it;
	    }
	  cout << "Case #" << ++cases << ": ";
	  for (int it = 0; it < len; it++)
	    {
	      if (it == 0 && str[it] == '0')
		continue;
	      cout << str[it];
	    }
	  cout << endl;
	}
    }
  return 0;
}
