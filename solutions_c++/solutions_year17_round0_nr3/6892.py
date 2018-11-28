#include <bits/stdc++.h>
using namespace std;

pair<long long, long long> go (long long N, long long K){
    if(K == 1){
        if(N % 2) return make_pair((N-1)/2, (N-1)/2);
        else return make_pair(N/2, (N-1)/2);
    }
    if( N % 2){
        long long n = (N-1)/2;
        long long x = 1;
        while(x < K + 1) x <<= 1;
        x /= 2;
        assert(x <= K);
        if(K <  x + (x / 2) ){
            long long k = K - (x/2);
            return go(n, k);
        }
        else{
            long long k = K - x;
            return go(n,k);
        }
    }
    else{
        long long n = (N-2)/2;
        long long x = 1;
        while(x < K + 1) x <<= 1;
        x /= 2;
        assert(x <= K);
        if(K < x + (x/2)){
            long long k = K - (x/2);
            n++;
            return go(n,k);
        }
        else{
            long long k = K - x;
            return go(n,k);
        }
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    freopen("in", "r", stdin); freopen("out", "w", stdout);
    int t; cin >> t;
    for(int tt = 0 ; tt < t; ++tt){
        long long N; cin >> N;
        long long K; cin >> K;
        pair<long long, long long> ans = go(N,K), brute;
        bool filled[N];
        for(int i = 0 ; i < N; ++i){
            filled[i] = false;
        }
        for(int ii = 0 ; ii < K; ++ii){
            int last = -1, next = 0, maxmin = -1, maxmax = -1, idx = -1;
            while(!filled[next] && next < N) next++;
            for(int i = 0 ; i < N; ++i){
                if(!filled[i]){
                    int a = i - last - 1, b = next - i - 1;
                    if(maxmin < min(a,b)){
                        idx = i; maxmin = min(a,b); maxmax = max(a,b);
                    }
                    else if(maxmin == min(a,b) && maxmax < max(a,b)){
                        idx = i; maxmax = max(a,b);
                    }
                    else continue;
                }
                else{
                    last = i;
                    next++;
                    while(!filled[next] && next < N) next ++;
                }
            }
            filled[idx] = true;
            if(ii == K-1){
                brute = make_pair(maxmax, maxmin);
                if(ans != brute) cerr << tt + 1 << " " << ans.first << " " << ans.second << " " << brute.first << " " << brute.second << endl;
            }
        }
        cout << "Case #" << tt + 1 << ": " << brute.first << " " << brute.second << endl;
    }
    return 0;
}


