#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <unordered_map>
#include <algorithm>
#include <functional>
#include <utility>
#include <bitset>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>

using namespace std;

void main2(void){
    int N, P;
    cin >> N >> P;
    vector<int> R(N,0); //The i-th of these represents the number of grams of the i-th ingredient needed to make one serving of ratatouille.
    for(int n=0;n<N;n++)
        cin>>R[n];
//    vector<vector<int>> S(N,vector<int>(P,0));
    vector<vector<int>> Q(N,vector<int>(P));
    for(int n=0;n<N;n++){
      for(int p=0;p<P;p++){
        cin>>Q[n][p];
      }
      sort(Q[n].begin(),Q[n].end());
    }
    //cerr << Q[0][0] << endl;
    vector<int> I(N,0);
    vector<int> MAXS(N,0);
    vector<int> MINS(N,0);
    int res=0;
    while(true){
      int min_serv=INT_MIN;
      int max_serv=INT_MAX;
      int i_max_serv=0;
      for(int n=0;n<N;n++){
        MINS[n]=ceil(10.0*Q[n][I[n]]/(11.0*R[n]));
        MAXS[n]=floor(10.0*Q[n][I[n]]/(9.0*R[n]));
        min_serv=max(min_serv,MINS[n]);
        max_serv=min(max_serv,MAXS[n]);
      }
      if(min_serv<=max_serv){
         res++;
         // cerr << res << endl;
         bool to_break=false;
         for(int n=0;n<N;n++){
           I[n]++;
           //cerr << I[n] << endl;
           //cerr << P << endl;
           if(I[n]>=P){
             to_break=true;
             break;
           }
         }
         if(to_break) break;
      }else{
        bool to_break=false;
        for(int n=0;n<N;n++){
          if(MAXS[n]==max_serv){
            I[n]++;
            if(I[n]>=P){
              to_break=true;
              break;
            }
          }
        }
        if(to_break) break;
      }
    }
    cout << res << endl;
}

int main(void){
    int T;
    cin>>T;
    for(int t=0;t<T;t++){
        printf("Case #%d: ", t+1);
        main2();
    }
    return 0;
}
