#include <bits/stdc++.h>
using namespace std;

long double a[10001],b[10001];

int main(){
    freopen("input.in","r",stdin);
    freopen("gcb_out2.txt","w",stdout);
    int t;
    cin>>t;
    int k=0;
    while(t--){
            k++;
        long double dist,n;
        cin>>dist>>n;
        for(int i=0; i<n; i++){
            cin>>a[i]>>b[i];
        }
        long double mi_time = 0;
        for(int i=0; i<n; i++){
            mi_time = max(mi_time,(long double)(dist-a[i])/b[i]);
        }
        long double ans = (long double)dist/mi_time;

        cout << "Case #" << k << ": " << setprecision(30) << ans << endl;
    }
}
