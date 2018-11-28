#include <stdio.h>
#include <iostream>

using namespace std;

int main(){

    int T;

    cin >> T;

    for (int t= 1; t<= T; t++){
        string S;
        cin >> S;
        int s[20];
        for (int i = 0 ; i < S.length() ; i++){
            s[i] = S[i] -'0';
        }

        for (int i = 1 ; i < S.length() ; i++) {
            if (s[i] < s[i-1]) {
                for (int j = i ;j < S.length(); j++){
                    s[j] = 9;
                }

                            s[i-1]--;

                int k = i-1;
                while (k > 0 && s[k] < s[k-1]) {
                    s[k] = 9;
                    s[k-1]--;
                    k--;
                }

                break;
            }

        }

        printf("Case #%d: ",t);
        if (s[0] != 0) {
            printf("%d",s[0]);
        }
        for (int i = 1 ; i< S.length();i++){

            printf("%d",s[i]);
        }
        printf("\n");
    }


}
