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

    int T;
    int b[6]= {1,3,2,6,4,5};
    char c[6]={'R','O','Y','G','B','V'};
    scanf("%d",&T);
    for(int t=1; t<=T; t++) {
        int n, a[7];
        scanf("%d",&n);
        for(int i=0; i<6; i++) {
            scanf("%d",&a[i]);
        }
        int R=a[0]+a[1]+a[5];
        int Y=a[2]+a[1]+a[3];
        int B=a[4]+a[3]+a[5];
        cout<<"Case #"<<t<<": ";
        if(R>n/2 || Y>n/2 || B>n/2) {
            printf("IMPOSSIBLE\n");
            continue;
        }
        string ans="";
        int val[1001];
        for(int i=0; i<n; i++) {
            ans+='x';
            val[i]=0;
        }
        int x=n-1,xx,yy;

        for(int i=5; i>=0; i--) {
            int mx=a[0];
            int mi=0;
            for(int j=0; j<6; j++) {
                if(a[j]>mx) {
                    mx=a[j];
                    mi=j;
                }
            }
            for(int j=0; j<a[mi]; j++) {
                do {
                    x=(x+1)%n;
                    xx=(x+1)%n;
                    yy=(x-1+n)%n;
                } while(val[x]>0 || (val[xx]&b[mi]) || (val[yy]&b[mi]));
                                //printf("%d %d %d, ",i,j,x);
                val[x]=b[mi];
                ans[x]=c[mi];
            }
            a[mi]=0;
        }
        cout<<ans<<endl;
    }
}
