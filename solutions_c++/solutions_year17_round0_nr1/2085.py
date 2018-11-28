//
// Created by huklee on 08/04/2017.
//

#include <map>
#include <queue>
#include <string>
#include <bitset>
#include <fstream>
#include <iostream>
using namespace std;

void solve(string pan, int k){
    vector<int> arr;
    int count=0;
    for (char c : pan) arr.push_back(c == '-' ? 1 : 0);

    for (int i=0; i < pan.size() - k + 1; i++){
        if (arr[i] == 1){
            for (int j=0; j < k; j++)
                arr[i + j] ^= 1;
            count++;
        }
    }

    for (int i : arr){
        if (i == 1){
            cout << "IMPOSSIBLE" << endl;
            return;
        }
    }
    cout << count << endl;
}

int main() {
//    freopen("/Users/huklee/ClionProjects/Algorithm_Study/input.txt", "r", stdin);

    int T, k;
    cin >> T;
    for (int tc=1; tc <= T; tc++){
        string pan;
        cin >> pan >> k;
        cout << "Case #" << tc << ": ";
        solve(pan, k);
    }
}
