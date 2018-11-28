#include <iostream>
#include <cstdio>
#include <queue>
#include <cstring>
#define INF 0x3f3f3f3f

using namespace std;

int T,K;
string S;

int main(){
    freopen("data2.in","r",stdin);
    freopen("data2.out","w",stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> T;
    for (int z = 1; z <= T; z++){
        cin >> S >> K;
        int cnt = 0;
        for (int i = 0; i <= S.length()-K; i++){
            if (S[i] == '-'){
                for (int j = 0; j < K; j++){
                    if (S[i+j] == '-') S[i+j] = '+';
                    else S[i+j] = '-';
                }
                cnt++;
            }
        }
        bool flag = 1;
        for (char c : S){
            if (c == '-'){
                flag = 0;
                break;
            }
        }
        printf("Case #%d: ",z);
        if (!flag) printf("IMPOSSIBLE\n");
        else printf("%d\n",cnt);
    }
    return 0;
}
