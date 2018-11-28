#include <iostream>

using namespace std;
int main(){
    int testCases;
    cin >> testCases;
    for (int test = 0; test < testCases; ++test) {
        string pancakes;
        cin >> pancakes;
        int k;
        cin >> k;
        int rotates = 0;
        for (int i = 0; i < pancakes.size()-k+1; ++i) {
            if (pancakes[i] == '-'){
                rotates++;
                for (int j = 0; j < k; ++j) {
                    pancakes[i+j] = pancakes[i+j] == '-' ? '+' : '-';
                }
            }
        }
        bool possible = true;
        for (int i = 0; i < pancakes.size(); ++i) {
            if (pancakes[i] == '-') {
                possible = false;
                break;
            }
        }
        cout << "Case #" << test+1 << ": ";
        if (possible)
            cout << rotates << endl;
        else
            cout << "IMPOSSIBLE" << endl;
    }
    return 0;
}