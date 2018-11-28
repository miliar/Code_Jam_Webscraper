#include <bits/stdc++.h>
using namespace std;

typedef vector <int> vi;
typedef vector <vi> vvi;
typedef set <int> si;
typedef map <int, int> mii;
typedef vector <char> vc;
typedef vector <vc> vvc;
typedef pair <int, int> ii;
typedef vector <ii> vii;
typedef long long ll;
typedef long double ld;

vvc C;
vvi I;

int main(){
    int cas_t;
    cin >> cas_t;
    for(int cas=1; cas<=cas_t; cas++){
        int n, m;
        cin >> n >> m;
        C = vvc(n, vc(m));
        I = vvi(n, vi(m));
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++) cin >> C[i][j];
        }
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(C[i][j] != '?'){
                    bool h=0, t=0;
                    if(j+1<m) if(C[i][j+1] == C[i][j]) h=1;
                    if(j-1>=0) if(C[i][j-1] == C[i][j]) h=1;
                    if(i+1<n) if(C[i+1][j] == C[i][j]) t=1;
                    if(i-1>=0) if(C[i-1][j] == C[i][j]) t=1;

                    if(h and t) I[i][j] = 4;
                    else if(h) I[i][j] = 3;
                    else if(t) I[i][j] = 2;
                    else if(C[i][j] == '?')I[i][j] = 0;
                    else I[i][j] = 1;
                }
            }
        }
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(I[i][j] == 3){
                    for(int a = j+1; a<m; a++){
                        if(C[i][a]=='?') C[i][a] = C[i][j];
                        else if(C[i][a]!=C[i][j]) break;
                    }
                    for(int a = j-1; a>=0; a--){
                        if(C[i][a]=='?') C[i][a] = C[i][j];
                        else if(C[i][a] != C[i][j]) break;
                    }
                }

            }
        }
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(I[i][j] == 2){
                    for(int a = i+1; a<n; a++){
                        if(C[a][j]=='?') C[a][j] = C[i][j], I[a][j] = 1;
                        else if(C[a][j]!=C[i][j]) break;
                    }
                    for(int a = i-1; a>=0; a--){
                        if(C[a][j]=='?') C[a][j] = C[i][j], I[a][j] = 1;
                        else if(C[a][j]!=C[i][j]) break;
                    }
                }
            }
        }
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(I[i][j] == 1){
                    for(int a = j+1; a<m; a++){
                        if(C[i][a]=='?') C[i][a] = C[i][j], I[i][a] = 1;
                        else if(C[i][a]!=C[i][j]) break;
                    }
                    for(int a = j-1; a>=0; a--){
                        if(C[i][a]=='?') C[i][a] = C[i][j], I[i][a] = 1;
                        else if(C[i][a] != C[i][j]) break;
                    }

                }
            }
        }
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(I[i][j] == 1){
                    for(int a = i+1; a<n; a++){
                        if(C[a][j]=='?') C[a][j] = C[i][j], I[a][j] = 1;
                        else if(C[a][j]!=C[i][j]) break;
                    }
                    for(int a = i-1; a>=0; a--){
                        if(C[a][j]=='?') C[a][j] = C[i][j], I[a][j] = 1;
                        else if(C[a][j]!=C[i][j]) break;
                    }
                }
            }
        }
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(I[i][j] == 1){
                    for(int a = j+1; a<m; a++){
                        if(C[i][a]=='?') C[i][a] = C[i][j], I[i][a] = 1;
                        else if(C[i][a]!=C[i][j]) break;
                    }
                    for(int a = j-1; a>=0; a--){
                        if(C[i][a]=='?') C[i][a] = C[i][j], I[i][a] = 1;
                        else if(C[i][a] != C[i][j]) break;
                    }

                }
            }
        }
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(I[i][j] == 1){
                    for(int a = i+1; a<n; a++){
                        if(C[a][j]=='?') C[a][j] = C[i][j];
                        else if(C[a][j]!=C[i][j]) break;
                    }
                    for(int a = i-1; a>=0; a--){
                        if(C[a][j]=='?') C[a][j] = C[i][j];
                        else if(C[a][j]!=C[i][j]) break;
                    }
                }
            }
        }
    /*    for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(C[i][j] == '?'){
                    if(i+1<n) if(I[i+1][j] == 1) C[i][j] = C[i+1][j];
                    if(i-1>=0) if(I[i-1][j] == 1) C[i][j] = C[i-1][j];
                    if(j+1<m) if(I[i][j+1] == 1) C[i][j] = C[i][j+1];
                    if(j-1>=0) if(I[i][j-1] == 1) C[i][j] = C[i][j-1];

                }
            }
        } */


        cout << "Case #" << cas << ":" << endl;
        for(auto x : C){
            for(auto y : x) cout << y;
            cout << endl;
        }
    }
}
