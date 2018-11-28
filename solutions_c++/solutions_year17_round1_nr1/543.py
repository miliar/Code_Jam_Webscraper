#include <bits/stdc++.h>

using namespace std;

char M[32][32];
int T, C=1, n, m;

int main() {

    for (scanf("%d",&T);T--;) {
        printf("Case #%d:\n",C++);
        scanf("%d %d",&n,&m);
        for (int i=0;i<n;i++)
            scanf("%s",M[i]);
        for (int j=0;j<m;j++) {
            for (int i=1;i<n;i++)
                if (M[i][j]=='?' and M[i-1][j]!='?')
                    M[i][j]=M[i-1][j];
            for (int i=n-2;i>=0;i--)
                if (M[i][j]=='?' and M[i+1][j]!='?')
                    M[i][j] = M[i+1][j];
        }
        for (int j=1;j<m;j++)
            if (M[0][j]=='?' and M[0][j-1]!='?') {
                for (int i=0;i<n;i++)
                    M[i][j] = M[i][j-1];
            }
        for (int j=m-2;j>=0;j--)
            if (M[0][j]=='?' and M[0][j+1]!='?') {
                for (int i=0;i<n;i++)
                    M[i][j] = M[i][j+1];
            }
        for (int i=0;i<n;i++)
            printf("%s\n",M[i]);

    }

    return 0;
}
