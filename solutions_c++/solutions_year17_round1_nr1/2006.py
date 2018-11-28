#include <cstdio>
#include <cstring>
char o[27][27];
char u[27][27];
int main() {
    int i, j, k, l;
    int t, tc;
    int n, m;
    freopen("/Users/SeoByeongChan/Desktop/practice/studyhard2/studyhard2/input.txt","rt",stdin);
    freopen("/Users/SeoByeongChan/Desktop/practice/studyhard2/studyhard2/output.txt","w",stdout);
    scanf("%d",&tc);
    for(t=1;t<=tc;t++) {
        scanf("%d %d",&n,&m);
        for(i=0;i<n;i++) scanf("%s",o[i]);
        for(i=0;i<n;i++) {
            for(j=0;j<m;j++) {
                u[i][j] = o[i][j];
            }
        }
        for(i=0;i<n;i++) {
            for(j=0;j<m;j++) {
                if(o[i][j] != '?') {
                    for(k=i;k>=0;k--) {
                        for(l=j;l>=0;l--) {
                            if((u[k][l] == '?' || u[k][l] == o[i][j]) && (o[i][l] == '?' || o[i][l] == o[i][j])) u[k][l] = o[i][j];
                            else break;
                        }
                        for(l=j;l<m;l++) {
                            if((u[k][l] == '?' || u[k][l] == o[i][j]) && (o[i][l] == '?' || o[i][l] == o[i][j])) u[k][l] = o[i][j];
                            else break;
                        }
                    }
                }
            }
        }
        for(i=0;i<n;i++) {
            for(j=0;j<m;j++) {
                if(u[i][j] == '?') u[i][j] = u[i-1][j];
            }
        }
        printf("Case #%d:\n",t);
        for(i=0;i<n;i++) {
            for(j=0;j<m;j++) printf("%c",u[i][j]);
            printf("\n");
        }
    }
    return 0;
}
