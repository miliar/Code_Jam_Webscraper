#include <iostream>
#include <assert.h>
#include <fstream>
#include <string>
#include <vector>

using namespace std;
  
void main()
{
    ifstream inFile("inputLarge.in");
    ofstream outFile("outputLarge.out");
    
    assert(outFile.is_open());
    assert(inFile.is_open());
    
    int T = 0;
    inFile >> T;

    for (int TestCase = 1; TestCase <= T; TestCase++)
    {
       string str;
       inFile >> str;
       int K;
       inFile >> K;

       int unhappyCake = -1;
       int count = 0;
       bool bPossible = true;
       int r = 0;
       do
       {          
          for (int i = r; i < str.length(); i++)
          {
             if (str[i] == '-')
             {
                unhappyCake = i;
                r = i;
                break;
             }
             else
             {
                unhappyCake = -1;
             }
          };

          if (unhappyCake < 0)
          {
             bPossible = true;
             break;
          }
          else if (unhappyCake + K > str.length())
          {
             bPossible = false;
             break;
          }

          for (int j = unhappyCake; j < (unhappyCake + K); j++)
          {
                str[j] = (str[j] == '-') ? '+' : '-';
          }
          
          count++;
       } while (unhappyCake >= 0);
       
       if (bPossible)
       {
          outFile << "Case #" << TestCase << ": " << count << "\n";
       }
       else
       {
          outFile << "Case #" << TestCase << ": " << "IMPOSSIBLE" << "\n";
       }
    }

    inFile.close();
    outFile.close();
}