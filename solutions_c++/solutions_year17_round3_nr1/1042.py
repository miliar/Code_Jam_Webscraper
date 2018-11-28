#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<cstring>
#include<stdio.h>
#include<cmath>
#include<set>
#include<map>

using namespace std;

pair<double, pair<double, double > > a[1001];


int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int T,k,n;

    cin>>T;
    for(int t=1; t<=T; t++) {
        cin>>n>>k;
        for(int i=0; i<n; i++) {
            scanf("%lf%lf",&a[i].second.first,&a[i].second.second);
            a[i].first = 2.0*a[i].second.second*a[i].second.first;
        }
        sort(a,a+n);

        double ans=0.0;
        for(int i=0; i<n; i++) {
            double r=a[i].second.first;
            double area=r*r+a[i].first;
            int cnt=1;
            for(int j=n-1; cnt<k && j>=0; j--) {
                if(i==j) continue;
                if(a[j].second.first <= r) {
                    area+=a[j].first;
                    cnt++;
                    if(cnt==k) break;
                }
            }
            if(cnt==k)
            ans=max(ans, area);
        }
        ans*=3.1415926535;
        cout<<"Case #"<<t<<": ";
        printf("%.6lf\n",ans);
    }
}
