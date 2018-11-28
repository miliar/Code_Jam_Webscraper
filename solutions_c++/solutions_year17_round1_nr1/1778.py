#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define ff first
#define ss second

typedef long long int ll;
typedef vector< pair<int, int> > vii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<long long int> vll;
typedef pair<int, int> pii;

const ll INF = 1e18;
const int inf = 1e9;
const int MOD = 1e9 + 7;
const int nax = 1000000 + 10;

void fille(char arr[27][27], int row, int m)
{
    int flag = 0;
    for(int i = 1; i <= m; i++)
    {
        if(arr[row][i] == '?')
            flag = 1;
    }
    if(flag == 0)
        return;

    int endi = m;
    while(arr[row][endi] == '?' && endi > 0)
        endi --;

        if(endi == 0)
        {
            for(int i = 1; i <= m; i++)
                arr[row][i] = arr[row - 1][i];
            return;
        }

    for(int i = endi + 1; i <= m; i++)
        {
            if(arr[row][i] == '?')
            arr[row][i] = arr[row][i-1];
        }

    for(int i = endi - 1; i > 0; i--)
        {
            if(arr[row][i] == '?')
            arr[row][i] = arr[row][i+1];
        }
}
int main()
{
    ios::sync_with_stdio(0);

   freopen("input1.in", "r", stdin);
   freopen("output.txt", "w", stdout);

   int t;
   cin >> t;
   int test = 0;
   while(t--)
   {
       cout << "Case #" << ++test <<": "<< endl;
       int n, m;
       cin >> n >> m;

       char arr[27][27];
       int flag = 0;
       int start = -1;
       for(int i = 1; i <= n; i ++)
       {
           for(int j = 1; j <= m; j++)
           {
               cin >> arr[i][j];
               if(flag == 0)
               {
                   if(arr[i][j] != '?')
                   {
                       flag = 1;
                       start = i;
                   }
               }
           }
       }

      if(start == -1)
      {
          for(int i = 1; i <= n; i++)
          {
              for(int j = 1; j <= m; j++)
              {
                  cout << 'A';
              }
              cout << endl;
          }
          continue;
      }

      for(int i = start; i <= n; i++)
      {
          int flag = 0;
          for(int j = 1; j <= m; j++)
          {
              if(arr[i][j] != '?') flag = 1;
          }
          if(flag == 0)
          {
              for(int j = 1; j <= m; j++)
                arr[i][j] = arr[i-1][j];
              continue;
          }

          fille(arr, i, m);
      }

      for(int i = 1; i <= start; i++)
      {
          for(int j = 1; j <= m; j++)
            cout << arr[start][j];

            cout << endl;
      }
      for(int i = start + 1; i <= n; i++)
      {
          for(int j = 1; j <= m; j++)
          {
              cout << arr[i][j];
          }
          cout << endl;
      }
   }

    return 0;
}
