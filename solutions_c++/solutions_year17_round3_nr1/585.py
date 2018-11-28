//
//  main.cpp
//  zz
//
//  Created by wjmiao on 30/04/2017.
//  Copyright © 2017 wjmiao. All rights reserved.
//

#include <iostream>
#include <algorithm>
using namespace std;

#define pi 3.141592653

struct G{
    int R;
    int H;
};

G g[1000];
double H[1000];

bool com(G g1, G g2){
    if (g1.R > g2.R)
        return true;
    else return false;
}

int main(int argc, const char * argv[]) {
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int ca = 1; ca <=T; ca++){
        int N,K;
        scanf("%d%d",&N,&K);
        for(int i=0;i<N;i++){
            scanf("%d%d",&g[i].R,&g[i].H);
        }
        sort(g,g+N,com);
        double ans = 0;
        for(int i=0;i+K-1<N;++i){
            int r=g[i].R;
            int cnt = 0;
            for(int j=i+1;j<N;++j){
                H[cnt++]=g[j].H * 2.0 * pi * g[j].R;
            }
            sort(H,H+cnt);
            double HSum = 0;
            for(int j=0;j<K-1;++j){
                HSum += H[cnt-j-1];
            }
            double tmp = HSum + pi*r*r + 2*pi*g[i].R*g[i].H;
            ans = max(ans,tmp);
        }
        printf("Case #%d: %.8lf\n",ca,ans);
    }
    return 0;
}
