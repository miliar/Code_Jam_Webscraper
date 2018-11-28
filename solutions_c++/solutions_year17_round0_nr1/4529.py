#include <iostream>
#include <string>
#include <unordered_set>

using namespace std;

char flip(char c)
{
  return c == '-' ? '+' : '-';
}

int main()
{
  int n;

  cin >> n >> ws;
  for (int i = 0; i < n; i++)
  {
    int size = 0, num = 0;
    string row;
    cin >> row >> ws >> size;

    bool flipped = true;
    while (flipped)
    {
      flipped = false;

      for (int k = 0; k + size <= row.size(); k++)
      {
        if(row[k]=='-'){
          flipped=true;
          num++;
          for(int y=0; y<size; y++){
            row[k+y]=flip(row[k+y]);
          }
        }
      }
    }

    bool impossible = false;

    for (int p = 0; p < row.size(); p++)
    {
      if (row[p] == '-')
        impossible = true;
    }

    if (impossible)
      cout << "Case #" << i + 1 << ": "
           << "IMPOSSIBLE" << endl;
    else
      cout << "Case #" << i + 1 << ": " << num << endl;
  }

  return 0;
}