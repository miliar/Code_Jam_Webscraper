# include <bits/stdc++.h>
using namespace std;
char str[1002];

int ones[1002], zeroes[1002];

int main () {

    int t, i, j, x;

    cin >> t;

    for (int k = 1; k <= t; k++) {

        cin >> str >> x;

        cout << "Case #" << k << ": ";

        int total = 0, n = strlen (str);

        for (i=0; i < n; i++) {

            if (str[i] == '+')
                total++;

        }

        //cout << total << "\n" ;

        if (total == n) {

            cout << "0\n";

        }

        else {

            int flip = 0, flag = 0;

            for (i=0; i <= (n - x); i++) {

                //cout << str[i] << "\n" ;

                if (str[i] == '+')
                    continue;

                else {

                    int ctr = 0, t1 = 0, t2 = 0;

                    flip++;

                    for (j=i; ctr != x; j++) {

                        ctr++;

                        if (str[j] == '+') {

                            t1++;
                            str[j] = '-';

                        }

                        else {

                            t2++;
                            str[j] = '+';

                        }

                    }

                    total = total - t1 + t2;

                    //cout << i << " " << flip << " " << total << endl;

                    if (total == n) {

                        flag = 1;
                        break;

                    }

                }

            }

            if (flag == 1)
                cout << flip << endl;

            else
                cout << "IMPOSSIBLE\n";

        }

    }

}
