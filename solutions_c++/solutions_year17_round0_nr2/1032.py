#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string s;
int nrt;
long long n;

string longlongToString(long long n) {
    string ans;

    while(n > 0) {
        ans.push_back(n % 10);
        n /= 10;
    }

    reverse(ans.begin(), ans.end());
    return ans;
}

bool isTidy(int l, int r) {
    for(int i = l; i < r; ++i) {
        if(s[i] > s[i + 1])
            return 0;
    }

    return 1;
}

void printSol(int t) {
    long long ans = 0;

    for(int i = 0; i < (int) s.length(); ++i)
        ans = ans * 10 + s[i];

    cout << "Case #" << t << ": " << ans << "\n";
}

int main() {

    cin >> nrt;
    for(int t = 1; t <= nrt; ++t) {
        cin >> n;
        s = longlongToString(n);

        if(isTidy(0, s.length() - 1)) {
            printSol(t);
            continue;
        }

        for(int i = s.length() - 1; i >= 0; --i) {
            if(s[i] == 0)
                continue;
            --s[i];
            if(isTidy(0, i)) {
                for(int j = i + 1; j < (int) s.length(); ++j)
                    s[j] = 9;
                printSol(t);
                break;
            }
            ++s[i];
        }
    }

    return 0;
}