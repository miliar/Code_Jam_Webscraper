#include <iostream>
#include <string>
#include <cmath>
#include <cstdio>
using namespace std;
#define MAX 1002
int pancake[MAX], lenPancake;
string s;

int movesFromSide(int idx, int cntItems, int increment, int k){
    int i, j, moves = 0;
    for(i = 0; i < lenPancake; i++)
        pancake[i] = ( s[i] == '+' ? 1 : 0 );

    while(cntItems--){
        if(!pancake[idx]){
            moves++;
            for(j = 0, i = idx; j < k; j++, i += increment)
                pancake[i] = !pancake[i];
        }
        idx += increment;
    }

    for(i = 0; i < lenPancake; i++)
        if(!pancake[i])
            return MAX;

    return moves;
}
void solve(){
    int T, t, K, ans;
    cin >> T;
    for(t = 1; t <= T; t++){
        cin >> s >> K;
        lenPancake = s.size();
        ans = min( movesFromSide(0, lenPancake - K + 1, 1, K), movesFromSide(lenPancake - 1, lenPancake - K + 1, -1, K) );
        if(ans == MAX)
            printf("Case #%d: IMPOSSIBLE\n", t);
        else
            printf("Case #%d: %d\n", t, ans);
    }
}

int main(){
    solve();
    return 0;
}
