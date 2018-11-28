#include <iostream>
using namespace std;
typedef int ll;

#define A(x) cout << #x << ":" ; ppp(x, N);
#define D A(L); A(R); A(O); A(MIN); A(MAX);

void ppp(ll *x, ll N) {
    for(ll i=0;i<N;i++) {
        cout << x[i] << ",\t" ;
    }
    cout << endl;
}
void solve(ll t, ll N, ll K) {
    ll L[N];
    ll R[N];
    ll O[N];

    ll MIN[N];
    ll MAX[N];


    memset(L, 0, sizeof(L));
    memset(R, 0, sizeof(R));
    memset(O, 0, sizeof(O));
    memset(MIN, 0, sizeof(MIN));
    memset(MAX, 0, sizeof(MAX));

//D;

    for(ll i=0;i<K;i++) {
        

        ll x=1;
        for(ll i=0;i<N;i++) {
            if(O[i]) 
                x = 0;
            L[i] = x++;
        }

        x = 1;
        for(ll i=N-1;i>=0;i--) {
            if(O[i]) 
                x = 0;
            R[i] = x++;
        }

        for(ll i=0;i<N;i++) {

            MIN[i] = min(L[i], R[i]);
            MAX[i] = max(L[i], R[i]);
        }

        ll min_x = -1;
        ll max_x = -1;
        x = -1;
        
        for(ll i=0;i<N;i++) {
            ll min_cur = MIN[i];
            ll max_cur = MAX[i];
            if(min_cur > min_x) {
                x = i;
                min_x = min_cur;
                max_x = max_cur;
            } else if (min_cur == min_x) {
                if(max_cur > max_x) {
                    x = i;
                    min_x = min_cur;
                    max_x = max_cur;
                } 
            }
        }


        O[x] = 1;//set person
//D;
        if(i == K-1) {
            cout << "Case #" << t+1 << ": " << max_x-1 << " " << min_x-1 << endl; 
        }
    }
}

int main() {
    int T;

    cin >> T;
    for(int t=0;t<T;t++) {
        ll N,K;
        cin >> N >> K;
        solve(t, N,K);        
    }
}
