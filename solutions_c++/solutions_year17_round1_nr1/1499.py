#include <iostream>
#include <string>
#include <vector>

using namespace std;
int main()
{
  int N; cin >> N;
  for (int ii = 1; ii <= N; ii++)
  {
    int r, c; cin >> r >> c;
    vector<string> data(r); 
    for (int i = 0; i < r; i++)
    {
      cin >> data[i]; 
    }
    
    int current = -1;  
    for (int i = 0; i < r; i++)
    {
      char last = 0;
      for (int k = 0; k < c; k++)
      {
        if (data[i][k] != '?')
        {
          if (! last)
          {  
            for (int j = 0; j < k; j++)
            {
              data[i][j] = data[i][k];
            }
          }  
          last = data[i][k];
        }
        else
        {
          data[i][k] = last;
        }
      }
      if (! last)
      {
        if (current >= 0)
        {
          data[i] = data[current];
        }
      }
      else
      {
        if (current < 0)
        {
          for (int j = 0; j < i; j++)
          {
            data[j] = data[i];
          }  
        }
        current = i;
      }
    }
    
    cout << "Case #" << ii << ":" << endl;
    for (int i = 0; i < r; i++)
    {
      cout << data[i] << endl;
    }  
  }
  return 0;
}