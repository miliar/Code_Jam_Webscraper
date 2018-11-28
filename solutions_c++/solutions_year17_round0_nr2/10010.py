#include <iostream>
using namespace std;

inline bool isTidy(unsigned long long N)
{
  int cur = N % 10;
  while(N > 0)
  {
    N /= 10;
    int next = N % 10;
    
    if(next > cur)
      return false;
    
    cur = next;
  }
  
  return true;
}


void solve()
{
  unsigned long long N; cin >> N;
  
  while(N > 0)
  {
    if(isTidy(N))
    {
      cout << N << endl;
      return;
    }
    N--;
  }
}

int main()
{ 
  int n; cin >> n;
  for(int i = 1; i <= n; i++)
  {
    cout << "Case #" << i << ": ";
    solve();
  }
}