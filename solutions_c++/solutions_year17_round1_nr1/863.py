#include <cstdio>
#include <cstring>
int t,r,c;
char s[33][33];
inline void flood1(int x,int y) {
    ++y;
    while (y<c&&s[x][y]=='?') {
        s[x][y]=s[x][y-1];
        ++y;
    }
}
inline void flood2(int x,int y) {
    --y;
    while (y>=0&&s[x][y]=='?') {
        s[x][y]=s[x][y+1];
        --y;
    }
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out3.txt","w",stdout);
    scanf("%d",&t);
    for (int cas=1;cas<=t;++cas) {
        scanf("%d%d",&r,&c);
        for (int i=0;i<r;++i)
            scanf("%s",s[i]);
        for (int i=0;i<r;++i)
            for (int j=0;j<c;++j)
                if (s[i][j]!='?') {
                    flood1(i,j);
                    flood2(i,j);
                }
        for (int i=0;i<r;++i)
            if (s[i][0]=='?') {
                int x=i;
                while (x<r) {
                    ++x;
                    if (x<r&&s[x][0]!='?') {
                        memcpy(s[i],s[x],sizeof s[x]);
                        break;
                    }
                }
                if (s[i][0]!='?')
                    continue;
                x=i;
                while (x>=0) {
                    --x;
                    if (x>=0&&s[x][0]!='?') {
                        memcpy(s[i],s[x],sizeof s[x]);
                        break;
                    }
                }
            }
        printf("Case #%d:\n",cas);
        for (int i=0;i<r;++i)
            puts(s[i]);
    }
    return 0;
}
