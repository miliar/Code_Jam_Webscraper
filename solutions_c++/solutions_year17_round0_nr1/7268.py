#include <bits/stdc++.h>
#define endl '\n'

using namespace std;

const int N = 1024;

int tests,current_case;
int n,k;
char a[N];
int ans;

void message(int current_case) {
    //cerr<<"Case "<<current_case<<" solved!"<<endl;
    fprintf(stderr, "Case %d solved!\n", current_case);
}



int main() {
    //ios_base::sync_with_stdio(false);
    //cin.tie(NULL);
    int i,j,z;

    tests=1;
    scanf("%d", &tests);
    //cin>>tests;
    for(current_case=1;current_case<=tests;current_case++) {
        scanf("%s", a+1);
        n=strlen(a+1);
        scanf("%d", &k);
        ans=0;
        for(i=1;i<=n;i++) {
            for(j=1;j+k-1<=n;j++) {
                if(a[j]=='-') {
                    ++ans;
                    break;
                }
            }
            if(j+k-1>n) break;
            for(z=j;z<=j+k-1;z++) {
                if(a[z]=='-') a[z]='+';
                else a[z]='-';
            }
        }
        printf("Case #%d: ", current_case);
        for(i=1;i<=n;i++) {
            if(a[i]!='+') break;
        }
        if(i<=n) printf("IMPOSSIBLE\n");
        else printf("%d\n", ans);

        MESSAGE:
        message(current_case);
    }

    return 0;
}
