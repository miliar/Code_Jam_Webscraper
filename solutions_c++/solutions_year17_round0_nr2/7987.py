#include <iostream>

using namespace std;

string clean(string counting)
{
  bool F = false;
  int pos9 = counting.length();
  if(pos9==1)
    return counting;
  
  for(int i=pos9-1;i>0;i--)
    {
      if(counting.at(i)<counting.at(i-1))
	{
	  while(i > 1 && counting.at(i)==counting.at(i-1))
	    i--;
	  pos9=i-1;
	  F=true;
	}
      else if(counting.at(i)==counting.at(i-1) && F)
	{
	  pos9=i-1;
	}
      else
	F=false;
    }
  
  if(pos9==counting.length())
    return counting;
  
  for(int i=pos9+1;i<counting.length();i++)
      counting.at(i)='9';
      
  if(counting.at(pos9)=='1')
    return counting.substr(1);

  counting.at(pos9)--;

  return counting;
}

int main()
{
  int cases; cin >> cases;
  for(int i =1;i<=cases;i++)
    {
      string counting, tidy;
      cin >> counting;

      tidy=clean(counting);
      
      cout << "Case #" << i << ": " << tidy << endl;
    }
}
