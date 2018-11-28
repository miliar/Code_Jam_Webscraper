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

/* convertir datos */
template<class Origen,class Destino> Destino convertir(Origen entrada)
	{ stringstream flujo; flujo<<entrada; Destino salida; flujo>>salida; return salida; }

int main(){
  int T;
  cin>>T;
  _f(tt,1,T+1){
    string N;
    cin>>N;
    
    _if(i, 1, N.length() - 1){
      //_dv(N)
      if(N[i - 1] > N[i]){
        //_dv(i)
        N[i - 1] = N[i - 1] - 1;
        fill(N.begin() + i, N.end(), '9');
      }
    }
    //_dv(N)
  
    unsigned long long L = convertir<string,unsigned long long>(N);
    printf("Case #%d: %llu\n",tt, L);
  }
  
  return 0;
}

