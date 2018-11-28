/* Author : Jordhy Fernando */
#include<bits/stdc++.h>
#define ll long long
#define For(i,j,n) for(int i = j; i < n; i++)
#define EPS 1e-12

using namespace std;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

int main(){
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        double ans, waktu;
        int D, N;
        cin >> D >> N;
        int K, S;
        for (int j = 0; j < N; j++) {
            cin >> K >> S;
            if (j == 0 || waktu * S + K < D) {
                waktu = (double) (D - K) / (double) S;
            }
        }

        ans = D / waktu;

        cout << fixed << setprecision(6);
        cout << "Case #" << i << ": " << ans << endl;
    }
	return 0;
}
