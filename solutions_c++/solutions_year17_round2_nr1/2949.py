/*************************************************************************
	> File Name: A.cpp
	> Author: tyxxzjpdez
	> Mail: tyxxzjpdez@163.com
	> Created Time: 2017年04月23日 星期日 07时59分26秒
 ************************************************************************/

#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

const int maxn=1000+10;
int D,N;
double Time;

int main(){
    //ios::sync_with_stdio(false);
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int T;scanf("%d",&T);
    for(int kase=1;kase<=T;kase++){
        Time=0.0;
        scanf("%d%d",&D,&N);
        for(int i=0;i<N;i++){
            int x,v;scanf("%d%d",&x,&v);
            Time=max(Time,1.0*(D-x)/v);
        }
        printf("Case #%d: %.6f\n",kase,1.0*D/Time);
    }
    return 0;
}
