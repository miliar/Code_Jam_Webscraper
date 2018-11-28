#include <bits/stdc++.h>
using namespace std;
int n, c, m;
int person[1005], in[1005];
void solve(int Case) {
    cin >> n >> c >> m;
    int p, b;
    int mper = 0, r = 0;
    for (int i=0 ; i <= 1000; i++) {
        person[i] = 0;
        in[i] = 0;
    }

    for (int i = 0; i < m; i++) {
        cin >> p >> b;
        person[b]++;
        in[p]++;
        mper = max(mper, person[b]);
        r = max(r, in[p]);
    }

    r = max(r,mper);
    int mov = 0;
    //cout << "r = " << r << " mper = " << mper << "\n";
    while (r > mper) {
        //cout << r << "*\n";
        int smax = 0, posi;
        for (int i = 1; i <=n; i++) {
            if(in[i] > smax) {
                smax = in[i];
                posi = i;
            }
        }
        int smin = smax-1, posi2 = 0;
        for (int i = posi-1; i > 0; i--) {
            if(smin > in[i]) {
                smin = in[i];
                posi2 = i;
            }
        }
        if (posi2 == 0) break;
        in[posi]--;
        in[posi2]++;
        mov++;
        smax = 0;
        for (int i = 1; i <=n; i++) {
            smax = max(smax,in[i]);
        }
        r = smax;
    }

    cout << "Case #" << (Case+1) <<": ";
    printf("%d %d\n", r, mov);
}

int main () {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    cin >> T;
    for (int i=0;i<T;i++) solve(i);
}
