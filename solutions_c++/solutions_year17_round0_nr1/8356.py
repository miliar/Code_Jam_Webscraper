#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int T;
char in[1005], len;
bool fl[1005];
int n;

int main(){
    scanf("%d", &T);
    for(int tt = 1; tt <= T; tt++){
        scanf("%s %d", in, &n);

        len = strlen(in);
        for(int i = 0; i < len; i++){
            fl[i] = false;
        }

        int ans = 0;
        bool flipping = false;
        for(int i = 0; i < len - n; i++){
            if(fl[i]){
                flipping = !flipping;
            }

            if((in[i] == '-' && !flipping) || (in[i] == '+' && flipping)){
                ans += 1;
                flipping = !flipping;

                fl[i + n] = !fl[i + n];
            }
        }

        bool lastflip;
        if(fl[len - n]){
            flipping = !flipping;
        }
        if((in[len - n] == '-' && !flipping) || (in[len - n] == '+' && flipping)){
            lastflip = true;
        }
        else {
            lastflip = false;
        }

        printf("Case #%d: ", tt);

        for(int i = len - n + 1; i < len; i++){
            if(fl[i]){
                flipping = !flipping;
            }

            if(((in[i] == '-' && !flipping) || (in[i] == '+' && flipping)) && !lastflip){
                ans = -1;
                break;
            }

            else if(((in[i] == '-' && flipping) || (in[i] == '+' && !flipping)) && lastflip){
                ans = -1;
                break;
            }
        }

        if(ans == -1){
            printf("IMPOSSIBLE\n");
        }
        else {
            printf("%d\n", ans + (lastflip == true));
        }
    }
}
