#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

int main() {
    
    freopen("inl","r",stdin);
    freopen("out.out","w",stdout);
    
    int T;
    scanf("%d", &T);
    
    char str[1001];
    int K;
    int iCase = 1;
    while(T--) {
        
        scanf("%s",str);
        scanf("%d", &K);
        int iNumFlips = 0;
        int len = strlen(str);
        for(int i=0; str[i] != '\0'; i++) {
            if(str[i] == '-' && i+K-1 < len) {
                str[i] = '+';
                int iLastIndexInThisFlip = i+K-1;
                for(int j= i+1; j <= iLastIndexInThisFlip; j++) {
                   if(str[j] == '+') {
                       str[j] = '-';
                   }else {
                       str[j]= '+';
                   }  
                }
                iNumFlips++;
            }
            
        }
        
        bool bPossible = true;
        for(int i=0;str[i] != '\0';i++) {
            if(str[i] == '-') {
                bPossible = false;
                break;
            }
        }
        
        if (bPossible) {
            printf("Case #%d: %d\n",iCase, iNumFlips);
        } else{
            printf("Case #%d: IMPOSSIBLE\n", iCase);
        }
        iCase++;
    }
    
    
    
    return 0;
}