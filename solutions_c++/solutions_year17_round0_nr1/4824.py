#include <bits/stdc++.h>
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define PI acos(-1)
#define endl '\n'
using namespace std;

typedef long long ll;

int lastBlank(string s) {
    int len = s.length();
    for(int i = len - 1; i >= 0; i--)
        if(s[i] == '-')
            return i;
    return -1;
}

void flip(string &s, int start, int k) {
    for(; k > 0; k--, start++) {
        s[start] = (s[start] == '+') ? '-' : '+';
    }
}

int main() {

    int t, k;
    string s;

    cin >> t;
    for(int i = 1; i <= t; i++) {
    
        cin >> s >> k;
        int flips = 0;
        int last = lastBlank(s);
        bool possible = true;

        while(last != -1) {

            if(last < k -1) {
                possible = false;
                break;
            }

            flip(s, last - k + 1, k);

            flips++;
            last = lastBlank(s);    
        }    

        cout << "Case #" << i << ": ";
        if(possible)
            cout << flips << endl;
        else
            cout << "IMPOSSIBLE" << endl; 

    }

    return 0;
}
