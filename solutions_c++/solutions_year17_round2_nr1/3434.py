#include <iostream>
#include <stdio.h>
#include <limits.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <queue>

typedef long long ll;
using namespace std;

int t,n;
int d;
int k[1010];
int s[1010];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

    cin >> t;

    for (int tt = 1; tt <= t; tt++) {
        cin >> d >> n;

        double t = 0;
        for (int i = 0; i < n; i++) {
            cin >> k[i] >> s[i];

            t = max(t, (d-k[i])*1.0/s[i]);

        }
        double ans = d / t;
        cout.precision(10);
        std::cout.setf( std::ios::fixed, std:: ios::floatfield );
        cout << "Case #" << tt << ": " << ans << endl;
    }


    return 0;
}
