#include<bits/stdc++.h>
using namespace std;

int b[5555];
vector<int> a[5];

int main() {

    int n,p,x,i,j,m,t,res;

    int ttt;
    scanf("%d", &ttt);
    for(int tt=1; tt<=ttt; tt++) {
        printf("Case #%d: ", tt);
        scanf("%d%d", &n, &p);
        for(i=0; i<=p; i++) a[i].clear();
        for(i=0; i<n; i++) {
            scanf("%d", &x);
            a[x%p].push_back(x);
        }

        j=0;
        for(i=0; i<a[0].size(); i++) b[j++] = a[0][i];

        if (p == 2) {
            for(i=0; i<a[1].size(); i++) b[j++] = a[1][i];
        }

        if (p == 3) {

            m = min(a[1].size(), a[2].size());
            for(i=0; i<m; i++) {
                b[j++] = a[1][i];
                b[j++] = a[2][i];
            }

            for(i=m; i<a[1].size(); i++) b[j++] = a[1][i];
            for(i=m; i<a[2].size(); i++) b[j++] = a[2][i];

        }

        if (p == 4) {

            m = min(a[1].size(), a[3].size());
            for(i=0; i<m; i++) {
                b[j++] = a[1][i];
                b[j++] = a[3][i];
            }

            for(i=0; i<a[2].size(); i++) b[j++] = a[2][i];

            for(i=m; i<a[1].size(); i++) b[j++] = a[1][i];
            for(i=m; i<a[3].size(); i++) b[j++] = a[3][i];
        }

        t = 0; res = 0;
        for(i=0; i<n; i++) {
            if (t == 0) res++;
            t = (t+b[i]) % p;
        }

        printf("%d\n", res);
    }

    return 0;
}
