#include <bits/stdc++.h>
using namespace std;
#define R 1
#define Y 2
#define B 4
#define NO "IMPOSSIBLE"
const int BASE[] = {R, Y, B};
const string COLOR = "*RYOBVG*";

int n, a[10];

int getIdMax()
{
  int idMax = R;
  for (int i = 0; i < 3; i++)
    if (a[BASE[i]] > a[idMax])
      idMax = BASE[i];
  return idMax;
}

vector<int> solveLarge()
{
  int newN = 0;
  for (int i = 0; i < 3; i++)
  {
    int x = BASE[i];
    if (a[x ^ 7] && a[x ^ 7] >= a[x])
      return vector<int>();
    a[x] -= a[x ^ 7];
    newN += a[x];
  }

  int idMax = getIdMax();
  if (a[idMax] * 2 > newN)
    return vector<int>();

  vector <int> ans(newN);
  for (int i = 0, turn = 0; turn < newN; turn++)
  {
    ans[i] = idMax;
    if (!--a[idMax]) 
      idMax = getIdMax();
    if (i + 2 < newN) i += 2;
    else i = 1;
  }
  return ans;
}

int main()
{
  int test;
  cin >> test;
  for (int iTest = 1; iTest <= test; iTest++)
  {
    cerr << "Running test " << iTest << endl;
    cin >> n >> a[R] >> a[R + Y] >> a[Y] >> a[Y + B] >> a[B] >> a[B + R];
    
    cout << "Case #" << iTest << ": ";
    int done = 0;
    for (int i = 0; i < 3; i++)
    {
      int x = BASE[i];
      if (a[x] == a[x ^ 7] && a[x] + a[x ^ 7] == n)
      {
        while (a[x]--)
          cout << COLOR[x] << COLOR[x ^ 7];
        done = 1;
        break;
      }
    }

    if (!done)
    {
      vector<int> ans = solveLarge();
      if (ans.empty()) cout << NO;
      else 
      {
        for (auto x : ans)
        {
          cout << COLOR[x];
          while (a[x ^ 7])
          {
            cout << COLOR[x ^ 7] << COLOR[x];
            a[x ^ 7]--;
          }
        }
      }
    }
    cout << endl;
  }
}