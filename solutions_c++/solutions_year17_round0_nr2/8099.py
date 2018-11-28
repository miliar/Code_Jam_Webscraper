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

bool isTidy(ULL num)
{
  if (num < 10)
    return true;
  else if (num == 1000000000000000000ULL)
    return false;

  stringstream numStr;
  numStr << num;
  string chars = numStr.str();
  char lastC = chars[0];
  for (auto c:chars)
  {
    if (c < lastC)
      return false;
    lastC = c;
  }
  return true;
}

int main(int argc, char* argv[])
{
  fstream input("test.in");
  fstream out("../out.txt", ios_base::out);
  
  int T = 0;
  ULL N = 0;  
  input >> T;
  string line;

  getline(input, line); //burn the empty line
  for (int i = 1; i <= T; i++)
  {
    input >> N;
    getline(input, line); //burn the empty line

    while (!isTidy(N))
      N--;

    out << "Case #" << i << ": ";
    out << N <<endl;
  }
	return 0;
}

