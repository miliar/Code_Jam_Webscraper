#include <iostream>
#include <string>

using namespace std;

string line;
int n, s, f;
bool pos;
int main()
{
  cin >> n;
  for (int x=0; x<n; x++)
  {
    f = 0;
    pos = true;
    cin >> line >> s;
    for (int i=0; i<line.length()-s+1; i++)
    {
      if (line[i] == '-')
      {
        line[i] = '+';
        for (int j=1; j<s; j++)
        {
          line[i+j] = line[i+j] == '+' ? '-' : '+';
        }
        f++;
      }
    }

    for (int i=0; i<line.length(); i++)
    {
      if (line[i] == '-') 
      {
        pos = false; 
        break;
      } 
    }

    if(pos)
      cout << "Case #" << x+1 << ": " << f << endl;
    else
      cout << "Case #" << x+1 << ": " << "IMPOSSIBLE" << endl;
  }
  return 0;
}