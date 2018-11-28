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
    int R, C;
    cin >> R >> C;
    vector<vector<char>> S(R,vector<char>(C));
    for(int r=0;r<R;r++){
      string s;
      cin >> s;
      //cout << s.length() << endl;
      for(int c=0;c<C;c++){
        S[r][c]=s[c];
        //cerr<<S[r][c];
      }
      //cerr<<endl;
    }
    //return;

    int upper=0;
    for(int r=0;r<R;r++){ //current_row
      int left=0;
      char last='?';
      for(int c=0;c<C;c++){
         if(S[r][c]!='?'){
           last=S[r][c];
           for(int u=upper;u<=r;u++){
             for(int l=left;l<=c;l++){
               S[u][l]=last;
             }
           }
           left=c+1;
         }
      }
      if(left>0){
        for(int u=upper;u<=r;u++){
          for(int l=left;l<C;l++){
            S[u][l]=last;
          }
        }
        upper=r+1;
      }
    }
    for(int r=0;r<upper;r++){
        for(int c=0;c<C;c++){
          cout<<S[r][c];
        }
        cout<<endl;
    }
    for(int u=upper;u<R;u++){
        for(int c=0;c<C;c++){
          cout<<S[upper-1][c];
        }
      cout<<endl;
    }
}

int main(void){
    int T;
    cin>>T;
    for(int t=0;t<T;t++){
        printf("Case #%d: ", t+1);
        cout<<endl;
        main2();
    }
    return 0;
}
