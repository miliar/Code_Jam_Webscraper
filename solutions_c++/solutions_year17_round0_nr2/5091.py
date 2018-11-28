#include <bits/stdc++.h>
using namespace std;

void solver(char* buffer)
{
    int len = strlen(buffer);
    for(int i = len - 1; i > 0; --i) {
        if(buffer[i - 1] > buffer[i]) {
            buffer[i - 1] -= 1;
            for(int j = i; j != len; ++j)
                buffer[j] = '9';
        }
    }
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
    scanf("%d", &t);
    for(int i = 0; i != t; ++i) {
        char buffer[25];
        scanf("%s", buffer);
        printf("Case #%d: ", i + 1);
        solver(buffer);
        if(buffer[0] != '0')
            printf("%s\n", buffer);
        else
            printf("%s\n", buffer + 1);
    }
    return 0;
}
