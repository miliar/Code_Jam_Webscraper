#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
#include<queue>
#include<list>

using namespace std;



int main() 
{
  int t,j,i,m,k,ans;
  int n;
  string s; 
  cin>>t;
  for(m=1;m<=t;m++)
  {
    cin>>s>>k;
    n = s.size();
    ans = 0;
    for(i=0;i<=n-k;i++)
    {
      if(s[i]=='-')
      {
        for(j=i;j<i+k;j++)
        {
          if(s[j]=='-'){s[j] = '+';}
          else { s[j] = '-';}
        }
         ans++;
      }
     
    }
    bool done = false;
    for(i=0;i<n;i++){ if(s[i]=='-'){done = true;break;}}
    if(done) { cout<<"Case #"<<m<<": IMPOSSIBLE\n";}
    else {  cout<<"Case #"<<m<<": "<<ans<<"\n"; }

  }
  return 0;
	
}