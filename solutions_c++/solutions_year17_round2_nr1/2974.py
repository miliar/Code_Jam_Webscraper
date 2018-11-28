#include<bits/stdc++.h>

using namespace std;

int n,d, s, v;
double maxt=0;

int main() {

    freopen("A-large.in", "r", stdin);
    freopen("out2.txt", "w", stdout);

    int T;
    scanf("%d", &T);
    for(int t=1; t<=T; t++) {
        maxt = 0.0;
        scanf("%d %d", &d,&n);
        for(int i=0; i<n; i++) {
            scanf("%d %d", &s,&v);
            maxt = max(maxt, (1.0*(d-s))/v);
        }
        //double ans=d/maxt;
        printf("Case #%d: ", t);
        printf("%lf\n",1.0*d/maxt);
    }
    return 0;
}
