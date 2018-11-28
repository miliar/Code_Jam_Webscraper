#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <queue>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
void max_min(int i, long long int n, long long int m)
{
      priority_queue<long long int>space;
      space.push(n);
      for(long long int i = 1; i<m ; i++)
      {
          n = space.top();
          space.pop();
          space.push(n/2);
          if(n % 2 == 0)
          {
              space.push((n/2) -1);
          }
          else
          {
              space.push(n/2);
          }
      }
      n = space.top();
      if(n % 2 == 0)
     	 cout << "Case #" << i << ": " << n/2 << " " << n/2 - 1 << endl;
      else
     	 cout << "Case #" << i << ": " << n/2 << " " << n/2 << endl;
        
}
int main() 
{
  int t, n, m;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> n >> m;  // read n and then m.
    max_min(i,n,m);
  }
  return 0;
}
 
