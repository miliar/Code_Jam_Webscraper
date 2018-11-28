#include <bits/stdc++.h>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);cin.tie(NULL);

    int t;
    unsigned long long n, k, r, s1, s2, aux;
    int k2;
    cin >> t;
    for(int i = 1; i <= t; i++) {
        cin >> n >> k;
        k2 = floor(log2(k));
        k2++;
        r = pow(2, k2);
        //Calculando el valor 1
        s1 = (n - k + r/2) / r; 
        // Calculando el valor 2
        s2 = (n - k)/r;
        cout << "Case #" << i << ": " << s1 << " " << s2 << endl;
    }
	return 0;
}