#include <stdio.h>
#include <string.h>

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large-output.txt", "w", stdout);
    int tc; scanf("%d", &tc);
    for(int testCase = 1; testCase <= tc; testCase++){
        char inp[20]={0,}; scanf("%s", inp);
        int len = (int)strlen(inp);
        for(int i = 0; i < len ;i++){
            bool possible = true;
            for(int j = i+1; j < len; j++){
                if(inp[i] < inp[j]) {
                    break;
                }
                if(inp[i] > inp[j]) {
                    possible = false;
                    break;
                }
            }
            if(possible) continue;
            inp[i]--;
            for(int j = i+1; j < len; j++)
                inp[j] = '9';
        }
        printf("Case #%d: ", testCase);
        for(int i = 0; i < len; i++){
            if(inp[i] == '0') continue;
            for(int j = i; j < len; j++)
                printf("%c", inp[j]);
            break;
        }
        printf("\n");
    }
    return 0;
}
