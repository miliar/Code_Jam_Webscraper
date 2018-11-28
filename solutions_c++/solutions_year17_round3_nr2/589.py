#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <cstring>
#include <iomanip>
 
using namespace std;
static const double EPS = 1e-5;
typedef long long ll;
int main(){
  int n_case;
  cin >> n_case;
  for( int loop = 0 ; loop < n_case ; loop++ ){
    int Ac, Aj;
    cin >> Ac >> Aj;
    vector< pair<pair<int,int>,int> > infos;
    //vector< pair<int,int> > CD;
    //vector< pair<int,int> > JK;
    for( int i = 0 ; i <Ac; i++ ){
      int C,D;
      cin >> C >> D;
      infos.push_back(make_pair(make_pair(C,D),0));
      //CD.push_back( make_pair(C,D) );
    }
    for( int j = 0 ; j <Aj; j++ ){
      int J,K;
      cin >> J >> K;
      //JK.push_back( make_pair(J,K) );
      infos.push_back(make_pair(make_pair(J,K),1));
    }
    //sort(CD.begin());
    //sort(JK.begin());
    sort(infos.begin(), infos.end());
    if( infos.size() == 0 ){
      infos.push_back( make_pair(make_pair(0,100),1)) ;
    }
    int sum[2];
    bool flag = true;
    while(flag){
      int min_ind = -1;
      int min_flag = -1;
      int min_add = 2*24*60;
      flag = false;
      sum[0]=sum[1]=0;
      int size=infos.size();
      for( int i = 0 ; i < size; i++ ){
        int start = infos[i].first.first;
        int end = infos[i].first.second;
        if( end < start ) end += 24*60;
        sum[infos[i].second]+=end-start;
        int j = (i+1)%size;
        //cout << infos[i].second <<", "<< infos[j].second << endl;
        if( infos[i].second == infos[j].second ){
          int next_start = infos[j].first.first;
          if( end > next_start ) next_start += 24*60;
          int diff = next_start - end;
          if( min_add > diff ){
            min_ind = i;
            min_add = diff;
            min_flag = infos[i].second;
            flag = true;
          }
        }
      }
      if( flag ){
        vector< pair<pair<int,int>,int> > new_infos;
        if( min_add + sum[min_flag]<=12*60){
          for( int i = 0 ; i < size; i++ ){
            if( i == (min_ind+1)%size ){ continue; }
            else if( i== min_ind ){
              int j = (i+1)%size;
              new_infos.push_back( make_pair(make_pair(infos[i].first.first, infos[j].first.second), infos[i].second));
            }
            else{
              new_infos.push_back(infos[i]);
            }
          }
        }
        else{
          for( int i = 0 ; i < size; i++ ){
            new_infos.push_back(infos[i]);
            if( i == min_ind ){
              new_infos.push_back( make_pair(make_pair(infos[i].first.second, infos[i].first.second+1),1-infos[i].second));
            }
          }
        }
        infos=new_infos;
      }
      /*
      for(int i=0; i<infos.size(); i++ ){
        cout << infos[i].first.first <<"-" << infos[i].first.second << "..." << infos[i].second<<endl;
      }*/
    }
    int ans = max((int)infos.size(),2);
    cout << "Case #" << loop+1 << ": "<< ans<<endl;
  }
  return 0;
}

