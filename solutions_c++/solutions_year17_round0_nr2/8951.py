#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){

  string tempForVector;
  int numberOfInput;
  cin >> numberOfInput;
  vector<string> inputVector(numberOfInput);
  for (int i = 0; i < numberOfInput; ++i)
  {
    cin >> tempForVector;
    inputVector[i] = tempForVector;
  }
  int allIndex = 0;

  while(allIndex != numberOfInput)
  {
    bool tidyFlag = false;
    if (inputVector[allIndex][0] == '1')
    {
      for (int i = 0; i < inputVector[allIndex].size() - 1; ++i)
      {
        if (inputVector[allIndex][i] != '1')
        {
          break;
        }
        if (inputVector[allIndex][i+1] == '0')
        {
          cout << "Case #" << allIndex+1 << ": ";
          for (int i = 0; i < inputVector[allIndex].size()-1; ++i)
          {
            cout << 9;
          }
          cout << endl;
        tidyFlag = true;
        break;
        }
      }
      if(tidyFlag)
      {
        allIndex++;
        continue;
      }
    }
    for(int i = 0; i < inputVector[allIndex].size()-1; i++)
    {
      if((inputVector[allIndex][i]) - 48 > (inputVector[allIndex][i+1]) - 48)
      {
        int temp = inputVector[allIndex][i] - 48;
        for(int k = i+1; k < inputVector[allIndex].size(); k++)
        {
          inputVector[allIndex][k] = '9';
        }
        for(int j = i; j > -1; j--)
        {
          if((inputVector[allIndex][j] == temp + '0' && inputVector[allIndex][j-1] == temp + '0'))
          {
            inputVector[allIndex][j] = '9';
          }
          else
          {
            inputVector[allIndex][j] = (temp-1) + '0';
            break;
          }
        }
      }
    }
      cout << "Case #" << allIndex+1 << ": ";
      cout << inputVector[allIndex] << endl;
    allIndex++;
  }
  return 0;
}