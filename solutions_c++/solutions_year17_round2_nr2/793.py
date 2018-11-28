#include <iostream>
#include <vector>
#include <map>
#include <sstream>
#include <algorithm>
#include <unordered_map>

using namespace std;

string twochar(char a, char b, int n)
{
  string res;
  res.resize(2*n);
  for (int i = 0; i < n; i++)
  {
    res[2*i] = a;
    res[2*i+1] = b;
  }
  return res;
}

bool hasR(char c)
{
  return c == 'R' || c == 'O' || c == 'V';
}

bool hasY(char c)
{
  return c == 'Y' || c == 'O' || c == 'G';
}

bool hasB(char c)
{
  return c == 'B' || c == 'V' || c == 'G';
}


bool check(string solution)
{
  for (int i = 0; i < solution.size(); i++)
  {
    int j = i - 1;
    if (j < 0) j += solution.size();
    char a = solution[i];
    char b = solution[j];
    if (hasR(a) && hasR(b)) return false;
    if (hasY(a) && hasY(b)) return false;
    if (hasB(a) && hasB(b)) return false;
  }
  return true;
}

string solve3color(int B, int Y, int R, int N)
{
  vector<tuple<int, bool, char> > elements;
  elements.emplace_back(B, false, 'B');
  elements.emplace_back(Y, false, 'Y');
  elements.emplace_back(R, false, 'R');
  stringstream res;
  bool first = true;
  char prev = 0;
  while (true)
  {
    sort(elements.begin(), elements.end());
    if (get<0>(elements[2]) == 0) break;

    int I = 2;
    if (!first) {
      if (get<2>(elements[I]) == prev)
        I = 1;
    }
    else
    {
      first = false;
      get<1>(elements[2]) = true;
    }
    get<0>(elements[I])--;
    prev = get<2>(elements[I]);
    res << prev;
  }

  return res.str();
}

int main()
{
  int T;
  cin >> T;

  for (int i = 0; i < T; i++)
  {
    int N, R, O, Y, G, B, V;
    cin >> N >> R >> O >> Y >> G >> B >> V;

    string solution;
    if (O == B && O+B==N)
    {
      solution = twochar('O', 'B', O);
    }
    else if (Y == V && Y+V==N)
    {
      solution = twochar('Y', 'V', Y);
    }
    else if (R == G && R+G==N)
    {
      solution = twochar('R', 'G', R);
    }
    else if (O >= max(1, B) || V >= max(1, Y) || G >= max(1, R))
    {
      solution = "IMPOSSIBLE";
    }
    else
    {
      B -= O;
      Y -= V;
      R -= G;
      N -= O + V + G;
      if (N == 1 && (O+V+G>0))
      {
        solution = "IMPOSSIBLE";
      }
      else if (B > Y + R || Y > B + R || R > B + Y)
      {
        solution = "IMPOSSIBLE";
      }
      else
      {
        string s = solve3color(B, Y, R, N);
        stringstream ss;
        bool bO = false, bV = false, bG = false;
        for (char c : s) {
          ss << c;
          if (c == 'B' && !bO) {
            bO = true;
            ss << twochar('O', 'B', O);
          }
          if (c == 'Y' && !bV) {
            bV = true;
            ss << twochar('V', 'Y', V);
          }
          if (c == 'R' && !bG) {
            bG = true;
            ss << twochar('G', 'R', G);
          }
        }
        solution = ss.str();
      }
    }

    cout << "Case #" << i+1 << ": " << solution << endl;

    if (solution != "IMPOSSIBLE")
    {
      if (!check(solution))
      {
        cout << "Bad case" << endl;
        return 0;
      }
    }
  }

  return 0;
}
