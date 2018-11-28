#include <iostream>
#include <map>
#include <stack>
#include <set>
#include <bits/stdc++.h>
#include <stdio.h>

using namespace std;

int T;
unsigned long long  D, N ,K[2000], S[2000];

char ans[1024];

void solve(){

}

int main(){

#if 0
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif

    cin>>T;
    for(int t=0; t<T; t++){
        cin>>D>>N;
        double max_h = 0;
        for(int i=0;i<N;i++){
            cin>>K[i]>>S[i];
            K[i] = D-K[i];

            double h = K[i]/(double)S[i];
            if(h>max_h)
                max_h = h;
        }

        solve();
        sprintf(ans, "%.6lf\n", (double)D/max_h);

        printf("Case #%d: %s", t+1, ans);
    }
    return 0;
}
