#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <cassert>
#include <unordered_map>
#include <unordered_set>
#include <cstring>

using namespace std;


int Encode(int r, int c, int R, int C)
{
  return r | (c << 5) | (R << 10) | (C << 15);
}

void Decode(int Code, int &r, int &c, int &R, int &C)
{
  r = Code & 31;
  c = (Code >> 5) & 31;
  R = (Code >> 10) & 31;
  C = (Code >> 15) & 31;
}

char ExactlyOne(const array<array<char, 25>, 25> &G,
                const int r, const int c, const int R, const int C)
{
  char e = 0;
  for (int i = r; i <= R; ++i)
  {
    for (int j = c; j <= C; ++j)
    {
      if (G[i][j] != '?')
      {
        if (e == 0) e = G[i][j];
        else if (G[i][j] != e) return 0;
      }
    }
  }

  return e;
}


bool Recurse(const int r, const int c, const int R, const int C,
             const array<array<char, 25>, 25> &G,
             unordered_map<int, array<array<char, 25>, 25>> &M)
{
  if (r == R || c == C) return true;

  int Code = Encode(r, c, R, C);
  auto it = M.find(Code);
  if (it != M.end())
    return true;

  bool found = true;
  for (int i = r; i < R; ++i)
  {
    for (int j = c; j < C; ++j)
    {
      char e = ExactlyOne(G, r, c, i, j);
      if (e)
      {
        bool f1 = Recurse(r, j+1, R, C, G, M);
        bool f2 = Recurse(i+1, c, R, j+1, G, M);
        bool f3 = Recurse(i+1, c, R, C, G, M);
        bool f4 = Recurse(r, j+1, i+1, C, G, M);

        if (f1 && f2)
        {
          array<array<char, 25>, 25> A = G;
          for (int ii = r; ii <= i; ++ii) for (int jj = c; jj <= j; ++jj) A[ii][jj] = e;

          auto it = M.find(Encode(r, j+1, R, C));
          for (int ii = r; ii < R; ++ii) for (int jj = j+1; jj < C; ++jj) A[ii][jj] = (*it).second[ii][jj];

          auto jt = M.find(Encode(i+1, c, R, j+1));
          for (int ii = i+1; ii < R; ++ii) for (int jj = c; jj < j+1; ++jj) A[ii][jj] = (*jt).second[ii][jj];

          M[Code] = A;
          return true;
        }
        else if (f3 && f4)
        {
          array<array<char, 25>, 25> A = G;
          for (int ii = r; ii <= i; ++ii) for (int jj = c; jj <= j; ++jj) A[ii][jj] = e;

          auto it = M.find(Encode(i+1, c, R, C));
          for (int ii = i+1; ii < R; ++ii) for (int jj = c; jj < C; ++jj) A[ii][jj] = (*it).second[ii][jj];

          auto jt = M.find(Encode(r, j+1, i+1, C));
          for (int ii = r; ii < i+1; ++ii) for (int jj = j+1; jj < C; ++jj) A[ii][jj] = (*jt).second[ii][jj];

          M[Code] = A;
          return true;
        }
      }
    }
  }

  return false;
}

int main()
{
  int T; scanf("%d\n", &T);
  for (int ii = 1; ii <= T; ++ii)
  {
    int R, C;
    scanf("%d %d\n", &R, &C);
    array<array<char, 25>, 25> A;
    char G[30][30];
    for (int i = 0; i < R; ++i)
    {
      scanf("%s\n", G[i]);
      for (int j = 0; j < C; ++j) A[i][j] = G[i][j];
    }

    unordered_map<int, array<array<char, 25>, 25>> M;

    bool f = Recurse(0, 0, R, C, A, M);
    assert(f);
    printf("Case #%d:\n", ii);
    int Code = Encode(0, 0, R, C);
    for (int i = 0; i < R; ++i)
    {
      for (int j = 0; j < C; ++j) printf("%c", M[Code][i][j]);
      printf("\n");
    }
  }
}

