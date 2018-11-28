#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
using namespace std;
struct S{
    int st, ed, p;
}data[220];
bool cmp(S a, S b){
    return a.st < b.st;
}
int n0, n1, dc;
int ans;


void DFS(int now, int t0, int t1, int st, int last, int step){
    if(step >= ans) return;
    if(t0 > 720 || t1 > 720) return;
    if(now == dc){
        int mod= 0;
        if(st != last) mod++;
        if(step + mod < ans){
            ans = step + mod;
        }
        return;
    }
    int n0 = t0, n1 = t1, nstep = step;
    
    int np = 1 - data[now].p;

    if(np == 0){
        n0 += data[now].ed - data[now].st;
    }else{
        n1 += data[now].ed - data[now].st;
    }
    if(last != np){
        nstep++;
    }

    int nxt = data[now + 1].st - data[now].ed;
    
    if(np == 0){
        DFS(now + 1, n0 + nxt, n1, st, 0, nstep);
        for(int i = 0; i < nxt; i++){
            DFS(now + 1, n0 + i, n1 + (nxt - i), st, 1, nstep + 1);
        }
    }else{
        DFS(now + 1, n0, n1 + nxt, st, 1, nstep);
        for(int i = 0; i < nxt; i++){
            DFS(now + 1, n0 + (nxt - i), n1 + i, st, 0, nstep + 1);
        }
    }
}



int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int T;
    cin >> T;
    
    for(int f = 1; f <= T; f++){
        cin >> n0 >> n1;
        dc = 0;
        for(int i = 0; i < n0; i++){
            cin >> data[dc].st >> data[dc].ed;
            data[dc++].p = 0;
        }
        for(int i = 0; i < n1; i++){
            cin >> data[dc].st >> data[dc].ed;
            data[dc++].p = 1;
        }
        sort(data, data + dc, cmp);
        data[dc].st = 1440;

        ans = 2147483647;

        DFS(0, data[0].st, 0, 0, 0, 0);
        DFS(0, 0, data[0].st, 1, 1, 0);
        for(int i = 1; i < data[0].st; i++){
            DFS(0, i, data[0].st - i, 0, 1, 1);
            DFS(0, data[0].st - i, i, 1, 0, 1);
        }


        cout << "Case #" << f << ": " << ans << endl;
    }

    return 0;
}
