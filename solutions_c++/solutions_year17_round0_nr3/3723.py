#include <bits/stdc++.h>
#define int long long

using namespace std;

int const N = 105;
int Pow[N], a[N];

int CALC(int n, int type){
    if(type == 0) return max(0ll, (n - 1) - (n - 1) / 2);
    return max(0ll, (n - 1) / 2);
}

void Solve(int n, int k){
    int Num = k, cnt = 0;
    for(int i=60; i>=2; i--){
        if(k < Pow[i-1])  continue;
        k = k - Pow[i-1] + 1;
        if(k <= (Pow[i-2])){
            Num = Pow[i-1] - 1 + 2 * k - 1;
        }
        else{
            k -= Pow[i-2];
            Num = Pow[i-1] - 1 + 2 * k;
        }
        break;
    }
    while(Num > 1){
        a[++cnt] = Num % 2;
        Num /= 2;
    }
    reverse(a+1, a+cnt+1);
    for(int i=1; i<=cnt; i++)
        n = CALC(n, a[i]);
    cout << CALC(n, 0) << " " << CALC(n, 1) << endl;
}

void Solve2(int n, int k){
    priority_queue < int > que;
    while(!que.empty()) que.pop();
    que.push(n);
    for(int i=1; i<k; i++){
        int u = que.top(); que.pop();
        que.push(CALC(u, 0));
        que.push(CALC(u, 1));
    }
    int u = que.top();
    cout << CALC(u, 0) << " " << CALC(u, 1) << endl;
}

main()
{
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T, n, k;
    cin >> T;
    Pow[0] = 1;
    for(int i=1; i<=60; i++)
        Pow[i] = Pow[i-1] * 2;
    for(int _=1; _<=T; _++){
        cout << "Case #" << _ << ": ";
        cin >> n >> k;
        //Solve(n, k);
        Solve2(n, k);
    }
}
