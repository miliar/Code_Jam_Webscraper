#include<algorithm>
#include<cmath>
#include<iomanip>
#include<iostream>
#include<map>
#include<numeric>
#include<queue>
#include<set>
#include<sstream>
#include<vector>
using namespace std;
using uint = unsigned int;
using ll = long long;
const int M = 1e9 + 7;
const ll MLL = 1e18L + 9;
#pragma unused(M)
#pragma unused(MLL)
#ifdef LOCAL
#include"rprint.hpp"
#else
template <class... T> void printl(T&&...){ }
template <class... T> void printc(T&&...){ }
template <class... T> void prints(T&&...){ }
template <class... T> void printd(T&&...){ }
#endif

char cake[25][25];
void solve(char ini, int y, int x, int dy, int dx, int r, int c){
    if(y < 0 || r <= y || x < 0 || c <= x){ return; }
    if(cake[y][x] == '?'){
        cake[y][x] = ini;
    }else if(cake[y][x] != ini){
        return;
    }
    // prints(ini, y, x);
    solve(ini, y + dy, x + dx, dy, dx, r, c);
}

int main(){
    int t; cin >> t;
    for(int i=1;i<=t;i++){
        cout << "Case #" << i << ": " << '\n';
        int r, c;
        cin >> r >> c;
        for(int j=0;j<r;j++){
            for(int k=0;k<c;k++){
                cin >> cake[j][k];
            }
        }
        set<char> dones;
        for(int jj=0;jj<r*2;jj++){
            int j = jj < r ? jj : 2 * r - 1 - jj;
            int dir = jj < r ? -1 : 1;
            int x = 0;
            while(x < c && cake[j][x] == '?'){ x++; }
            if(x == c){
                if(j + dir < 0 || r <= j + dir){ continue; }
                for(int k=0;k<c;k++){
                    cake[j][k] = cake[j + dir][k];
                }
            }else{
                char ini = cake[j][x];
                int k = 0;
                while(k < c){
                    while(k < c && (cake[j][k] == '?' || cake[j][k] == ini)){
                        cake[j][k] = ini;
                        k++;
                    }
                    if(k == c){ break; }
                    ini = cake[j][k];
                }
            }
            // for(int k=0;k<c;k++){
            //     if(cake[j][k] != '?'){
            //         if(dones.count(cake[j][k])){ continue; }
            //         dones.insert(cake[j][k]);
            //         solve(cake[j][k], j, k, 1, 0, r, c);
            //         solve(cake[j][k], j, k, -1, 0, r, c);
            //         solve(cake[j][k], j, k, 0, 1, r, c);
            //         solve(cake[j][k], j, k, 0, -1, r, c);
            //     }
            // }
        }
        for(int j=0;j<r;j++){
            for(int k=0;k<c;k++){
                cout << cake[j][k];
            }
            cout << '\n';
        }
    }
    return 0;
}
