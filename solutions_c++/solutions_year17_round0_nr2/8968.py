#include <iostream>
#include <vector>
#include <algorithm>
#include <string.h>
#include <math.h>
#include <cmath>
#define FOR(i,f,c) for(int i=f;i<c;i++)
#define FORM(i,f,c) for(int i=f;i>c;i++)
using namespace std;
int main()
{
  int T;
  long long int N;
  cin >> T;
  FOR(t,1,T+1)
  {
  cin >> N;
  cout << "Case #" << t << ": ";
  long long int fans;
  FOR(j,1,N+1)
  {
    long long int k = j;
    int cj=0 ,ans=0;
    vector<long long int> cf;
    while(k > 0)
    {
      cf.push_back(k%10);
      k=k/10;
    }
    FOR(c,0,cf.size()-1)
    {
      if(cf[c] < cf[c+1])
      {
        ++ans;
      break;
    }
    }
    if(ans==0)
    {
    fans=j;
  }
    cf.clear();
  }
  cout << fans << endl;
}
  return 0;
}
