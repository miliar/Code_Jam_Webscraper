#include <iostream>
#include <string>

using namespace std;

int main()
{
  int T;
  cin >> T;
  string pancakes;
  int K;
  for (int t = 1; t <= T; ++t)
  {
    // TODO special case K == 1
    getline(cin, pancakes, ' ');
    cin >> K;
    cin.ignore();
    unsigned long long steps = 0;
    size_t first_minus = pancakes.find('-');
    if (first_minus == string::npos)
    {
      cout << "Case #" << t << ": " << 0 << endl;
      continue;
    }
    bool impossible = false;
    while (first_minus != string::npos)
    {
      if (pancakes.length() - first_minus < K)
      {
        impossible = true;
        break;
      }
      steps++;
      for (int i = first_minus, k = 0; k < K; i++, k++)
      {
        pancakes[i] = (pancakes[i] == '-') ? '+' : '-';
      }
      first_minus = pancakes.find('-', first_minus);
    }
    if (impossible)
      cout << "Case #" << t << ": IMPOSSIBLE" << endl;
    else
      cout << "Case #" << t << ": " << steps << endl;
  }
  return 0;
}
