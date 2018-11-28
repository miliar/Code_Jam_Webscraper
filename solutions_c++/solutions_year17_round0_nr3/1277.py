#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

void write(int n, pair<ll, ll> p){
   ofstream ofs;
   ofs.open ("out.txt", ios_base::app);
   // ofs << fixed << setprecision(6);
   ofs << "Case #" << n << ": " << p.first << " " << p.second << endl;
   ofs.close();
}

pair<ll, ll> solve(){
    ll N, K; cin >> N >> K;
    map<ll,ll> len_to_amount;
    set<ll> locs;
    locs.insert(N);
    len_to_amount[N] = 1;
    ll i = 0;
    while (1){
        ll cur = *locs.rbegin();
        auto it = locs.end(); it--; locs.erase(it);
        ll bigger = cur/2; ll smaller = (cur-1)/2;
        locs.insert(bigger);
        ll amount = len_to_amount[cur];
        len_to_amount[bigger] += amount;
        locs.insert(smaller);
        len_to_amount[smaller] += amount;
        i += amount;
        if (i >= K) return {bigger, smaller};
    }
}

int main(void){
   remove("out.txt");
   int T; cin >> T;
   for (int i = 1; i <= T; i++){
       write(i, solve());
   }
   return 0;
}
