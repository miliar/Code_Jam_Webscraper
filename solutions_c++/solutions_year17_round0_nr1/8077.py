#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <sstream>
#include <algorithm>
#include <math.h>
//#include <cstdint>
#include <iomanip>

using namespace std;

int main(int argc, char* argv[])
{
  fstream input("test.in");
  fstream out("out.txt", ios_base::out);
  int T = 0;
  string S;
  int K = 0;  //num to flip at a time
  int flips = -1;
  input >> T;
  string line;
  int len;
  int count;
  char c;
  int happyCount = 0;
  int lastHC = 0;
  bool found = false;
  int firstM = 0;

  getline(input, line); //burn the empty line
  for (int i = 1; i <= T; i++)
  {
    input >> S;
    input >> K;
    getline(input, line); //burn the empty line
    flips = 0;
    happyCount = 0;
    lastHC = 0;
    found = false;
    firstM = 0;
    len = S.length();
    while (!found)
    {
      count = 0;
      c = S[0];
      lastHC = happyCount;
      happyCount = 0;
      for (int j = 0; j < len; j++)
      {
        if (S[j] == '+')
        {
          happyCount++;
          if (happyCount == len)
          {
            found = true;
            break;
          }
          if (count)
            count++;
          else
            continue;
        }
        else
        { 
          count++;
        }

        if (count == K)
        {
          for (int k = j + 1 - K; k <= j; k++)
          {
            char c2 = S[k];
            if (c2 == '-')
            {
              S[k] = '+';
              if (!firstM)
                happyCount++;
            }
            else
            {
              S[k] = '-';
              happyCount--;
              if (firstM)
                firstM = min<int>(firstM, k);
              else
                firstM = k;
            }
          }
          if (firstM)
          {
            j = firstM - 1;
            firstM = 0;
          }
          count = 0;
          flips++;
        }

      }

      if (happyCount <= lastHC)
        break;
    }

    out << "Case #" << i << ": ";
    if (found)
        out << flips << endl;
    else
        out << "IMPOSSIBLE" << endl;
  }
	return 0;
}

