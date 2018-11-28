#include <iostream>
#include <string>
#include <vector>
#include <deque>
#include <map>
#include <algorithm>

using namespace std;

int get_prev_nr_flips(deque<int>& flips, int i, int k)
{
  while ((flips.size() > 0) && (i - flips.back() >= k))
    flips.pop_back();
  return flips.size();
}

int solve(vector<int>& vi, int k)
{
  int nr_flips, prev_nr_flips, res;
  int sz = vi.size();
  deque<int> flips;
  bool invalid = false;
  // left to right
  nr_flips = 0;
  for (int i = 0; i < sz; i++)
  {
    prev_nr_flips = get_prev_nr_flips(flips, i, k);
    if ((vi[i] + prev_nr_flips) % 2)
    {
      nr_flips++;
      if (i > sz - k) invalid = true;
      flips.push_front(i);
    }
  }

  if (invalid)
    res = -1;
  else
    res = nr_flips;

  return res;
}

void convert(string& s, vector<int>& vi)
{
  int l = s.size();
  vi.erase(vi.begin(),vi.end());
  for (int i=0; i < l; i++)
    if (s[i] == '+')
      vi.push_back(0);
    else
      vi.push_back(1);
}

int main(int argc, char * argv[])
{
  vector<int> vi;
  int nr_cases, res_ltr, res_rtl, res;
  cin >> nr_cases;

  for (int cas = 1; cas <= nr_cases; cas++)
  {
    string s;
    int k;
    cin >> s;
    cin >> k;
    convert(s, vi);
    res_ltr = solve(vi, k);
    reverse(vi.begin(), vi.end());
    res_rtl = solve(vi, k);
    if ((res_ltr >= 0) && (res_rtl >= 0))
      res = (res_ltr < res_rtl ? res_ltr : res_rtl);
    else
      res = (res_ltr < 0) ? res_rtl : res_ltr;

    if (res < 0)
      cout << "Case #" << cas << ": " << "IMPOSSIBLE" << endl;
    else
      cout << "Case #" << cas << ": " << res << endl;
  }
}
