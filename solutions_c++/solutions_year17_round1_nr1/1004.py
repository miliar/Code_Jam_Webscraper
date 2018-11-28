#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;

char atleast(int i, string s) {
    for(int j = i; j < s.length(); j++) {
        if(s[j] >= 'A' && s[j] <= 'Z') return s[j];
    }
    return '?';
}

char atmost(int i, string s) {
    for(int j = i - 1; j >= 0; j--) {
        if(s[j] >= 'A' && s[j] <= 'Z') return s[j];
    }
    return '?';
}

int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        int R, C; cin >> R >> C;
        vector<string> A(R);
        for(int i = 0; i < R; i++) {
            cin >> A[i];
            if(atleast(0, A[i]) != '?') {
                for(int j = 0; j < C; j++) {
                    A[i][j] = atleast(j, A[i]);
                    if(A[i][j] == '?')
                        A[i][j] = atmost(j, A[i]);
                }
                for(int j = i - 1; j >= 0; j--) {
                    if(atleast(0, A[j]) == '?') {
                        A[j] = A[i];
                    }
                }
            }
        }
        for(int i = 1; i < R; i++) {
            if(atleast(0, A[i]) == '?') A[i] = A[i-1];
        }
        printf("Case #%d: \n", t);
        for(string s : A) cout << s << endl;
    }
    return 0;
}
