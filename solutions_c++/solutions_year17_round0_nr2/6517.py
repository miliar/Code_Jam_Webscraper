# include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int a[100], b[100];
int check (ll n) {

    int d, prev;
    prev = n%10;
    n = n/10;

    while (n > 0) {

        d = n%10;

        if (d <= prev) {

            prev = d;
            n = n/10;

        }

        else
            return 0;

    }

    return 1;

}


int main () {

    int t, pos, i, j, k, temp, prev,  mark;

    ll n;

    cin >> t;

    for (k=1; k<=t; k++) {

        cin >> n;

        cout << "Case #" << k << ": " ;

        pos = 0;

        if (check (n)) {

            cout << n << endl;

        }

        else {

            ll m = n;

            while (m > 0) {

                a[pos++] = m % 10;
                m = m/10;

            }

            j = 0;
            for (i=pos-1; i>=0; i--) {

                b[j++] = a[i];

            }

            prev = b[0];
            for (i=1; i<pos; i++) {

                if (b[i] < prev)
                    break;

                prev = b[i];

            }

            temp = b[i-1];
            mark = 0;

            for (j=i-1; j>=0; j--) {

                //cout << b[j] <<" " << temp << "\n";
                if (b[j] != temp) {

                    mark = j+1;
                    break;

                }
            }

            //cout << pos << " " << i << " " << mark << endl;

            for (i=mark+1; i<pos; i++)
                b[i] = 9;

            b[mark] -= 1;

            for (i=0; i<pos; i++) {

                if (i==0 && b[i]==0)
                    continue;

                cout << b[i] ;
            }

            cout << endl;

        }
    }

}
