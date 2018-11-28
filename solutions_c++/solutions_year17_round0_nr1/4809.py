//
// Created by Taewoo Kim on 4/8/2017.
//

#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int flip(string s, int k){
    int n = s.length();
    int i = 0;//begin index
    int count = 0;

    while (i < n){
        if (s[i] == '-'){
            if (i + k > n) return -1;
            for (int j = i; j < i + k; j++){
                s[j] = (s[j] == '-' ? '+' : '-');
            }
            count++;
        }
        while (i < n && s[i] == '+') i++;
    }
    return count;
}

int main() {
    int t;
    cin >> t;

    //ofstream myFile("output.txt");

    for (int i = 1; i <= t; i++){
        string s;
        int k;
        cin >> s >> k;
        int res = flip(s,k);
        cout << "Case #" << i << ": " << (res == -1 ? "IMPOSSIBLE" : to_string(res)) << endl;
    }

    //myFile.close();

    return 0;
}