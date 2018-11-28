#include <cstdio>
#include <cstring>

long long lowest(long long prefix) {
    //printf("prefix == %lld\n", prefix);

    long long res = prefix % 10;
    res -= 1;
    
    while (res < prefix) {
        res *= 10;
        res += 9;
    }
    
    return res;
}

int main() {
    char str[20];
    int t, n;
    
    scanf("%d", &t);
    
    long long pow[20];
    
    pow[0] = 1LL;
    
    for (int i = 1; i <= 18; i++) {
        pow[i] = pow[i - 1] * 10;
    }
    
    for (int tcase = 1; tcase <= t; tcase++) {
        scanf("%s", str);
        
        n = strlen(str);
        
        int right = 0;        
        long long prefix = str[0] - '0';

        printf("Case #%d: ", tcase);
        for (int i = 1; i < n; i++) {
            //printf("i = %d right = %d\n", i, right);
        
            if (right == (i - 1) && str[i - 1] < str[i] ) {
                right++;
                printf("%lld", prefix);
                prefix = str[i] - '0';
            } else if ( (right == i - 1) && (str[i - 1] == str[i]) ) {
                right++;
                prefix = prefix * 10LL + str[i] - '0';
            } else if (right == i - 1) {
                prefix = lowest(prefix);
            } else {
                prefix = prefix * 10 + 9LL;
            }
        }
        
        printf("%lld\n", prefix);
    }
    return 0;
}
