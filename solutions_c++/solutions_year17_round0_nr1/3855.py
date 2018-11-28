#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
#include <sstream>
#include <iterator>
#include <unordered_set>

using namespace std;

string flipPancakes(string A) {
    string B;
    for (int i = 0; i < A.length(); i++) {
        if (A[i] == '+') {
            B = B + "-";
        }
        else {
            B = B + "+";
        }
    }
    return B;
}

int findMinimumFlips(string A, int K) {

    if (A == "+") {
        return 0;
    }

    if (A == "-" && K == 1) {
        return 1;
    }
    
    size_t found = A.find('-');
    if (A.length() < K) {
        if (found != string::npos) {
            return -1;
        }
        else {
            return 0;
        }
    }
    
    if (A[0] == '+') {
        return findMinimumFlips(A.substr(1, A.length() - 1), K);
    }
    else {
        A = flipPancakes(A.substr(0, K)) + A.substr(K, A.length() - K);
        int remaining_flips = findMinimumFlips(A, K);
        if (remaining_flips >= 0) {
            return (remaining_flips + 1);
        }
        else {
            return -1;
        }
    }
}

int main() {
    int n;
    cin >> n;
    vector<pair<string, int> > Z(n);
    for (int i = 0; i < n; i++) {
        string s;
        int k;
        cin >> s >> k;
        Z[i] = make_pair(s, k);
    }

    for (int i = 0; i < n; i++) {
        cout << "Case #" << (i + 1) << ": ";
        int output = findMinimumFlips(Z[i].first, Z[i].second);
        if (output != -1) {
            cout << output << endl;
        }
        else {
            cout << "IMPOSSIBLE" << endl;
        }
    }
    return 0;
}
