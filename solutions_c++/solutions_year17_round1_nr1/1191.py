#include <bits/stdc++.h>
#define F(n) Fi(i,n)
#define Fi(i,n) Fl(i,0,n)
#define Fl(i,l,n) for(int i=l;i<n;i++)
using namespace std;
const int N = 27;
char D[N][N];
main(){
    // ios_base::sync_with_stdio(false);
    // cin.tie(0);
    int t,n,m;
    cin>>t;
    Fi(cas, t){
        cin>>n>>m;
        F(n){
            Fi(j,m){
                cin>>D[i][j];
                if(j && D[i][j] == '?')D[i][j] = D[i][j-1];
            }
            Fi(j,m){
                if(j && D[i][m-1-j] == '?')D[i][m-1-j] = D[i][m-j];
            }
        }
        F(n)if(i && D[i][0] == '?'){
            strncpy(D[i],D[i-1],m);
        }
        F(n)if(i && D[n-1-i][0] == '?'){
            strncpy(D[n-1-i],D[n-i],m);
        }
        cout<<"Case #"<<cas+1<<":\n";
        F(n){
            Fi(j,m)cout<<D[i][j];
            cout<<'\n';
        }
        cout<<flush;
    }
}