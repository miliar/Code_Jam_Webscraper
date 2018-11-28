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

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int T,k;
    string s;
    cin>>T;
    for(int t=1; t<=T; t++) {
        int D,n;
        pair<int,int> a[1001];
        cin>>D>>n;
        for(int i=0; i<n; i++)
            scanf("%d%d",&a[i].first,&a[i].second);
        sort(a,a+n);
        double c=0;
        for(int i=n-1; i>=0; i--) {
            double x=double(D-a[i].first)/double(a[i].second);
            c=max(c,x);
        }
        double ans = D/c;

        cout<<"Case #"<<t<<": ";
        printf("%.6lf\n",ans);
    }
}
