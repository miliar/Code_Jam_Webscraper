#include <bits/stdc++.h>

#define f(_i, _n) for (auto _i = 0; _i < _n; _i++)
#define F(_i, _k, _n) for (auto _i = _k; _i < _n; _i++)
#define fr(_i, _k, _n) for (auto _i = _k; _i < _n; _i++)
#define r(_t, _n)     _t _n;     cin >> _n;
#define ra(_type, _name, _len)_type _name[_len]; f(_i, _len)    cin >> _name[_len];
#define mp make_pair
#define re return
#define takedown re 0;
#define fi first
#define se second
#define in(_name) freopen(_name, "r", stdin);
#define out(_name) freopen(_name, "w", stdout);
#define err(_name) freopen(_name, "w", stderr);
//#ifdef FairlyLocal
    #define deb cerr
//#else
//    #define deb GetCE :(
//#endif
#define pb push_back
#define fill(_a, _n) memset(_a, _n, sizeof(_a))
#define all(_v) _v.begin(), _v.end()
#define vi std::vector<int>
using namespace std;
typedef pair<int,int> pii;
typedef long long ll;

#ifndef FairlyLocal
    // class fastio {
    // public:
    //     fastio() {
    //         ios::sync_with_stdio(false);
    //         cin.tie(nullptr);
    //     }
    // } __fastio;
#endif

string field[100];
int fxd[100][100];
void solve(int iii){
    int r, c;
    cin >> r >> c;
    f(i, r) cin >> field[i];
    f(i, r) f(j, c) fxd[i][j] = 0;
    deb << "CASE " << iii << endl;
    f(i, r) f(j, c){
        if(field[i][j] == '-' || field[i][j] == '|'){
            int notvert = 0, nothor = 0;
            for(int k = j-1; field[i][k]!='#' && k>=0; k--){
                if(field[i][k] == '-' || field[i][k] == '|'){
                    nothor = 1;
                    break;
                }
            }
            for(int k = j+1; field[i][k]!='#' && k < c; k++){
                if(field[i][k] == '-' || field[i][k] == '|'){
                    nothor = 1;
                    break;
                }
            }
            for(int k = i-1; field[k][j]!='#' && k>=0; k--){
                if(field[k][j] == '-' || field[k][j] == '|'){
                    notvert = 1;
                    break;
                }
            }
            for(int k = i+1; field[k][j]!='#' && k < r; k++){
                if(field[k][j] == '-' || field[k][j] == '|'){
                    notvert = 1;
                    break;
                }
            }
            if(notvert && nothor){
                cout << "Case #" << iii << ": " << "IMPOSSIBLE\n";
                re;
            }
            if(notvert || nothor) fxd[i][j] = 1;
            if(notvert) field[i][j] = '-';
            if(nothor) field[i][j] = '|';
        }
    }
    f(i, r){
        f(j, c){
            deb << fxd[i][j];
        }
        deb << endl;
    }
    f(kkk, 100000){
      int ch = 0;
      f(i, r) f(j, c){
//        deb << i << ' ' << j << ' ' << field[i][j] << ' ' << fxd[i][j] << endl;
        if(field[i][j] == '.' && !fxd[i][j]){
            int horpos, vertpos, h = 0, v = 0;
//            deb << i << ' ' << j << ' ' << v << ' ' << h << endl;
            for(int k = j-1; field[i][k]!='#' && k>=0; k--){
                if(field[i][k] == '-' || (!fxd[i][k] && field[i][k] == '|') ){
                    horpos = k;
                    h = 1;
                    break;
                }
            }
            for(int k = j+1; field[i][k]!='#' && k < c; k++){
                if(field[i][k] == '-' || (!fxd[i][k] && field[i][k] == '|') ){
                    horpos = k;
                    h = 1;
                    break;
                }
            }
            for(int k = i-1; field[k][j]!='#' && k>=0; k--){
                if(field[k][j] == '|' || (!fxd[k][j] && field[k][j] == '-')){
                    vertpos = k;
                    v = 1;
                    break;
                }
            }
            for(int k = i+1; field[k][j]!='#' && k < r; k++){
                if(field[k][j] == '|' || (!fxd[k][j] && field[k][j] == '-')){
                    vertpos = k;
                    v = 1;
                    break;
                }
            }
            if(!v && !h){
                cout << "Case #" << iii << ": " << "IMPOSSIBLE\n";
                re;
            }
            if(v^h){
                if(v){
                    fxd[vertpos][j] = 1;
                    field[vertpos][j] = '|';
                }
                else{
                    fxd[i][horpos] = 1;
                    field[i][horpos] = '-';
                }
                fxd[i][j] = 1;
                ch++;
            }
        }
      }
      if(!ch){
            cout << "Case #" << iii << ": " << "POSSIBLE\n";
            f(i, r){
                f(j, c){
                    if(field[i][j] == '-' && !fxd[i][j]) cout << '|';
                    else cout << field[i][j];
                }
                cout << '\n';
            }
            re;
        }
    }
    deb << "WTF" << endl;
}

int main(){
//    #ifdef FairlyLocal
        in(".input");
        out(".output");
        err(".debug");
//    #endif
    int t;
    cin >> t;
    f(i, t){
        solve(i+1);
    }
}
