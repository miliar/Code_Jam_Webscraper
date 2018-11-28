//#include<stdio.h>
//#include<string.h>
//#include<algorithm>
//#include<math.h>
//using namespace std;
//const double PI=acos(-1.0);


//
//int a[20000];
//
//int main(){
//    fre();
//    int _,kcase = 0;
//    scanf("%d",&_);
//    while(_--){
//        int ac,aj;
//        memset(a,0,sizeof(a));
//        scanf("%d %d",&ac,&aj);
//        int l,r,act=0,ajt=0;
//        for(int i=1;i<=ac;i++){
//            scanf("%d%d",&l,&r);
//            for(int i=l;i<=r;i++)      a[i%1440]=1,act++;
//        }
//
//        for(int i=1;i<=aj;i++){
//            scanf("%d%d",&l,&r);
//            for(int i=l;i<=r;i++)      a[i%1440]=2,ajt++;
//        }
//
//        printf("Case #%d: ",++kcase);
//        if(ac+aj == 1)     puts("2");
//        else {
//            if(ac==1)       puts("2");
//            else {
//                int sum1,sum2 ,flag=0;
//                for(int i=0;i<720;i++){
//                    sum1 = sum2 = 0;
//                    for(int j=i;j<i+720;j++){
//                        if(a[j%1440]==1) sum1++;
//                        if(a[j%1440]==2) sum2++;
//                    }
//                    if(sum1 == act && sum2 == 0  ) flag = 1;
//                    if(sum1 == 0   && sum2 == ajt) flag = 1;
//
//                }
//                if(flag)   puts("2");
//                else       puts("4");
//            }
//        }
//    }
//    return 0;
//}
#include<stdio.h>
#include<string.h>
#include<queue>
using namespace std;

void fre(){
    freopen("C-small-1-attempt0.in" ,"r",stdin );
    freopen("asdf.out","w",stdout);
}

int main()
{
    fre();
    int kase=0;
    int t;
    scanf("%d",&t);
    while(t--)
    {
        double U;
        int n,k;
        priority_queue<double, vector<double>, greater<double> >s;
        scanf("%d%d",&n,&k);
        scanf("%lf",&U);
        for(int i=0;i<n;i++)
        {
            double x;
            scanf("%lf",&x);
            s.push(x);
        }
        while(U>1e-8)
        {
            double tmp=s.top();
            s.pop();
            tmp+=0.0001;
            U-=0.0001;
            if(tmp>1)tmp=1;
            s.push(tmp);
        }
        double ans=1;
        while(!s.empty())
        {
            double tmp=s.top();
            s.pop();
            ans*=tmp;
        }
        printf("Case #%d: ",++kase);
        printf("%lf\n",ans);
    }
}
