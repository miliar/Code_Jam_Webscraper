#include <iostream>

using namespace std;

int main() {
    int t;
    cin >> t;
    for ( int testCase = 1; testCase <= t; ++testCase ) {
        string input;
        int windowSize;
        cin >> input >> windowSize;
        int minusCount = 0;
        for ( auto &&item : input ) {
            if ( item == '-' ) {
                ++minusCount;
            }
        }
        int moves = 0;
        for ( int i = 0; i < input.size() - windowSize + 1; ++i ) {
            if ( input[i] == '-' ) {
                ++moves;
                for ( int j = i; j < i + windowSize; ++j ) {
                    if ( input[j] == '-' ) {
                        --minusCount;
                        input[j] = '+';
                    } else {
                        ++minusCount;
                        input[j] = '-';
                    }
                }
            }
        }
        cout << "Case #" << testCase << ": ";
        if ( minusCount == 0 ) {
            cout << moves << endl;
        } else {
            cout << "IMPOSSIBLE" << endl;
        }
    }
    return 0;
}