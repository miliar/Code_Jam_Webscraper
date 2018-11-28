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

#define ULL unsigned long long

int main(int argc, char* argv[])
{
  fstream input("test.in");
  fstream out("../out.txt", ios_base::out);
  
  int T = 0;
  unsigned long long S; //chosen stall
  unsigned long long K = 0;  //num people
  unsigned long long N = 0;  //Stalls
  unsigned long long y = 0;  //max
  unsigned long long z = 0;  //min
  unsigned long long leftMax = 0;  //max
  unsigned long long leftMin = 0;  //min
  unsigned long long rightMax = 0;  //max
  unsigned long long rightMin = 0;  //min

//  vector<unsigned long long> LS, RS, MIN, MAX;
  input >> T;
  string line;

  getline(input, line); //burn the empty line
  for (int i = 1; i <= T; i++)
  {
    input >> N;
    input >> K;
    getline(input, line); //burn the empty line
    /*
        1 2 3 4 5 6 7 8 9 0
        1 0 0 0 0 0 0 0 0 1
                 /\
    1 0 0 0 1 (3)  1 0 0 0 0 1 (4)
        /   \             / \            
     101(1) 101 (1)   101(1) 1001 (2)
                              /  \
                           11(0) 101(1)

          1 2 3 4 5 6 7 8 9 
          1 0 0 0 0 0 0 0 1 
                        /\
          1 0 0 0 1 (3)  1 0 0 0 1 (3)
          /   \             / \
          101(1) 101 (1)   101(1) 1001 (2)
          /  \
          11(0) 101(1)

    */
    
    multiset<unsigned long long> possibleVals;
     
    possibleVals.insert(N);
    for (int per = 1; per < K; per++)
    {
      ULL val = *possibleVals.rbegin();
      possibleVals.erase(--possibleVals.end(), possibleVals.end());
      if (val > 1)
      {
        ULL val1 = val / 2;
        ULL val2 = val1;
        if (val % 2 == 0)
        {
          val2--;
        }
        possibleVals.insert(val1);
        possibleVals.insert(val2);
      }
    }

    ULL val = *possibleVals.rbegin();
    if (!val)
    {
      y = 0;
      z = 0;
    }
    else
    {
      y = val / 2;
      z = y;
      if (val % 2 == 0)
      {
        z--;
      }
    }
    out << "Case #" << i << ": ";
    out << y << " " << z <<endl;
  }
	return 0;
}

