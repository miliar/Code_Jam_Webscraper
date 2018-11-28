#include <bits/stdc++.h>

using namespace std;

const int INF = 10000;

int n, m, k;

string pancakes;

void flipK(int index) {
    for (int i = index; i < index + k; i++) {
        pancakes[i] = (pancakes[i] == '+') ? '-' : '+';
    }
}
bool isValid() {
    for (int i = 0; i < pancakes.length(); i++) {
        if (pancakes[i] != '+') {
            return false;
        }
    }
    return true;
}
int main()
{
    int tests;
    freopen("A-large.in", "r", stdin);
    freopen("A-largeOUT.txt","w", stdout );
    scanf("%d", &tests);
    for (int i = 1; i <= tests; i++) {
        cin >> pancakes;
        cin >> k;
        int answer = 0;
        for (int j = 0; j < pancakes.length() - k + 1; j++) {
            if (pancakes[j] == '-') {
                flipK(j);
                answer++;
            }
        }
        cout << "Case #" << i << ": ";
        if (isValid()) {
            cout << answer;
        } else {
            cout << "IMPOSSIBLE";
        }
        cout << endl;
    }
    return 0;
}
