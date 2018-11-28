#include <fstream>
#include <cstring>
using namespace std;
ifstream cin("date.in");
ofstream cout("date.out");

char s[1009];
bool v[1009];
int dp[1009];
int T_MAX, t, k;

int main(){
    cin >> T_MAX;
    for(t = 1; t <= T_MAX; t++){
        for(int i = 0; i <= 1008; i++){
            dp[i] = 0;
        }
        cin >> s >> k;
        for(int i = 0; i < strlen(s); i++){
            v[i] = 0;
            if(s[i] == '+'){
                v[i] = 1;
            }
        }

        for(int i = strlen(s)-1; i >= k-1; i--){

            for(int j = i+1; j <= strlen(s)-1; j++){
                if(v[i] == 1){
                    s[i] = '+';
                }else{
                    s[i] = '-';
                }
            }
            if(v[i] == 1){
                dp[i] = dp[i+1];
                s[i] = '+';
            }else{
                dp[i] = dp[i+1] + 1;
                for(int j = i; j >= i-k+1; j--){
                    v[j] = !v[j];
                    if(s[j] == '+'){
                        s[j] = '-';
                    }else{
                        s[i] = '+';
                    }
                }
            }
        }

        bool ok = 1;
        for(int j = 0; j <= strlen(s)-1; j++){
            if(v[j] == 0){
                ok = 0;
                break;
            }
        }
        if(ok == 0){
            cout << "Case #" << t << ": IMPOSSIBLE" << '\n';
        }else{
            cout << "Case #" << t << ": " <<dp[k-1] << '\n';
        }

    }
    return 0;
}
