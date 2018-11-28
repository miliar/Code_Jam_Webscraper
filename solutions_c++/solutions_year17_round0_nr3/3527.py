#include <bits/stdc++.h>

using namespace std;

pair < long long, long long > solve(long long u){
    return make_pair(max(0LL, (u) / 2), max(0LL, (u - 1) / 2));
}

int main(){
    freopen("1.inp", "r", stdin);
    freopen("1.out", "w", stdout);
    int tt;
    scanf("%d", &tt);
  //  cout << answer << endl;
    for(int iTest = 1; iTest <= tt; ++iTest){
        long long n, k;
        cin >> n >> k;
        long long Firstmax = (n) / 2, Firstmin = (n - 1) / 2;
        long long Secondmax = 0, Secondmin = 0;
        long long Cntmax = 1, Cntmin = 0;
        cout << "Case #" << iTest << ": ";
        while(k > 0){
            if(Cntmax >= k){
                cout << Firstmax << " " << Firstmin << endl;
                break;
            }
            else{
                k -= Cntmax;
            }
            if(Cntmin >= k){
                cout << Secondmax << " " << Secondmin << endl;
                break;
            }
            else{
                k -= Cntmin;
            }
            long long newFirstmax = max(0LL, (Firstmax) / 2);
            long long newFirstmin = max(0LL, (Firstmax - 1) / 2);
            long long newCntmax = Cntmax;
            long long newSecondmax = 0, newSecondmin = 0, newCntmin = 0;
            pair < long long, long long > base = make_pair(newFirstmax, newFirstmin);
            if(solve(Firstmin) == base){
                newCntmax += Cntmax;
            }
            else{
                newSecondmax = solve(Firstmin).first;
                newSecondmin = solve(Firstmin).second;
                newCntmin = Cntmax;
            }
            if(Cntmin > 0 && solve(Secondmax) == base){
                newCntmax += Cntmin;
            }
            else if(Cntmin > 0){
                newSecondmax = solve(Secondmax).first;
                newSecondmin = solve(Secondmax).first;
                newCntmin += Cntmin;
            }
            if(Cntmin > 0 && solve(Secondmin) == base){
                newCntmax += Cntmin;
            }
            else if(Cntmin > 0){
                newSecondmax = solve(Secondmin).first;
                newSecondmin = solve(Secondmin).second;
                newCntmin += Cntmin;
            }
            Firstmax = newFirstmax;
            Firstmin = newFirstmin;
            Secondmax = newSecondmax;
            Secondmin = newSecondmin;
            Cntmax = newCntmax;
            Cntmin = newCntmin;
         //   break;
        }
    }
    return 0;
}
