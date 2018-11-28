#include <cstdio>
#include <cstring>

const int sz = 110;
char line[sz];
int a[sz];

int main() {
    //freopen("in.txt", "r", stdin);
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int cases;
    scanf("%d", &cases);
    for(int caseno=1;caseno<=cases;caseno++) {
        int len,i;
        scanf(" %s", line);
        len = strlen(line);
        for(i=0;i<len;i++) {
            a[i] = line[i] - '0';
        }

        while(true) {
            for(i=0;i+1<len;i++) {
                if(a[i]>a[i+1])
                    break;
            }
            if(i >= len-1)
                break;

            --a[i];
            for(i=i+1;i<len;i++) {
                a[i] = 9;
            }
        }

        printf("Case #%d: ", caseno);
        for(i=0;!a[i];i++);
        for(;i<len;i++) printf("%d",a[i]);
        puts("");
    }
    return 0;
}
