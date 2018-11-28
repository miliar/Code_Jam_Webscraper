#include <bits/stdc++.h>
using namespace std;
int Solve(){
    int N, P;
    scanf("%d%d", &N, &P);
    vector<int> vc(P);
    for(int i = 0 ; i < N ; i++){
        int x;
        scanf("%d", &x);
        x %= P;
        vc[x]++;
    }
    int ans = 0;
    if(P == 2){
        ans += (vc[1] + 1) / 2;
    }else if(P == 3){
        int t = min(vc[1], vc[2]);
        int t1 = vc[1] - t, t2 = vc[2] - t;
        int ans1 = t + (t1 + 2) / 3 + (t2 + 2) / 3;
        int ans2 = (vc[1] + 2) / 3 + (vc[2] + 2) / 3;
        ans = max(ans1, ans2);
    }else if(P == 4){
    }
    return ans + vc[0];
}
int main(){
    int T;
    scanf("%d", &T);
    for(int i = 1 ; i <= T ; i++)
        printf("Case #%d: %d\n", i, Solve());
    return 0;
}
