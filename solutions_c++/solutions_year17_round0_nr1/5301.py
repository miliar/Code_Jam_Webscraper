#include <iostream>
#include <string>

using namespace std;

int main(void){
    int kase, K, counter;
    string S;
    cin >> kase;
    for(int cs = 1; cs <= kase; cs++){
        S.clear();
        cin >> S >> K;
        int s_len = S.length();
        counter = 0;
        for(int i = 0; i < (s_len - K + 1); i++){
            if(S[i] == '+') continue;
            if(S[i] == '-'){
                for(int j = i; j < i+K; j++){
                    if(S[j] == '+'){ S[j] = '-';}
                    else if(S[j] == '-'){ S[j] = '+';}
                }
                counter++;
            }
        }
        int flag = 1;
        for(int j = 0; j < s_len; j++){
            if(S[j] == '-'){
                flag = 0;
                break;
            }
        }
        if(!flag){
            cout << "Case #" << cs << ": IMPOSSIBLE" << endl;
            continue;
        }
        cout << "Case #" << cs << ": " << counter << endl;
    }
    return 0;
}
