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
  int D = 0; //dest
  int N = 0;  //# horses
  input >> T;
  string line;

  struct horse {
    int pos;
    int speed;
  };
  
  out << std::fixed;
  out << std::setprecision(6);

  long double maxT;
  getline(input, line); //burn the empty line
  for (int i = 1; i <= T; i++)
  {
    input >> D;
    input >> N;
    getline(input, line); //burn the empty line
    vector<horse> horses;
    maxT = 0;
//     out << "Case #" << i << ": ";
//     out << D << " " << N << endl;
    for (int j = 0; j < N; j++)
    {
      horse h;
      input >> h.pos;
      input >> h.speed;
      horses.push_back(h);
      long double t = ((long double)(D - h.pos))/h.speed;
//      out << t << " " << maxT << endl;
      maxT = max(t, maxT);
  //    out << h.pos << " " << h.speed << endl;
    }

    out << "Case #" << i << ": ";
    out << (D / maxT) << endl;
  }
	return 0;
}

