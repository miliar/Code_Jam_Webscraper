#include <bits/stdc++.h>
using namespace std;
#define forn(i,n) for(int i=0 ;i < (int)(n); i++)
#define forni(i,n) for(int i=1 ;i <= (int)(n); i++)
#define dforn(i, n) for( tint i=(int) (n)-1 ;i >= 0; i--)
typedef long long tint;
const int MAXN=500100, inf=1e9;

int r, c;
char board[150][150], act;
bool fr;

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("Output_Problem_1.txt", "w", stdout);
    int t;
    cin >> t;
    forn(cs, t){
    //while(cin >> n){
        cout << "Case #" << cs+1 << ":\n";
        cin >> r >> c;
        forn(i, r)forn(j, c)cin >> board[i][j];
        bool fr = false;
        forn(i, r){
            bool is = false;
            forn(j, c)if(board[i][j]!='?'){
                is = true; fr = true;
                act = board[i][j];
                forn(k, j)board[i][j] = act;
                break;
            }
            if(is)forn(j, c){
                if(board[i][j]=='?')board[i][j]=act;
                act=board[i][j];
            }
            else{
                if(!fr)continue;
                forn(j, c)board[i][j] = board[i-1][j];
            }
        }
        dforn(i, r)if(board[i][0]=='?'){
            forn(j, c)board[i][j] = board[i+1][j];
        }
        forn(i, r){
            forn(j, c)cout << board[i][j]; cout << endl;
        }
    }
    return 0;
}

