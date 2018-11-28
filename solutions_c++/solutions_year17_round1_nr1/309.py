#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string.h>
#include <set>
using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

int main(){
    int tcn;
    scanf("%d",&tcn);
    for(int tc=1;tc<=tcn;tc++){
        printf("Case #%d:\n",tc);
        int r,c;
        char a[30][30];
        scanf("%d%d",&r,&c);
        for(int i=0;i<r;i++){
            scanf("%s",a[i]);
        }

        for(int i=0;i<c;i++){
            char c = '?';
            for(int j=0;j<r;j++){
                if(a[j][i]!='?'){
                    c = a[j][i];
                    break;
                }
            }
            a[0][i] = c;
        }

        for(int i=0;i<c;i++){
            for(int j=1;j<r;j++){
                if(a[j][i]=='?')a[j][i] = a[j-1][i];
            }
        }
        int mn;
        for(int i=0;i<c;i++){
            if(a[0][i] != '?'){
                mn = i;
                break;
            }
        }
        if(a[0][0] == '?'){
            for(int i=0;i<r;i++){
                a[i][0] = a[i][mn];
            }
        }
        for(int i=0;i<r;i++){
            for(int j=1;j<c;j++){
                if(a[i][j] == '?'){
                    a[i][j] = a[i][j-1];
                }
            }
        }

        for(int i=0;i<r;i++){
            printf("%s\n",a[i]);
        }

    }
}
