#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main()
{
  int N; cin >> N;
  for (int ii = 1; ii <= N; ii++)
  {
    int n, p; cin >> n >> p;
    vector<int> data(n); 
    for (int i = 0; i < n; i++)
    {
      cin >> data[i]; 
    }
    
    int result = 0;
    vector<int> rest(p, 0);    
    for (int i = 0; i < n; i++)
    {
      rest[data[i]%p] ++;
    }
    
    switch(p) {
    case 2:
      result = n - rest[1]/2;
      break;
      
    case 3:
      {
        int x = min(rest[1], rest[2]);
        int y = max(rest[1], rest[2]) - x;
        //cout << x << ":" << y << ":" << ":" << (y - (y-1)/3 - 1) << endl;
        result = n - x;
        if (y > 0) result -= y - (y-1)/3 - 1;
      }  
      break;
    }  
    
    cout << "Case #" << ii << ": " << result << endl;
  }
  return 0;
}