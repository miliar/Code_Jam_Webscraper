#include<bits/stdc++.h>

using namespace std;

int main(){

    freopen("gcj_in.txt","r",stdin);
    freopen("gcj_out.txt","w",stdout);

    int t;
    cin >> t;
    for(int it=1;it<=t;it++) {
        int n,i,idx,k,j;
        double a[55],temp=0,u,x,ans=0;
        cin >> n >> k;
        cin >> u;
        for(i=0;i<n;i++) {
            cin >> a[i];
        }
        sort(a,a+n);
        for(i=0;i<n;i++) {
            temp = 0;
            for(j=i-1;j>=0;j--) {
                temp = temp + (a[i] - a[j]);
            }
            if(temp <= u) {
                idx = i;
            }
        }
        for(i=idx;i>=0;i--) {
            u = u - (a[idx] - a[i]);
        }
        temp = a[idx];
        while(u > 1e-7) {
            x = u / (double)(idx + 1);
            temp = temp + x;
            u = u - (x * (double)(idx + 1));
        }
        ans = 1.0;
        for(i=0;i<=idx;i++) {
            ans = ans * temp;
        }
        for(i=idx+1;i<n;i++) ans = ans * a[i];
        cout << "Case #" << it << ": ";
        printf("%0.8f\n",min(ans,1.0));

    }
    return 0;


}
