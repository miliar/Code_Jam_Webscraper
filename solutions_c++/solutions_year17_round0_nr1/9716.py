#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>

using namespace std;

int main(){

    int n_cases;
    scanf("%d", &n_cases);

    for(int n = 0; n < n_cases; n++){
        string S;
        int K;

        cin >> S >> K;
        int solution = 0;

        for(int i = 0; i < S.length(); i++){
            if(S[ i ] == '-' && (i+K) <= S.length()){
                for(int j = i; j < i+K; j++){
                    S[ j ] == '-' ? S[ j ] = '+' : S[ j ] = '-';
                }
                solution++;
            }
        }

        int T = 0;
        for(int i = 0; i < S.length(); i++)
            if(S[ i ] == '+') T++;
        printf("Case #%d: ", n+1);
        (T == S.length()) ? cout << solution << endl : cout << "IMPOSSIBLE\n";
    }

    return 0;
}
