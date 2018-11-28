#include<iostream>
#include<string>
#include<vector>
using namespace std;
void fi(vector<string> &mp, int lr, int lc, int rr, int rc, int ch) {
    for (int i = lr; i <= rr; i++)
        for (int j = lc; j <= rc; j++)
            mp[i][j] = ch;
}

int main()
{
    int t;
    cin >> t;
    for (int cs = 1; cs <= t; cs++){
        int r, c;
        cin >> r >> c;
        vector<string> mp(r);
        for (int i = 0; i < r; i++)
            cin >> mp[i];
        int up = 0;
        for (int i = 0; i < r; i++) {
            int leftStart = 0;
            char last;
            for (int j = 0; j < c; j++) {
                if (mp[i][j] != '?') {
                    fi(mp, up, leftStart, i, j, mp[i][j]);
                    leftStart = j + 1;
                    last = mp[i][j];
                }
            }

            if (leftStart > 0) {
                fi(mp, up, leftStart, i, c - 1, last);
                up = i + 1;
            }
        }

        if (up < r) {
            for (int i = up; i < r; i++) {
                for (int j = 0; j < c; j++) {
                    mp[i][j] = mp[up - 1][j];
                }
            }
        }

        cout << "Case #" << cs << ":" << endl;
        for (int i = 0; i < r; i++)
            cout << mp[i] << endl;
    }

    return 0;
}

