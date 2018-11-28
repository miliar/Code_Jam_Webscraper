#include<bits/stdc++.h>

using namespace std;

#define mp(x,y) make_pair(x, y)
#define For(i, n) for (int i = 0; i < (int) n; i++)

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

int main () {
    int T;
    cin >> T;
    For(cases, T) {
        string s;
        cin >> s;
        char smallest = '9';
        int firstchange = s.size() - 1;
        for(int i = s.size() - 1; i >= 0; i--) {
            if (s[i] > smallest) {
                s[i] --;
                firstchange = i;
                smallest = s[i];
            }
            smallest = min(smallest, s[i]);
        }
        bool printed = false;
        printf("Case #%d: ", cases + 1);
        for (int i = 0; i <= firstchange; i++) {
            if (!printed && s[i] == '0') continue;
            printf("%c", s[i]);
        }
        for (int i = firstchange + 1; i < s.size(); i++) printf("9");
        printf("\n");
    }
}
