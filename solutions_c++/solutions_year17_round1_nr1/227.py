#include <iostream>

using namespace std;

int main(void) {

    int test_num;
    cin >> test_num;
    for (int Case = 1 ; Case <= test_num ; ++Case) {

        int n, m;
        cin >> n >> m;

        string str[n];
        for (int i = 0 ; i < n ; ++i) {
            cin >> str[i];
        }

        char const Q = '?';
        for (int i = 0 ; i < n ; ++i) {
            bool found = false;
            for (int j = 0 ; j < m ; ++j) {
                if (str[i][j] != Q) {
                    found = true;
                }
            }
            if (found) {
                for (int j = 1 ; j < m ; ++j) {
                    if (str[i][j] == Q and str[i][j-1] != Q) {
                        str[i][j] = str[i][j-1];
                    }
                }
                for (int j = m-2 ; j >= 0 ; --j) {
                    if (str[i][j] == Q and str[i][j+1] != Q) {
                        str[i][j] = str[i][j+1];
                    }
                }
            }
        }

        for (int i = 1 ; i < n ; ++i) {
            if (str[i][0] == Q) {
                str[i] = str[i-1];
            }
        }
        for (int i = n-2 ; i >= 0 ; -- i) {
            if (str[i][0] == Q) {
                str[i] = str[i+1];
            }
        }

        cout << "Case #" << Case  << ":" << endl;
        for (int i = 0 ; i < n ; ++i) {
            cout << str[i] << endl;
        }
        
        cerr << Case << endl;
    }

    return 0;
}
