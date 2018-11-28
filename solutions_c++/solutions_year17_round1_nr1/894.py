#include<iostream>
using namespace std;
const int MAXN = 100;
char tb[MAXN][MAXN];
int main()
{
  int T;
  cin >> T;
  for(int t = 0;t < T;t ++)
  {
    int R , C;
    cin >> R >> C;

    for(int i = 0;i < R;i ++)
      for(int j = 0;j < C;j ++)
        cin >> tb[i][j];

    for(int i = 0;i < R;i ++)
      for(int j = 0;j < C;j ++)
      {
        int pos = j - 1;
        while(pos >= 0 && tb[i][pos] == '?')
          tb[i][pos --] = tb[i][j];
        pos = j + 1;
        while(pos < C && tb[i][pos] == '?')
          tb[i][pos ++] = tb[i][j];
      }

    for(int i = 0;i < R;i ++)
      for(int j = 0;j < C;j ++)
      {
        int pos = i - 1;
        while(pos >= 0 && tb[pos][j] == '?')
          tb[pos --][j] = tb[i][j];
        pos = i + 1;
        while(pos < R && tb[pos][j] == '?')
          tb[pos ++][j] = tb[i][j];
      }
    cout << "Case #" << t + 1 << ":" << endl;
    for(int i = 0;i < R;i ++)
    {
      for(int j = 0;j < C;j ++)
        cout << tb[i][j];
      cout << endl;
    }
  }
  return 0;
}
