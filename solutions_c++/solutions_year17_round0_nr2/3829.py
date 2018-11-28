#include <cstdio>
#include <cstring>
using namespace std;
int T;
char n[32];
int main() {
    freopen("blarge.in", "r", stdin);
    freopen("blarge.out", "w", stdout);
    scanf("%d", &T);
    for(int I = 1; I <= T; ++I) {
        scanf("%s", n);
        int l = strlen(n);
        for(int i = 0; i < l-1; ++i) {
            if(n[i] > n[i+1]) {
                for(; i > 0 && n[i] == n[i-1]; --i);
                --n[i];
                for(++i; i < l; n[i++] = '9');
                break;
            }
        }
        int os;
        for(os = 0; n[os] == '0'; ++os);
        printf("Case #%d: %s\n", I, n+os);
    }
    return 0;
}
            
