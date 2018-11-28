#include <cstdio>
#include <cstring>
using namespace std;

char a[1005];

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, m, n;
    scanf("%d", &t);
    for(int i=1; i<=t; i++){
        scanf("%s%d", a, &m);
        n = 0;
        for(int j=0; j<=strlen(a)-m; j++){
            if( a[j] == '-' ){
                n++;
                for(int k=0; k<m; k++){
                    if(a[k+j]=='-') a[k+j]='+';
                    else if(a[k+j]=='+') a[k+j]='-';
                }
            }
        }
        bool flag = true;
        for(int j=0; j<strlen(a); j++)
            if(a[j] == '-') flag = false;
        if(flag)
            printf("Case #%d: %d\n", i, n);
        else
            printf("Case #%d: IMPOSSIBLE\n", i);
    }
    return 0;
}
