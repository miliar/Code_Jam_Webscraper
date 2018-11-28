#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main(int argc, char * argv[])
{
  string s, res;
  int nr_cases;
  cin >> nr_cases;

  for (int cas = 1; cas <= nr_cases; cas++)
  {
    long long N;
    cin >> N;
    s = to_string(N);
    int i = 1, j, l = s.size();
    while ((i < l) && (s[i-1] <= s[i])) i++;

    if (i < l)
    {
      j = i;
      while (s[i-1] > s[i])
      {
        s[i-1] = s[i-1] - 1;
        s[i] = '9';
        i--;
      }
      while (j < l)
        s[j++] = '9';
    }
    if (s[0] == '0') s.erase(0, 1);

    res = s;

    cout << "Case #" << cas << ": " << res << endl;
  }
}
