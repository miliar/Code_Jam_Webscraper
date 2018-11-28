#include <cstdio>
#include <cstring>
using namespace std;

char a[20];

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int i=1; i<=t; i++){
        scanf("%s", a);
        for(int j=0, Max=0; j<strlen(a); j++){
            if( a[j]-'0' >= Max )
                Max = a[j] - '0';
            else if( Max != 1 ){
                while( j > 0 && a[j-1] == Max+'0') j--;
                a[j]--;
                for(int k=j+1; k<strlen(a); k++)
                    a[k] = '9';
                break;
            }
            else{
                for(int k=0; k<strlen(a)-1; k++)
                    a[k] = '9';
                a[strlen(a)-1] = '\0';
                break;
            }
        }
        printf("Case #%d: %s\n", i, a);
    }
    return 0;
}
