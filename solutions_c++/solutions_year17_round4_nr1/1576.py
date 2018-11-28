#include <bits/stdc++.h>
#define ff first
#define ss second
#define mp make_pair
#define var(x) cerr << #x << " = " << x << endl;

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

int v[9];

int main() {
    int N;
    cin >> N;
    for(int t=1;t<=N;t++) {
        int n, p, g, r=1;
        cin >> n >> p;
        memset(v,0,sizeof(v));
        for(int i=0;i<n;i++) {
            cin >> g;
            v[g%p]++;
        }
        if(v[0] < n) {
            r += v[0];
            n -= v[0];
        }
        if(p == 2) {
            r += (v[1]-1)/2;
            n -= v[1];
        } else if(p == 3) {
            int  k = min(v[1],v[2]);
            r += k;
            n -= 2*k;
            v[1] -= k;
            v[2] -= k;
            if(n == 0) r--;
            else {
                if(v[1] > 0) r += (v[1]-1)/3;
                if(v[2] > 0) r += (v[2]-1)/3;
            }
        } else if(p == 4) {
        }
        printf("Case #%d: %d", t, r);
        cout << endl;
    }
    return 0;
}

