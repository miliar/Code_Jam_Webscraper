#include<bits/stdc++.h>
using namespace std;
char x[30][30];
void solve( int i , int j , int n , int m , int choice , char val){
    if( i < 0 || j < 0 || i >= n || j >= m  ) return;
    if(x[i][j] != '?')    return;
    x[i][j] = val;
    if(choice == 1){
    solve( i + 1 , j , n , m , choice , val);
    solve( i - 1 , j , n , m , choice , val);
    } else {
    solve( i  , j + 1, n , m , choice , val);
    solve( i  , j - 1, n , m , choice , val);
    }
}
int main(){
                  cin.sync_with_stdio(false);
                  ifstream cin("a.txt");
                  ofstream cout("b.txt");
                  int T , tt = 1;
                  cin >> T;
                  while(T--){
                      int n , m;
                      cin >> n >> m;
                      for(int i = 0 ; i < n;  ++i )
                       for(int j = 0 ; j < m ; ++j )
                         cin >> x[i][j];
                         for(int i = 0 ; i < n ; ++i ){
                           for(int j = 0 ; j < m ; ++j ){
                             if(x[i][j] != '?'){
                             char temp = x[i][j];
                             x[i][j] = '?';
                                solve(i , j , n , m , 1 , temp);
                                }
                             }
                            }
                        for(int i = 0 ; i < n ; ++i ){
                           for(int j = 0 ; j < m ; ++j ){
                             if(x[i][j] != '?'){
                             char temp = x[i][j];
                             x[i][j] = '?';
                                solve(i , j , n , m , 0 , temp);
                                }
                             }
                            }

                             cout << "Case #" << tt++ <<":" << endl;
                             for(int i = 0 ;i < n ; ++i ){
                              for(int j = 0 ; j < m ; ++j )
                              cout << x[i][j];
                              cout << endl;
                            }
                    }
    return 0;
}
