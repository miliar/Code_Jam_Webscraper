#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <stack>
#include <queue>
#include <set>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <climits>
#include <cfloat>
#include <cstdlib>

using namespace std;

#define pb push_back
#define mp make_pair
#define fs first
#define sc second

#define ri(X) scanf("%d", &(X))
#define rii(X, Y) scanf("%d%d", &(X), &(Y))
#define riii(X, Y, Z) scanf("%d%d%d", &(X), &(Y), &(Z))
#define all(a) (a).begin(),(a).end()

#define INF 0x3f3f3f3f
#define INFL 0x3f3f3f3f3f3f3f3fLL

typedef pair<int,int> pii;
typedef vector<int> vi;
typedef long long ll;

int mod1 = int(1e9) + 7;

int main(){

    int t;
    ri(t);

    for(int cas=1; cas<=t; cas++) {

        ll n,k;
        cin >> n >> k;

        ll mmax,mmin;
        ll hc=1, lc=0, h=n;
        while(true) {
            ll m = 0;
            if(hc>=k) {
                m = h;
            } else if(hc+lc>=k) {
                m = h-1;
            }
            if(m) {
                if(m%2) {
                    mmax = mmin = (m-1)/2;
                } else {
                    mmax = m/2;
                    mmin = mmax-1;
                }
                break;
            }

            k -= (hc+lc);

            ll nhc=0, nlc=0;
            if(h%2) {
                h = (h-1) / 2;
                nhc = 2*hc;

                nlc += lc;
                nhc += lc;
            } else {
                h = h/2;
                nhc = nlc = hc;

                nlc += 2*lc;
            }
            hc = nhc;
            lc = nlc;
        }

        cout << "Case #" << cas << ": " << mmax << " " << mmin << endl;
        
    }

    return 0;
}
