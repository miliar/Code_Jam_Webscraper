#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <cstring>

using namespace std;

int main() {
    int TT, T;
    scanf("%d", &TT);
    
    for (T = 1; T <= TT; T++) {
        printf("Case #%d: ", T);
        
        char str[100];
        
        scanf("%s", str);
        int i;
        int len = strlen(str);
        
        for (i = 1; i < len; i++) 
            if (str[i] < str[i-1])
                break;
        
        if (i == len) {
            printf("%s\n", str);
            continue;
        }
        
        for (i = i - 1; i > 0; i--) {
            if (str[i] > str[i-1])
                break;
        }
        str[i] -= 1;
        for (i = i+1; i < len; i++)
            str[i] = '9';
        if (str[0] == '0')
            printf("%s\n", &str[1]);
        else
            printf("%s\n", str);
 

    }
}
        