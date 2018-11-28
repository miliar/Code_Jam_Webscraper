#include<bits/stdc++.h>

using namespace std;

long long n,d;

long long a[1005],b[1005];

int main(){

    freopen("gcj_in.txt","r",stdin);
    freopen("gcj_out.txt","w",stdout);

    int t1;
    cin >> t1;
    for(int it=1;it<=t1;it++) {

        long long i,j;
        cin >> d >> n;
        for(i=1;i<=n;i++) {
            cin >> a[i] >> b[i];
        }
        double ans,x,y,t;
        bool found = true;
        for(i=1;i<=n;i++) {
            x = ((double) d * (double) b[i]) / (double) (d - a[i]);
            t = (double) (d - a[i]) / (double) b[i];
            for(j=1;j<=n;j++) {
                y = (double) (d - a[j]) / (double) b[j];
                if(y > t) break;
            }
            if(j == n + 1) {
                if(found) ans = x,found = false;
                else ans = max(ans,x);
            }
        }
        cout << "Case #" << it << ": ";
        printf("%0.8f\n",ans);
    }
    return 0;

}

