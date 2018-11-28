#include <iostream>
#include <string.h>
#include <fstream>
using namespace std;

ifstream fin("date.in");
ofstream fout("date.out");

bool v[1000];
char s[1000];
int k;
int l;
int moves;
int incp;
int cas;
bool endcon;

bool flipped()
{
  for (int i = 0; i < l; i ++)
    if (!v[i])
      return false;
  return true;
}

void flip(int start)
{
    if (flipped())
        return;

  moves ++;
  while(v[start] && start + k < l)
  {
    start ++;
  }

  incp = start;

  if (start + k == l)
  {
    endcon = true;
    for (int i = 0; i < k; i ++)
        v[start + i] = !v[start + i];
    return;
  }

    for (int i = 0; i < k; i ++)
        v[start + i] = !v[start + i];

  flip(start);
}

void rez()
{
  fin >> s >> k;
  l = strlen(s);
  for (int i = 0; i < l; i ++)
    v[i] = (s[i] == '+');

  moves = 0;

  flip(0);

    fout << "Case #" << cas << ": ";
    if (!flipped())
        fout << "IMPOSSIBLE\n";
    else
        fout << moves << "\n";
}

int main()
{
  int n;
  fin >> n;
  for (int i = 0; i < n; i ++)
  {
    cas ++;
    rez();
  }
}
