#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

struct horse
{
  int k;
  int s;
};
bool operator<(const horse& a, const horse& b)
{
  return a.k > b.k;
}
double velCalc(horse h, int d)
{
  return (double(d)*h.s)/(d - h.k);
}
int main()
{
  ifstream fin;
  fin.open("A-small-attempt2.in");
  ofstream fout;
  fout.open("output.txt");
  int testCases;
  fin >> testCases;
  for(int i = 0; i < testCases; i++)
  {
    int d;
    fin >> d;
    int horseCount;
    fin >> horseCount;
    vector<horse> horses;
    for(int n = 0; n < horseCount; n++)
    {
      horse h;
      fin >> h.k;
      fin >> h.s;
      horses.push_back(h);
    }
    sort(horses.begin(), horses.end());
    double v;
    if(horses.size() == 1)
    {
      v = velCalc(horses[0], d);
    }
    else if(horses.size() == 2)
    {
      double tCatch = (double(horses[0].k) - horses[1].k)/(horses[1].s - horses[0].s);
      double pCatch = horses[1].s * tCatch + horses[1].k;
      if(pCatch > d || tCatch < 0)
      {
        v = velCalc(horses[1], d);
      }
      else
      {
        v = velCalc(horses[0], d);
      }
    }
    fout << fixed << "Case #" << i + 1 << ": " << setprecision(9) << v << endl;
  }
  return 0;
}
