#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int tc,t=0;
    scanf("%d",&tc);
    while(t<tc){
            t++;
        int n,d;
            cin>>d>>n;
            double arr[5000];
            double srr[5000];
            double m=0,a,b,c,q=0,p;
            for(int i=0;i<n;i++){
                    cin>>arr[i]>>srr[i];
                        a=d-arr[i];
                        b=a/srr[i];
                        if(b>m){
                            m=b;
                        }
            }
            p=d/m;
            printf("Case #%d: %0.6lf\n",t,p);


    }

    return 0;
}
