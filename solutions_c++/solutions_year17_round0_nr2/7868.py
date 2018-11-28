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
  int t,j,i;
  long long n;
  cin>>t;
  for(j=1;j<=t;j++)
  {
    cin>>n;
    vector<int> v;
    while(n>0)
    {
      v.push_back(n%10);
      n/=10;
    }
    n = v.size();
    bool carry = false;
    for(i=0;i<n-1;i++)
    {
      if(v[i] < v[i+1])
      {
        for(int k =i;k>=0;k--)
        {
          v[k] = 9;
        }
        v[i+1] = (v[i+1]+10-1)%10;
      }
    }
    if(v[n-1]==0){v.pop_back();}
    reverse(v.begin(),v.end());
    string res = "";
    for(i = 0;i<v.size();i++)
    {
      res+=(char)(v[i]+'0');
    }
    cout<<"Case #"<<j<<": "<<res<<"\n";


  }
  return 0;
	
}