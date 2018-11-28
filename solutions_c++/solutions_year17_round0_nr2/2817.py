#include <cstdio>

int n;
char t[30];

void prog() {
    n = 0;
    scanf("%s", t);
    while(t[n]) n++;
    int i = 0;
    while(t[i] <= t[i + 1]) i++;
    if(i == n - 1) {
        printf("%s\n", t);
        return;
    }

    for(int j = i + 1; j < n; ++j) t[j] = '9';
    t[i]--;
    while(i && t[i - 1] > t[i]) {
        t[i] = '9';
        t[i - 1]--;
        i--;
    }
    
    i = 0;
    while(t[i] == '0') i++;
    printf("%s\n", t+i);
}

int main() {
    int _; scanf("%d", &_);
    for(int i = 1; i <= _; ++i) {
        printf("Case #%d: ", i);
        prog();
    }
}
