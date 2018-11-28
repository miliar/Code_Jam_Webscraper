#include <bits/stdc++.h>

using namespace std;

int G[105];

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    freopen("A-small-attempt4.in","r",stdin);
    freopen("out1.txt","w",stdout);
    int T, N, P;
    cin >> T;
    for (int i = 1; i <= T; ++i){
        cout << "Case #" << i << ": ";
        cin >> N >> P;
        for (int j = 1; j <= N; ++j){
            cin >> G[j];
            G[j]%=P;
        }
        if (P == 2){
            int odd = 0;
            for (int j = 1; j <= N; ++j){
                odd += G[j];
            }
            cout << N - odd/2 << '\n';
        }
        else if (P == 3){
            int ones = 0, twos = 0;
            int exec = 0;
            for (int j = 1; j <= N; ++j){
                if (G[j] == 1) ones++;
                if (G[j] == 2) twos++;
            }
            exec = min(ones,twos);
            ones -= exec;
            twos -= exec;
            cout << N - exec - (ones/3)*2 - (twos/3)*2 - (ones%3==2) - (twos%3==2) << '\n';
        }
        else if (P == 4){

        }
    }
    return 0;
}
