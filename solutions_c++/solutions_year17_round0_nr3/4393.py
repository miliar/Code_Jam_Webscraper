#include <iostream>
#include <queue>
#include <cmath>
using namespace std;

void solve(const int & N, const int & K, int & y, int & z)
{
  int counter = 1;
  int space, newspace;
  priority_queue<int> q;
  q.push(N);
  while(true)
  {
    space = q.top();
    q.pop();
    if(K == counter)
    {
      if(space % 2 == 0)
      {
        y = space / 2;
        z = y - 1;
      }
      else
      {
        y = (space - 1) / 2;
        z = y;
      }
      break;
    }
    if(space % 2 == 0)
    {
      newspace = space / 2;
      if(newspace > 0)
        q.push(newspace);
      newspace -= 1;
      if(newspace > 0)
        q.push(newspace);
    }
    else
    {
      newspace = (space - 1) / 2;
      if(newspace > 0)
      {
        q.push(newspace);
        q.push(newspace);
      }
    }
    counter++;
  }
}

int main()
{
  int T, N, K, y, z;
  
  cin >> T;
  for(int i = 1; i <= T; i++)
  {
    cin >> N >> K;
    solve(N, K, y, z);
    cout << "Case #" << i << ": " << y << " " << z << endl;
  }
  return 0;
}