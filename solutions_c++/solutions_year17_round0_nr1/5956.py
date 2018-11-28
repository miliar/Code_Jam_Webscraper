#include <iostream>
#include <string>
#include <cassert>
#include <algorithm>
using namespace std;

bool all_plus(string c, int n)
{
  int range = min(n,int(c.length()));
  for (int i=0; i < range; i++)
  {
    if (c[i] != '+')  {return false;}
  }
  return true;
}

string flip(string c, int p, int f)
{
  assert(p + f - 1 <= c.size() - 1);

  //flip f bits ('-' and '+') starting from position p
  int range = min(p+f,int(c.length()));

  //cout << "fip(" << c <<") p: " << p << ", f: " << f << endl;
  for (int i=p; i < range; i++)
  {
    if (c[i] == '-')  {c[i] = '+';}
    else if (c[i] == '+')  {c[i] = '-';}
  }
  //cout << "newc: " << c << endl;
  return c;
}
int minFlip(string cakes, int n, int f)
{
  //return minimum flips to move cakes to "++++*"
  //if impossible, return a negative number 
  //only consider the first n characters of cakes
  //f is the number of consecutive cakes you have to flip

  //cout << "cakes: " << cakes << ", n: " << n << endl;

  assert(cakes.length() >= n);
 
  //base cases
  if (n < f)
  {
    //possible iff all are '+'
    if(all_plus(cakes, n))  {return 0;}
    else  {return -100000;}
  }

  if (cakes[n-1] == '+')
  {
    //ignore it
    return minFlip(cakes,n-1,f);
  }
  //otherwise flip it
  int p = n-f;
  cakes = flip(cakes,p,f);
  return 1+minFlip(cakes,n-1,f);
}

int tick(string c, int f)
{
  return minFlip(c, c.size(), f);
}

int main()
{
  int bigN;
  cin >> bigN;
  for (int i=1; i <= bigN; i++)
  {
    string c;
    cin >> c;
    int f;
    cin >> f;
    int answer = tick(c,f);
    cout << "Case #" << i << ": ";
    if (answer >= 0)  {cout << answer;}
    else  {cout << "IMPOSSIBLE";}
    cout << endl;
  }

  return 0;
}
