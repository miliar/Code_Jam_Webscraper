#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
#include<map>
#include<unordered_map>
#include<string>
#include<queue>
#define ll long long
#define fi first
#define se second
using namespace std;
int main(void){
    //freopen("test.txt", "r", stdin);
    //freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-large.in","r", stdin);
    freopen("A.out", "w",stdout);
    int T;
    scanf("%i", &T);
    for(int l=0;l<T;l++){
        int N; int M;
        scanf("%i %i", &N, &M);
        char c;
        char a[N][M];
        int i;
        int j;
        for(i=0;i<N;i++){
            scanf("%c", &c);
            for(j=0;j<M;j++){
                scanf("%c", &a[i][j]);
            }
        }
        int k; int m;
        char zrovna;
        char prvni;
        for(i=0;i<N;i++){
            zrovna='?';
            prvni='.';
            for(j=0;j<M;j++){
                if(a[i][j]!='?') zrovna=a[i][j];
                if(prvni=='.'&&a[i][j]!='?') prvni=a[i][j];
                if(a[i][j]=='?') a[i][j]=zrovna;
            }
            if(prvni=='.') continue;
            for(j=M-1;j>=0;j--){
                if(a[i][j]=='?') a[i][j]=prvni;
            }
        }
        for(i=1;i<N;i++){
            for(j=0;j<M;j++){
                if(a[i][j]=='?') a[i][j]=a[i-1][j];
            }
        }
        for(i=N-2;i>=0;i--){
            for(j=0;j<M;j++){
                if(a[i][j]=='?') a[i][j]=a[i+1][j];
            }
        }
        printf("Case #%i:\n", l+1);
        for(i=0;i<N;i++){
            for(j=0;j<M;j++){
                printf("%c",a[i][j]);
            }
            printf("\n");
        }
    }
    return 0;
}
