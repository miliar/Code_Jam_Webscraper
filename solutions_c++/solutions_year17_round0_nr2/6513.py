#include <iostream>
#include <algorithm>

using namespace std;

// int main()
// {
//   long long T, N, x, y;
//   cin >> T;
//   for (int nCase = 1; nCase <= T; nCase++) {
//     cin >> N;
//     string str = to_string(N);
//     while (!is_sorted(str.begin(), str.end())) {
//       N--;
//       str = to_string(N);
//     }
//     cout << "Case #" << nCase << ": " << str << endl;
//   }
//   return 0;
// }

string calc(string str)
{
  if (is_sorted(str.begin(), str.end()))
    return str;

  int i;
  for (i = 0; i < str.size() - 1; i++) {
    if (str[i] > str[i + 1])
      break;
  }

  char n = str[i];

  for (;;) {
    if (i != 0 && str[i - 1] == n)
      i--;
    else
      break;
  }

  str[i]--;

  for (i++; i < str.size(); i++)
    str[i] = '9';

  str.erase(0, min(str.find_first_not_of('0'), str.size()-1));

  return str;
}

int main()
{
  int T;
  string N;
  cin >> T;
  for (int nCase = 1; nCase <= T; nCase++) {
    cin >> N;
    cout << "Case #" << nCase << ": " << calc(N) << endl;
  }
  return 0;
}