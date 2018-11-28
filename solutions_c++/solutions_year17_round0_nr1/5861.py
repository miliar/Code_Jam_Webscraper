#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;

int solve(string S, int K) {
    int i = 0;
    int total = 0;
    while (i<S.length()) {
        if (S.at(i) == '-') {
            if (i+K <=S.length()) {
                total++;
                for (int j = i; j<i+K; j++) {
                    if (S[j] == '-') {
                        S[j] = '+';
                    } else {
                        S[j] = '-';
                    }
                }
            } else {
                return -1;
            }
        }
        i++;
    }
    return total;

}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int N;
    cin>>N;
    for (int aa=0;aa<N;aa++) {
        string S;
        int K;
        cin>>S;
        cin>>K;
        int ans = solve(S,K);
        printf("Case #%d: ", aa+1);
        if(ans == -1) {
           cout<< "IMPOSSIBLE"<<endl;
        } else {
            cout<<ans<<endl;
        }
    }
    fclose(stdin);
    fclose(stdout);
}
