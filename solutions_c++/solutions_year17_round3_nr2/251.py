#include <bits/stdc++.h>

using namespace std;

vector<bool>    J,
                C;
vector<vector<vector<int> > >   mem,
                                mem2;

int solve(int j, int c, bool jside){
    if(j > 720 || c > 720) return (1<<30);
    if(j == 720 && c == 720) {
        //return jside ? 0 : 1;
        return 0;
    }
    int t = j + c;
    if(jside && J[t] || !jside && C[t]) {
        mem[j][c][jside] = (1<<30);
        return mem[j][c][jside];
    }
    if(mem[j][c][jside] != -1) return mem[j][c][jside];

    if(jside){
        mem[j][c][jside] = min(solve(j+1,c,true), solve(j,c+1,false) + 1);
    } else {
        mem[j][c][jside] = min(solve(j+1,c,true) + 1, solve(j,c+1,false));
    }
//    cout << j << " " << c << " " << jside << " " << mem[j][c][jside] << endl;
    return mem[j][c][jside];
}

int solve2(int j, int c, bool jside){
    if(j > 720 || c > 720) return (1<<30);
    if(j == 720 && c == 720) {
//        return jside ? 1 : 0;
        return 0;
    }
    int t = j + c;
    if(jside && J[t] || !jside && C[t]) {
        mem2[j][c][jside] = (1<<30);
        return mem2[j][c][jside];
    }
    if(mem2[j][c][jside] != -1) return mem2[j][c][jside];

    if(jside){
        mem2[j][c][jside] = min(solve(j+1,c,true), solve(j,c+1,false) + 1);
    } else {
        mem2[j][c][jside] = min(solve(j+1,c,true) + 1, solve(j,c+1,false));
    }
    return mem2[j][c][jside];
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("outlarge.txt","w",stdout);

    ios::sync_with_stdio(false); cin.tie(0);
    int T, cnt = 0;
    cin >> T;
    while(T--){
        cnt++;
        int Ac, Aj;
        cin >> Ac >> Aj;
        J.assign(1441, false);
        C.assign(1441, false);
        mem.assign(721, vector<vector<int> > (721, vector<int> (2,-1)));
        mem2.assign(721, vector<vector<int> > (721, vector<int> (2,-1)));
        for(int i = 0; i < Ac; i++){
            int c, d;
            cin >> c >> d;
            for(int j = c; j < d; j++){
                C[j] = true;
            }
        }
        for(int i = 0; i < Aj; i++){
            int c, d;
            cin >> c >> d;
            for(int j = c; j < d; j++){
                J[j] = true;
            }
        }

        cout << "Case #" << cnt << ": ";
        int ans = (1<<30);
        ans = min(ans,solve(0,0,true));
        ans = min(ans,solve2(0,0,false));
        if(mem[0][0][0] != -1) ans = min(ans,mem[0][0][0]);
        if(mem2[0][0][1] != -1) ans = min(ans,mem2[0][0][1]);
        if(ans % 2 != 0) ans++;
        cout << ans << endl;
    }
    return 0;
}

