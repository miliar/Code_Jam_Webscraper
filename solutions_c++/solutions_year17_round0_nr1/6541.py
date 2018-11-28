#include <iostream>

using namespace std;

bool row[1010];

int calc(string str, int k)
{
  int count = 0;
  int s = str.size();
  for (int i = 0; i < s; i++)
    row[i] = (str[i] == '+');

  int i;
  for (i = 0; i < s - k; i++) {
    if (row[i])
      continue;
    for (int j = 0; j < k; j++) {
      row[i + j] = !row[i + j];
    }
    count++;
  }

  bool f = row[i];
  for (; i < s; i++) {
    if (row[i] != f)
      return -1;
  }

  return f ? count : ++count;
}

int main()
{
  int t;
  cin >> t;
  for (int nCase = 1; nCase <= t; nCase++) {
    string str;
    int k;
    cin >> str >> k;
    int result = calc(str, k);
    cout << "Case #" << nCase << ": " <<
      ((result < 0) ? "IMPOSSIBLE" : to_string(result)) << endl;
  }
  return 0;
}