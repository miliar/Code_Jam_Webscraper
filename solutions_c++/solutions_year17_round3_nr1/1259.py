#include<stdio.h>
#include<iostream>
#include<map>
#include<string.h>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;
typedef long long LL;
const int N = 1005;
int n,k;
struct Node{
    int r,h;
    LL  rh;
    int id;
    bool operator < (const Node& o) const{
        return r>o.r;
    }
}a[N];

const double pi = acos(-1.0);
int main(){
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    int T;scanf("%d",&T);
    int cas = 1;
    while(T--){
        scanf("%d%d",&n,&k);
        for(int i=0;i<n;i++){
            scanf("%d%d",&a[i].r,&a[i].h);
            a[i].rh=1LL*a[i].r*a[i].h;
        }
        sort(a,a+n);
        // int cnt = 1;
        // for(int i=1;i<n;i++){ 
        //     if(a[i].r==a[i-1].r) a[cnt-1].h = max(a[cnt-1].h,a[i].h);
        //     else a[cnt++] = a[i];
        // }
        // n = cnt;
        // for(int i=0;i<n;i++) printf("r:%d h:%d\n",a[i].r,a[i].h);
        // puts("");

        double res = 0;
        for(int i=0;i<n;i++){
            vector<LL> vec;
            for(int j=0;j<n;j++){
                if(j==i || a[i].r<a[j].r) continue;
                vec.push_back(a[j].rh);
            }


            if(vec.size()<k-1) continue;

            double R = a[i].r*1.0;

            sort(vec.begin(),vec.end());

            double tmp = R*R*pi;
            int count = k-1;
            for(int j=vec.size()-1;j>=0 && count;j--,count--){
                // printf("vec[%d]:%.6lf\n",j,vec[j]);
                tmp+=2*pi*vec[j]; 
            }
            tmp+=2*pi*a[i].rh;

            // printf("tmp:%.6lf\n\n",tmp);
            res = max(res,tmp);
        }
        printf("Case #%d: %.9lf\n",cas++,res);



    }

    return 0;
}
