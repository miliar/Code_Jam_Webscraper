#include<stdio.h>
#include<string.h>
#include<memory.h>
#include<algorithm>
#include <map>
#include <unordered_map>
#include<utility>
#include<iostream>
#include<math.h>
#include<vector>
#include <queue>

using namespace std;


bool hasletter(const string &s) {
    for(int j=0;j<s.length();j++) {
        if(isalpha(s[j]))
            return true;
    }
    return false;
}
void solveCase(vector<string> &S) {

    for(int i= 0 ; i < S.size();i++) { // 25
        if(hasletter(S[i])) { // 25
            for(int j=0;j<S[i].length();j++) {
                // fild letter to the left
                if(isalpha(S[i][j]))
                    continue;

                char c = -1;
                for(int k = j+1 ; k < S[i].length();k++) { // 25
                    if(isalpha(S[i][k])) {
                        c = S[i][k];
                        break;
                    }
                }

                if(c==-1) {// find letter to the left
                    for(int k = 0; k < j ; k++) {
                        if(isalpha(S[i][k])) {
                            c = S[i][k];
                        }
                    }
                }
                S[i][j] = c;
            }
        }
    }

    for(int i = 0; i < S.size();i++) {
        for(int j = 0; j < S[i].length();j++) {
            if (S[i][j] == '?') {
                // find letter to the bottom
                char c = - 1;
                for (int k = i+ 1 ; k < S.size();k++) {
                    if(isalpha(S[k][j])) {
                        c = S[k][j];
                        break;
                    }
                }
                if(c==-1) {
                    for(int k = 0; k < i ; k++) {
                        if(isalpha(S[k][j])) {
                            c = S[k][j];
                        }
                    }
                }
                S[i][j] = c;
            }
        }
    }

}



int main() {
    int testCases;
    cin >> testCases;
    for(int i=0;i<testCases; i++) {
        vector<string> S;
        int R, C;
        cin >> R >> C;
        for(int j = 0 ; j < R; j++) {
            string s;
            cin >> s;
            S.push_back(s);
        }

        solveCase(S);
        cout << "Case #" << (i+1) << ":" << endl;
        for(int i = 0; i < R; i++) {
            for(int j = 0; j < C; j ++) {
                cout << S [i][j];

            }
            cout << "\n";
        }
    }

}