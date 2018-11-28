#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int main(){
    int t;
    scanf("%d", &t);
    for (int z = 1; z <= t; z++){
        char s[20];
        scanf("%s", s);
        for (int i = strlen(s) - 2; i >= 0; i--)
            if (s[i] > s[i + 1]){
                s[i] = s[i] - 1;
                for (int j = i + 1; j < strlen(s); j++)
                    s[j] = '9';
            }
        printf("Case #%d: ", z);
        int j;
        for (j = 0; j < strlen(s); j++) if (s[j] != '0') break;;
        for (int k = j; k < strlen(s); k++)
            printf("%d", s[k] - 48);
        printf("\n");
    }
    return 0;
}