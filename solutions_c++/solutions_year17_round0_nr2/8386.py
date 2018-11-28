#include <cstdio>
#include <cstring>

char in[20];
int ans[20];
int T;

int main() {
    scanf("%d", &T);
    for(int tt = 1; tt <= T; tt++){
        scanf("%s", in);
        int len = strlen(in);

        ans[0] = in[0] - '0';
        for(int i = 1; i < len; i++){
            int curr = in[i] - '0';
            if(ans[i - 1] > curr){
                int st;
                for(st = i - 2; st >= 0; st--){
                    if(ans[st] < ans[i - 1]){
                        break;
                    }
                }
                st++;

                ans[st] --;
                for(int j = st + 1; j < len; j++){
                    ans[j] = 9;
                }
                break;
            }
            ans[i] = curr;
        }

        long long out = 0;
        for(int i = 0; i < len; i++){
            out *= 10;
            out += ans[i];
        }

        printf("Case #%d: %lld\n", tt, out);
    }
}
