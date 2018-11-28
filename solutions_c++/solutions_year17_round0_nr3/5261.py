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

int main(){
  int T;
  long long K, N;
  cin>>T;
  _f(tt,1,T+1){
    cin>>N>>K;
    
    vector< pair<long long,long long> > sets(1, make_pair(N, 1LL));
    _f(i, 1, K){
      //extract longest set
      pair<long long, long long> lset = sets.front();
      
      //reduce amount of current set
      if(lset.second > 1)
        sets[0].second--;
      else{
        pop_heap(sets.begin(), sets.end());
        sets.pop_back();
      }
      
      //if set is long enough
      if(lset.first > 1){
        //create new sets
        long long ls[2];
        ls[0] = lset.first / 2LL;
        ls[1] = (lset.first % 2LL) ? ls[0] : ls[0] - 1LL;
        bool inserted[2];
        fill_n(inserted, 2, false);
        
        //add new sets
        _f(j, 0, 2){
          if(ls[j] <= 0)
            continue;
            
          _fv(it, sets)
            if(it->first == ls[j]){
              it->second++;
              inserted[j] = true;
            }
          if(!inserted[j])
            sets.push_back(make_pair(ls[j], 1));
        }
        
        //reorder sets
        make_heap(sets.begin(), sets.end());
      }
    }
    
    //get longest set
    pair<long long, long long> lset = sets.front();
    long long ls[2];
    ls[0] = lset.first / 2LL;
    ls[1] = (lset.first % 2LL) ? ls[0] : ls[0] - 1LL;
  
    printf("Case #%d: %lld %lld\n",tt, ls[0], ls[1]);
  }
  
  return 0;
}

