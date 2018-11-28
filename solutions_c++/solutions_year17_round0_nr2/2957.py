#include <fstream>
#include <algorithm>
#include <queue>
#include <vector>
#include <iostream>
#include <cmath>
#include <string>

using namespace std;

vector<int> num;

void crnum( long long N )
{
  if (N >= 10)
    crnum(N / 10);
  num.push_back(N % 10);
}

long long solve( long long N)
{
  num.clear();
  crnum(N);
  long long res = 0;
  int prev = 0;
  bool flag = true;
  for (auto & i : num)
  {
    if (i < prev)
      flag = false;
    if (flag)
      res = res * 10 + i;
    else
      res *= 10;
    prev = i;
  }
  if (!flag)
    res--;

  return res;
}


int main( void )
{
  ifstream fin("B-large.in");
  ofstream fout("output.txt");

  int T;
  fin >> T;
  
  for (int i = 0; i < T; i++)
  {
    long long N;
    fin >> N;
    while (N != solve(N))
      N = solve(N);
    fout << "Case #" << i + 1 << ": " << N << endl;
  }

  return 0;
}