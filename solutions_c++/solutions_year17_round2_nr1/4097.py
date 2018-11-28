#include<iostream>
#include<algorithm>
#include<vector>
#include<stdio.h>

using namespace std;

int main(){
    freopen("small1.in", "r", stdin);
    freopen("outS1.txt", "w", stdout);
    int t, n;
    int d, k, s;
    cin>>t;
    for(int x=0;x<t;++x){
        cin>>d>>n;
        vector<long double> v(n);
        for(int i=0;i<n;++i){
            cin>>k>>s;
            v[i] = (long double)(d-k)/s;
        }
        sort(v.begin(), v.end(), greater<long double>());
        printf("Case #%d: %1f\n", x+1, (double)((long double)d/v[0]));
    }
    return 0;
}
