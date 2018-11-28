#include <bits/stdc++.h>

#define cin fin
#define cout fout

using namespace std;

ifstream fin("C-large.in");
ofstream fout("C-large.out");

typedef long long ll;

int T;
ll N, K;
ll pow2[70];

int main()
{
    cin >> T;

    pow2[0] = 1LL;
    for (int i=1; i<=69; i++)
        pow2[i] = pow2[i-1]+pow2[i-1];

    for (int caseno=1; caseno<=T; caseno ++) {
        cin >> N >> K;

        while (K > 1) {
            if (K%2 == 0) {
                N = N/2;
            } else {
                N = N-N/2-1;
            }
            K/=2;
        }

        cout << "Case #" << caseno << ": " << N/2 << " " << N-N/2-1 << endl;
    }

    return 0;
}
