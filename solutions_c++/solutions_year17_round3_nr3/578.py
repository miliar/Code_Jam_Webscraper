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
    int N,K;
    cin >> N >> K;
    double U;
    cin >> U;
    double P[N];
    for( int i = 0 ; i< N; i++ ){
      cin >> P[i];
    }
    sort(P, P+N);
    double totalAns = 0.0;
    totalAns = 1;
    while( U >= 1e-15 ){
      double minP = P[0];
      int cnt = 1;
      for( int i = 1 ; i < N; i++ ){
        if( P[i] == minP ) cnt++;
        else break;
      }
      double next = 1;
      if(cnt<N) next = P[cnt];
      //cout << next << endl;
      double diff = next-P[0];
      if( diff*cnt <= U ){
        U-=diff*cnt;
        for( int i = 0 ; i <cnt; i++ ){
          P[i]=next;
        }
      }
      else{
        for( int i = 0 ; i < cnt; i++ ){
          P[i] += U/cnt;
        }
        U=0;
      }
      /*
      for( int i = 0 ; i < N ; i++ ){
        cout << P[i]<<" ";
      }
      cout <<U << endl;
      */
    }
    for( int i = 0 ; i < N ; i++ ){
      //cout << P[i];
      totalAns *= P[i];
    }
    //cout << endl;
    /*
    for( int t = N; t >= 0; t-- ){
      for( int i = 0 ; i <N; i++ ){
        cout << P[i]  <<", ";
      }
      cout << "u:" << U <<endl;
      double right = 1.0;
      double left= 0.0;
      bool possible = true;
      for( int i = 0 ; i < 5000&& right-left < 1e-15; i++ ){
        double mid = (right+left)*0.5;
        double tmpU =U;
        for( int j = 0 ; j <N; j++ ){
          if( P[i] > mid ){
            break;
          }
          else{
            tmpU -= mid-P[j];
            if( tmpU < 0 ){
              possible = false;
              break;
            }
          }
        }
        if( possible ){
          left = mid;
        }
        else{
          right = mid;
        }    
      }
      cout << left << endl;
      double Ans = 1.0;
      for( int i = N-1; i >= 0; i-- ){
        if(P[i] < left ){
          Ans *= (left);
        }
        else{
          Ans *= (P[i]);
        }
      }
      totalAns = max(Ans, totalAns);
      cout << totalAns << endl;
      if(t>=1){
        U-=1-P[t-1];
        P[t-1] = 1;
      }
      if( U <= 0 ){
        P[t-1]+= U;
        U=0;
      }
    }*/
    cout << "Case #" << loop+1 << ": "<<fixed << setprecision(10) <<totalAns<<endl;
  }
  return 0;
}

