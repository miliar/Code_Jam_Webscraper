#include <iostream>
#include <fstream>
#include <algorithm>
#include <iomanip>
using namespace std;

int main()
{
  ifstream in("A-large.in");
  ofstream out("output.txt");

  int T;
  in>>T;
  for(int t=0; t<T; t++)
  {
    double m = 0;
    int D, N;
    in>>D>>N;
    for(int i=0, a, b; i<N; i++)
    {
      in>>a>>b;
      m = max(m, (double)(D - a) / (double)b);
    }
    double speed = (double)D / m;
    out<<"Case #"<<(t+1)<<": ";
    out<<std::fixed<<std::setprecision(6)<<speed<<"\n";
  }

  in.close();
  out.close();
  return 0;
}
