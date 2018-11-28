#include <iostream>
#include <cstdio>

using namespace std;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("large.out", "w", stdout);

    int t;
    cin >> t;
    for(int ts = 1 ; ts <= t ; ts++) {
        string p;
        int k;

        cin>>p>>k;

        int answer = 0;

        for(int i = 0 ; i <= p.length() - k ; i++) {
            if( p[i] == '-' ) {
                for(int j = 0 ; j < k ; j++) {
                    p[j+i] = p[j+i] == '+' ? '-' : '+';
                }

                answer++;
            }
        }

        int flag = true;

        for(int i = 0 ; i < p.length() ; i++) {
            if( p[i] == '-' ) {
                flag = false;
                break;
            }
        }

        cout << "Case #" << ts << ": ";

        if( flag ) {
            cout << answer << endl;
        }
        else {
            cout<< "IMPOSSIBLE" << endl;
        }
    }
    return 0;
}