#include <cstdio>
#include <cstring>

using namespace std;

char flip(char a){
    if(a == '-')return '+';
    return '-';
}

char str[1003];

int main(){

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int t;
    scanf("%d", &t);

    int tc = 0;

    while(t--){
        int k;
        scanf("%s %d", str, &k);
        int s = strlen(str);
        int c = 0;
        for(int i=0; i+k<=s; i++){
            if(str[i] == '-'){
                str[i] = '+';
                for(int j=i+1; j<i+k; j++)str[j] = flip(str[j]);
                c++;
            }
        }

        for(int i=s-1; i>=s-k; i--)if(str[i] == '-')c = -1;
        printf("Case #%d: ", ++tc);
        if(c == -1)printf("IMPOSSIBLE\n");
        else
            printf("%d\n", c);

    }

}
