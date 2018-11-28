#include <bits/stdc++.h>

using namespace std;

const int MAXRC = 30;

char ch[MAXRC][MAXRC];

int main() {
    ifstream cin ("A-large.in");
    ofstream cout ("cake.out");
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int test;
    cin >> test;
    for (int ttest = 1; ttest <= test; ttest++) {
        cout << "Case #" << ttest << ": ";
        cout << "\n";

        int r, c;
        cin >> r >> c;

        for (int i = 1; i <= r; i++) {
            for (int j = 1; j <= c; j++) {
                cin >> ch[i][j];
            }
        }

        for (int i = 1; i <= r; i++) {
            for (int j = 1; j <= c; ) {
                if ('A' <= ch[i][j] && ch[i][j] <= 'Z') {
                    int k = j - 1;
                    while (k > 0 && ch[i][k] == '?') {
                        ch[i][k] = ch[i][j];
                        k--;
                    }
                    k = j + 1;
                    while (k <= c && ch[i][k] == '?') {
                        ch[i][k] = ch[i][j];
                        k++;
                    }
                    j = k;
                } else j++;
            }
        }

        for (int i = 1; i <= r; i++) {
            if (ch[i][1] == '?') {
                if (i == 1) {
                    int k;
                    for (k = 2; k <= r; k++)
                        if (ch[k][1] != '?') break;
                    for (int j = 1; j <= c; j++) ch[i][j] = ch[k][j];
                } else {
                    for (int j = 1; j <= c; j++) ch[i][j] = ch[i - 1][j];
                }
            }
        }

        for (int i = 1; i <= r; i++) {
            for (int j = 1; j <= c; j++) {
                cout << ch[i][j];
            }
            cout << "\n";
        }
    }
}

