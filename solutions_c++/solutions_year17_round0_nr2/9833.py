#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef pair<int,int> pi;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    short t = 0;
    cin >> t;

    ull n = 0, p =0;

    for (int i=1; i<=t; ++i) {
        cin >> n;
        p = n;

        short j = 0, prev = n % 10;
        short r = 0;
        bool failed = false;

        while (n > 0) {
            //cout << "\t" << n << "\n";
            r = n % 10;
            n /= 10; 

            j++;

            if (prev < r) {
                failed = true;
                if (r-1 >= n%10)
                    break;
            }

            prev = r;
        }

        if (prev < r) {
            failed = true;                
        }

        cout << "Case #" << i << ": ";
        if (!failed) {
            cout << p;
        }
        else {
            if (n > 0)
                cout << n;
            if (r > 1)
                cout << r-1;
            for (int t=0; t<j-1; ++t) {
                cout << 9;
            }
        }
        cout << "\n";
    }
     
    return 0;
} 
