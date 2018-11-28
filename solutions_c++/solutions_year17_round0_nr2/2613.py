#include <cstdio>
#include <cstring>
char o[23];
int main() {
    int i, j, n;
    int t, tc;
    //freopen("/Users/SeoByeongChan/Desktop/input.txt","rt",stdin);
    //freopen("/Users/SeoByeongChan/Desktop/output.txt","w",stdout);
    scanf("%d",&tc);
    for(t=1;t<=tc;t++) {
        char p[23] = {0,};
        scanf("%s",o);
        n = (int)strlen(o);
        strcpy(p, o);
        for(i=1;i<n;i++) {
            if(o[i-1] > o[i]) {
                j = i - 1;
                
                while(j > 0 && o[j] == o[j-1]) j--;
                if(j == 0) {
                    if(o[j] == '1') {
                        for(j=0;j<n-1;j++) p[j] = '9';
                        p[n-1] = 0;
                    }
                    else {
                        p[j] = p[j] - 1;
                        for(j=1;j<n;j++) p[j] = '9';
                    }
                }
                else {
                    p[j] = p[j] - 1;
                    for(j=j+1;j<n;j++) p[j] = '9';
                }
                break;
            }
        }
        printf("Case #%d: %s\n",t,p);
    }
    return 0;
}
