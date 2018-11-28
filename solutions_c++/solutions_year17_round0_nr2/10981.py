//Small data-set Problem B
#include <stdio.h>
#include <string.h>
#include <string>
#include <iostream>
using namespace std;




int main()
{
  int numInputs,currInput,z;
  cin >> numInputs;
  for(int i = 1; i<=numInputs; i++)
  {
    cin >> currInput;
    //for single input
    for(int y = currInput; y>0; y--)
    {
      string s = to_string(static_cast<long long>(y));
      const char* charInt = s.c_str();
      int length = strlen(charInt);
      if(length >1)
      {
        //checking each decremented number
        for( z = 0; z<length-1; z++)
        {
          if(charInt[z+1]<charInt[z])
            break;

        }
        if(z==length-1)
        {
          cout<<"Case #"<<i<<": "<<y<<endl;
          break;
        }
      }
      else
      { 
        cout<<"Case #"<<i<<": "<< y<<endl;
        break;
      }
    }
  }
  return 0;
}
