#include <bits/stdc++.h>

using namespace std;
#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, v) for(auto& a : v)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

ll big = 1000000007ll;
ll big2 = 1000000009ll;
ll n,m,q,T,k;

ll d;

ll per[6] = {0,3,1,5,2,4};
ll pal[3] = {5,4,3};
char CH[6] = {'R','Y','B','O','V','G'};

bool isblox[3] = {0};
ll F[6] = {0};

void solve(ll c4){

ll i = 0;
ll ma = -1;

for(ll c1 = 0; c1 < 3; c1++){
    if(F[c1] > ma){
        ma = F[c1];
        i = c1;
    }
}


if(2*ma > n){
    cout << "Case #" << c4+1 << ": IMPOSSIBLE\n";
}
else{

    vector<ll> ANS;
    ll n2 = F[0]+F[1]+F[2];
    ll prev = -1;
    if(c4 == 92){

        //cerr << F[0] << " " << F[1] << " " << F[2] << " - " << i << "\n";


    }
    for(ll c1 = 0; c1 < n2; c1++){

        if(prev == -1){
            ANS.push_back(i);
            F[i]--;
        }
        else{

            if(prev != i && F[i] > 0){
                ANS.push_back(i);
                F[i]--;
            }
            else{

                ll ni = 0;
                ll mni = -1;
                for(ll c2 = 0; c2 < 3; c2++){
                    if(F[c2] > mni && c2 != i){
                        mni = F[c2];
                        ni = c2;
                    }
                }
                ANS.push_back(ni);
                F[ni]--;
            }
        }
        prev = ANS[c1];
    }

    cout << "Case #" << c4+1 << ": ";
    prev = -1;
    for(ll c1 = 0; c1 < n2; c1++){

        cout << CH[ANS[c1]];
        if(ANS[c1] == prev)cerr << c4 << "\n";
        if(isblox[ANS[c1]]){
            for(ll c2 = 0; c2 < F[pal[ANS[c1]]]; c2++){
                cout << CH[pal[ANS[c1]]] << CH[ANS[c1]] ;
            }
            isblox[ANS[c1]] = 0;
        }
        prev = ANS[c1];
    }
    if(ANS[0] == prev)cerr << c4 << " " << ma << "\n";
    cout << "\n";
}

}


int main()
{
    freopen("input.txt","r",stdin);
    freopen("autput.txt","w",stdout);

    ll a,b,c;

    cin >> T;

    for(ll c4 = 0; c4 < T; c4++){

        for(ll c1 = 0; c1 < 6; c1++){
            F[c1] = 0;
        }
        bool yes1 = 1;
        cin >> n;

        isblox[0] = 0;
        isblox[1] = 0;
        isblox[2] = 0;


        for(ll c1 = 0; c1 < 6; c1++){
            cin >> a;
            F[per[c1]] = a;
        }

        for(ll c1 = 0; c1 < 3; c1++){
            if(F[pal[c1]] > 0){
                isblox[c1] = 1;
                F[c1] -= F[pal[c1]];
                if(F[c1] < 0)yes1 = 0;
            }
        }

        if(!yes1){
            cout << "Case #" << c4+1 << ": IMPOSSIBLE\n";
        }
        else{

            solve(c4);
        }

    }

    return 0;
}
