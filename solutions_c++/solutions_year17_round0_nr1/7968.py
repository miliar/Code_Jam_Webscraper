#include <iostream>
using namespace std;

int main()
{
  int cases;
  cin >> cases;
  for(int i=1;i<=cases;i++)
    {
      int flop[2001]={};
      string pancake; cin >> pancake;
      int k; cin >> k;
      int nFlips=0;
      bool flip=false;
      for(int j=0;j<pancake.length();j++)
	{
	  if(flop[j])
	    flip=!flip;
	 
	  if((pancake.at(j)=='-' && !flip) ||
	     (pancake.at(j)=='+' && flip))
	    {
	      flip=!flip;
	      nFlips++;
	      flop[j+k]=1;
	    }
	 
	}
      flip=true;
      cout << "Case #" << i << ": ";
      for(int j=pancake.length()+1;j<pancake.length()+k;j++)
	if(flop[j])
	  {
	    cout << "IMPOSSIBLE" << endl;
	    flip=false;
	    break;
	  }
      if(flip)
	cout << nFlips << endl;
    }
}
