#include<bits/stc++.h>
using namespace std;
int main(){
             cin.sync_with_stdio(false);
             int T;
             cin >> T;
             while(T--){
                      int N , P;
                      cin >> N >> P;
                      long long in[N];
                      for(int i = 0 ; i < N ; ++i  )
                        cin >> in[i];

                      long long x[P][P];
                      for(int i = 0 ; i < N ; ++i )
                        for(int j = 0 ; j < P ; ++j )
                          cin >> x[i][j];

                          if(N == 1){
                            int res = 0;
                            for(int i = 0 ; i < P ; ++i ){
                              long long I = x[0][i];
                              long long Max =  floor( (in[0] * 1.0 * 10)/(9 * I));
                              long long Min = ceil((in[0] * 1.0 * 10)/(11 * I));
                              cout << Min <<" "<< Max << endl;
                              if(Min <= Max && Min > 0)
                              ++res;
                            }
                          }




             }
}
