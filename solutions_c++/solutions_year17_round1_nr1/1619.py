#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <bitset>
#include <cmath>
#include <numeric>
#include <iterator>
#include <iostream>
#include <cstdlib>
#include <functional>
#include <queue>
#include <stack>
#include <list>
#include <ctime>
#include <complex>
using namespace std;

typedef long long LL;

int R,C;
char mat[30][30];

void fillRow(int c) {
    if(c==C-1) return;
    if(mat[0][c+1] == '?' && c<C) fillRow(c+1);
    for(int i = 0 ; i < R ; i++ ) {
        mat[i][c] = mat[i][c+1];
    }
}

void solve(int cases) {
    scanf("%d%d",&R,&C);
    for(int i = 0 ; i < R ; i++ ) {
        scanf("%s",mat[i]);
    }
    for(int i = 0 ; i < C ; i++ ) {
        for(int j = 0 ; j < R ; j ++ ) {
            if(mat[j][i] != '?') {
                for(int k = j + 1 ; k < R ; k++) {
                    if(mat[k][i]!='?' && mat[k][i]!=mat[j][i])
                        break;
                    else mat[k][i] = mat[j][i];;
                }
                for(int k = j-1 ; k >= 0 ; k-- ) {
                    if(mat[k][i]!='?' && mat[k][i]!=mat[j][i])
                        break;
                    else mat[k][i] = mat[j][i];
                }
            }
        }
    }
    //for(int i = 0 ; i < R ; i++ ) printf("%s\n",mat[i]);
    for(int i = 0 ; i < C ; i++ ) {
        if(mat[0][i] == '?') {
            if(i==0){
                fillRow(i);
            } else {
                for(int j = 0 ; j < R ; j++ ) {
                    mat[j][i] = mat[j][i-1];
                }
            }
        }
    }
    printf("Case #%d:\n",cases);
    for(int i = 0 ; i < R ; i++ ) printf("%s\n",mat[i]);
}


int main() {
    int T;
    scanf("%d",&T);
    for(int i = 1 ; i<= T ; i++ ) {
        solve(i);
    }
    return 0;
}
