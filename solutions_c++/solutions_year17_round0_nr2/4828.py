#include <iostream>
#include <string>

using namespace std;

int findBadIndex(const string &N) {
    long long badIndex = -1;
    for (long long i = 0; i < N.length() - 1; i++)
        if (N[i] > N[i+1])
            return i;
    return -1;
}

void fix(string &N, int badIndex) {
    if (badIndex == -1) 
        return;

    string firstPart = N.substr(0, badIndex + 1);
    string lastPart = N.substr(badIndex + 1);

    long long newFirstPart = stoll(firstPart) - 1;
    for (long long i = 0; i < lastPart.size(); i++) {
        lastPart[i] = '9';
    }

    N = to_string(newFirstPart) + lastPart;
}

long long solve() {
    string N;
    cin >> N;

    int badIndex;
    while ((badIndex = findBadIndex(N)) != -1) {
        fix(N, badIndex);
    }
    return stoll(N);
}

int main() {
    long long T;
    cin >> T;
    for (long long i = 0; i < T; i++) {
        long long result = solve();
        cout << "Case #" << i+1 << ": ";
        if (result == -1) {
            cout << "IMPOSSIBLE\n";
        } else {
            cout << result << "\n";
        }
    }
}
