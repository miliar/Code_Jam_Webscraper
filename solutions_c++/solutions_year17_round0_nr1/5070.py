#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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

using namespace std;

#define _f(i,x,n) for(int i=x;i<n;i++)
#define _if(i,x,n) for(int i=(n);i>=x;i--)
#define _fv(it,v) for(typeof((v).begin()) it=(v).begin(); it!=(v).end(); it++)

#define _dv(var) cout<<"L"<<__LINE__<<": "<<#var<<": "<<var<<endl;
#define _dav(i,f) cout<<"L"<<__LINE__<<": "<<#i<<"-"<<#f<<": "; dav(i,f);
template<typename it> void dav(it i,it f)
	{ cout<<"[ "; while(i!=f) cout<<*(i++)	<<" "; cout<<"]"<<endl; }
#define _ln cout<<"_ln: "<<__LINE__<<endl;

string S;

bool checkPancakes(int j, int e_plus, int e_minus){
  //check -
  for(int i = 0; i < e_plus; i++, j++){
    if(S.length() <= j || '-' == S[j])
      return false;
  }
  //check +
  for(int i = 0; i < e_minus; i++, j++){
    if(S.length() <= j || '+' == S[j])
      return false;
  }
  
  return true;
}

int main(){
  int T, K, i, j;
  cin>>T;
  _f(tt,1,T+1){
    cin>>S>>K;
    int r = 0;
    
    _f(i, 0, S.length())
      if('-' == S[i]){
        //check flip is possible
        if(i + K > S.length()){
          r = -1;
          break;
        }
        
        //flip
        _f(j, 0, K)
          S[i + j] = '-' == S[i + j] ? '+' : '-';
          
        r++;
      }
    
    if(r == -1)
      printf("Case #%d: IMPOSSIBLE\n",tt);
    else
      printf("Case #%d: %d\n",tt,r);
  }
  
  return 0;
}

