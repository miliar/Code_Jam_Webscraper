#include<iostream>
using namespace std;

bool isTidyNumber(int n)
{
  bool itistidy=true;
  int prev=n%10;
  while(n)
  { 
    if(prev <  n%10)
    {
      itistidy= false;
      break;
    } 
    prev = n%10;
    n=n/10;   
  }

  return itistidy;
}

int nearestTidyNumber(int n)
{
  if(isTidyNumber(n))
    return n;
  
  for(int i=n ; i>0; --i)
  {
    if(isTidyNumber(i))
      return i;
  }
}

int main()
{
  int t, n;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> n ;  // read n.
    cout << "Case #" << i << ": " << nearestTidyNumber(n) << endl;
  }

}
