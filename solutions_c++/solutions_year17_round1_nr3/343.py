#include <bits/stdc++.h>
using namespace std;

#define   LL            long long

int r[100];
int q[100][100];
int num[100];
int n,p;

bool check(int i,int j)
{
    //cout<<r[j]*i*0.9<<" "<<q[j][num[j]]<<" "<<r[j]*i*1.1<<endl;
    if(num[j]<p&&(LL)r[j]*i*9<=(LL)q[j][num[j]]*10&&(LL)r[j]*i*11>=(LL)q[j][num[j]]*10) return true;
    //cout<<1<<endl;
    return false;
}
int main()
{
    int t;
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small-attempt1.out","w",stdout);
    scanf("%d",&t);
    int kase=0;
    while(t--) {
        int hd,ad,hk,ak,b,d;
        cin>>hd>>ad>>hk>>ak>>b>>d;
        int ans=1e9;
        kase++;
        printf("Case #%d: ",kase);
        for(int i=0; i<=100; i++) {
            for(int j=0; j<=100; j++) {
                int num1=i;
                int num2=j;
                int ret=0;
                int flag=0;
                int cure=0;
                int hd1=hd,ad1=ad,hk1=hk,ak1=ak,b1=b,d1=d;
                while(1) {
                    ret++;
                    if(num1) {
                        if(hd1-(ak1-d1)<=0) {
                            if(cure==0) {
                                cure=1;
                                hd1=hd;
                                hd1-=ak1;
                            } else {
                                flag=1;
                                break;
                            }
                        } else {
                            ak1=max(ak1-d1,0);
                            cure=0;
                            hd1-=ak1;
                            num1--;
                        }
                    } else if(num2) {
                        if(hd1-ak1<=0) {
                            if(cure==0) {
                                cure=1;
                                hd1=hd;
                                hd1-=ak1;
                            } else {
                                flag=1;
                                break;
                            }
                        } else {
                            ad1+=b1;
                            cure=0;
                            hd1-=ak1;
                            num2--;
                        }
                    } else {
                        if(hk1-ad1<=0) {
                            break;
                        }
                        if(hd1-ak1<=0) {
                            if(cure==0) {
                                cure=1;
                                hd1=hd;
                                hd1-=ak1;
                            } else {
                                flag=1;
                                break;
                            }
                        } else {
                            hk1-=ad1;
                            hd1-=ak1;
                            cure=0;
                        }
                    }
                }
                if(!flag) ans=min(ans,ret);
            }

        }
        if(ans==1e9) printf("IMPOSSIBLE\n");
        else printf("%d\n",ans);
    }
    return 0;
}
