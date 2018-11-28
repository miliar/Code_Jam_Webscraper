#include <bits/stdc++.h>

using namespace std;

int main()
{
    ifstream cin("in.in");
    ofstream cout("out.out");

    int t;
    cin >> t;

    for(int o = 1; o <= t; o ++) {

        bool mod[20];
        int d[20], k = 1;
        long long aux, n, ans = 0;

        cin >> n;
        aux = n;

        while(aux > 0) {
            d[k] = aux % 10;
            aux /= 10; k ++;
        }
        k --; // number of digits

        for(int i = 0; i <= k; i ++) mod[i] = false;

        for(int i = k - 1; i > 0; i --) {
                if(d[i] < d[i + 1]) {
                    if(!mod[i + 1]) {
                        d[i + 1] --;

                        for(int j = i + 1; j < k; j ++) {
                            if(d[j] < d[j + 1]) {
                                d[j] = 9;
                                d[j + 1] --;
                            }
                        }
                    }

                    d[i] = 9;
                    mod[i] = true;
                }
            }

        while(k > 0 && d[k] == 0) k --;

        cout << "Case #" << o << ": ";

        for(int i = k; i > 0; i --) cout << d[i];

        cout << "\n";

    }

    return 0;
}
