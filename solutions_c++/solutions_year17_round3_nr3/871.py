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

double a[55];


int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int T,k,n;
    double u;
    cin>>T;
    for(int t=1; t<=T; t++) {
        cin>>n>>k;
        cin>>u;
        for(int i=0; i<n; i++) {
            scanf("%lf",&a[i]);
        }
        sort(a,a+n);
        while(u>0) {
            int ind=0;
            while(ind<n && a[ind]==a[0]) {
                ind++;
            }

            if(ind==n) {
                for(int i=0; i<n; i++)
                    a[i]+=u/(double)n;
                u=0;
            }else {
                if(u>=ind*(a[ind]-a[0])) {
                    u-=double(ind)*(a[ind]-a[0]);
                    for(int i=0; i<ind; i++)
                        a[i]=a[ind];
                }else {
                    for(int i=0; i<ind; i++)
                        a[i]+=u/(double)ind;
                    u=0;
                }
            }
        }

        cout<<"Case #"<<t<<": ";
        double ans=a[0];
        for(int i=1; i<n; i++)
            ans*=a[i];
        printf("%.6lf\n",ans);
    }
}
