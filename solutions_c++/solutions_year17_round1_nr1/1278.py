#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
    freopen("/Users/zty/Downloads/A-large.in", "r", stdin);
    freopen("/Users/zty/Downloads/A-large.txt", "w", stdout);

    int n,a,b;
    char c[30][30];
    bool used[30];
    scanf("%d",&n);
    for (int cas = 1; cas <= n; ++cas) {
        scanf("%d%d",&a,&b);
        getchar();
        fill(used,used+30,false);
        bool flag=true;
        char ch;
        for (int i = 1; i <= a; ++i) {
            for (int j = 1; j <= b; ++j) {
                scanf("%c",&c[i][j]);
                if (c[i][j]!='?') {
                    used[i]=true;

                }
            }
            getchar();
        }
        int tmp=1;
        for (int i = 1; i <= a; ++i) {
            if (used[i]) {
                tmp=i;
                break;
            }
        }

        for (int i = 1; i <= a; ++i) {
            if (!used[i]) {
                if (i>tmp) {
                    for (int j = 1; j <= b; ++j) {
                        c[i][j]=c[i-1][j];
                    }
                }
            } else {

                bool f=true;
                for (int j = 1; j <= b; ++j) {
                    if (c[i][j]!='?') {
                        for (int k = j+1; k <= b; ++k) {
                            if (c[i][k]=='?') {
                                c[i][k]=c[i][j];
                            } else {
                                break;
                            }
                        }
                        if (f) {
                            for (int k = 1; k < j; ++k) {
                                c[i][k]=c[i][j];
                            }
                            f=false;
                        }
                    }
                }
            }
        }

        printf("Case #%d:\n",cas);
        for (int i = 1; i <= a; ++i) {
            if (i>=tmp) {
                for (int j = 1; j <= b; ++j) {
                    printf("%c",c[i][j]);
                }
            } else {
                for (int j = 1; j <= b; ++j) {
                    printf("%c",c[tmp][j]);
                }
            }
            printf("\n");
        }
    }
    return 0;
}