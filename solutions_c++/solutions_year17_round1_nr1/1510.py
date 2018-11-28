#include <bits/stdc++.h>
#define ll long long
#define mp make_pair
#define PI 3.1415926535897932384626433832
#define MOD 1000000007
#define MOD2 1000000009
#define bas 29
#define bas2 19

using namespace std;
int main()
{
    freopen("inn","r",stdin);
    freopen("out","w",stdout);
   int t ;
   cin>>t ;
   for(int u = 1 ; u <= t ; u++){
        int r , c ;
        cin>>r>>c ;
        char mat[r][c];
        for(int i = 0 ; i < r ; i++){
            for(int j = 0 ; j < c ; j++)cin>>mat[i][j];
        }

        for(int i = 0 ; i < r ; i++){
            for(int j = 0 ; j < c ; j++){
                if(i != 0){
                    if(mat[i][j] == '?'){
                        mat[i][j]=mat[i - 1][j];
                    }
                }

            }
        }
        for(int i = r - 1 ; i >= 0 ; i--){
            for(int j = 0 ; j < c ; j++){
                if(i != r - 1){
                    if(mat[i][j] == '?'){
                        mat[i][j]=mat[i + 1][j];
                    }
                }

            }
        }
        for(int i = r - 1 ; i >= 0 ; i--){
            for(int j = 0 ; j < c ; j++){
                if(j != 0){
                    if(mat[i][j] == '?'){
                        mat[i][j]=mat[i ][j - 1];
                    }
                }

            }
        }
        for(int i = r - 1 ; i >= 0 ; i--){
            for(int j = c - 1 ; j >= 0 ; j--){
                if(j != c - 1){
                    if(mat[i][j] == '?'){
                        mat[i][j]=mat[i ][j + 1];
                    }
                }

            }
        }
    cout<<"Case #"<<u<<":"<<endl;
    for(int i = 0 ; i < r ; i++){
        for(int j = 0 ; j < c ; j++)cout<<mat[i][j];
        cout<<endl;
    }
   }
}
