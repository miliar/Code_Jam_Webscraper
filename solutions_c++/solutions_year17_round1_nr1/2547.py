#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for (int cas=1; cas<=t; cas++) {
        char s[30][30];
        int r,c;
        scanf("%d%d",&r,&c);
        for (int i=0; i<r; i++) scanf("%s",s[i]);
        for (int i=0; i<r; i++)
            for (int j=0; j<c; j++) {
                if (s[i][j]!='?') {
                    int k=j-1;
                    while (k>=0) {
                        if (s[i][k]=='?') s[i][k]=s[i][j];
                        else break;
                        k--;
                    }
                    k=j+1;
                    while (k<c) {
                        if (s[i][k]=='?') s[i][k]=s[i][j];
                        else break;
                        k++;
                    }
                }
            }
        for (int i=0; i<r; i++)
            if (s[i][0]=='?') {
                int k=i-1;
                bool flag=false;
                while (k>=0) {
                    if (s[k][0]!='?') {
                        flag=true;
                        break;
                    }
                    k--;
                }
                if (flag) {
                    for (int j=0;j<c;j++) s[i][j]=s[k][j];
                } else {
                    k=i+1;
                    while (k<r) {
                        if (s[k][0]!='?') break;
                        k++;
                    }
                    for (int j=0;j<c;j++) s[i][j]=s[k][j];
                }
            }
        printf("Case #%d:\n",cas);
        for (int i=0; i<r; i++) printf("%s\n",s[i]);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
