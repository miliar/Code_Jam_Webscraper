#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <queue>
#include <algorithm>
#include <string>
using namespace std;
#define MAX 110

int main() {
    //freopen("/Users/d/Documents/D-small-attempt4.in", "rt", stdin);
    //freopen("/Users/d/Documents/INPUT.TXT", "rt", stdin);
    int n;
    cin >> n;
    for(int i=1;i<=n;i++){
        vector<vector<char>> data(MAX, vector<char>(MAX, '.'));
        vector<vector<char>> add(MAX, vector<char>(MAX, '.'));
        int N, M;
        cin >> N >> M;
        char temp1;
        int x, y;
        int ox=-1, oy=-1;
        for(int i=0;i<M;i++){
            cin >> temp1 >> x >> y;
            data[x][y] = temp1;
            if(temp1=='x'||temp1=='o'){
                ox=x;
                oy=y;
            }
        }
        int cAdd=0;
        if(ox!=-1){
            if(data[ox][oy]=='x'){
                data[ox][oy]='o';
                add[ox][oy]='o';
                cAdd++;
            }
        } else {
            data[1][1]='o';
            add[1][1]='o';
            cAdd++;
            ox=oy=1;
//            for(int i=2;i<=N;i++){
//                if(data[1][i]=='.'){
//                    data[1][i]='+';
//                    add[1][i]='+';
//                    cAdd++;
//                }
//            }
        }
        for(int i=1;i<=N;i++){
            if(data[1][i]=='.'){
                data[1][i]='+';
                add[1][i]='+';
                cAdd++;
            }
        }
        for(int i=2;i<=N-1;i++){
            data[N][i]='+';
            add[N][i]='+';
            cAdd++;
        }
        int minus=0;
        if(oy<=2) {
            for(int i=1;i<=N-1;i++){
                int u, v;
                u=ox+i;
                v=oy+i;
                if(v>N){
                    v = v-N;
                }
                data[u][v]='x';
                add[u][v]='x';
                cAdd++;
            }
        } else if (oy >= N-1) {
            for(int i=1;i<=N-1;i++){
                int u, v;
                u=ox+i;
                v=oy-i;
                if(v<1){
                    v = v+N;
                }
                data[u][v]='x';
                add[u][v]='x';
                cAdd++;
            }
        } else {
            int u=0, v=0;
            for(int i=1;i<=N-1;i++){
                u=ox+i;
                v=oy+i;
                if(v>N){
                    v = v-N;
                }
                data[u][v]='x';
                add[u][v]='x';
                cAdd++;
            }
            data[u][v]='o';
            add[u][v]='o';
            cAdd--;
        }
        cout << "Case #" << i << ": ";
        if(N!=1){
            cout << N*3 - 2 << " " << cAdd << endl;
        } else {
            cout << 2 << " " << cAdd << endl;
        }
        for(int i=1;i<=N;i++){
            for(int j=1;j<=N;j++){
                if(add[i][j]!='.') {
                    cout << add[i][j] << " " << i << " " << j << endl;
                }
            }
        }
    }
    return 0;
}
