#include <bits/stdc++.h>

using namespace std;
const double pi = acos(-1);

struct node{
    int r,h;
    double w;
    bool operator < (const node &a) const{
        return w>a.w;
    }
    node(int r,int h):r(r),h(h){
        w = pi*2*r*h;
    }
    node(){}
};

vector<node> cake;

int main(){
    freopen("A-large (1).in","r",stdin);
    freopen("A.out","w",stdout);
    int T,n,k,r,h;
    //printf("%f\n",pi);
    scanf("%d",&T);
    for(int cas = 1;cas <= T;cas++){
        cake.clear();
        scanf("%d%d",&n,&k);
        for(int i = 0; i < n;i++){
            scanf("%d%d",&r,&h);
            cake.push_back(node(r,h));
        }
        sort(cake.begin(),cake.end());
        double ans = 0;
        for(int i =0;i < cake.size();i++){
            double tmp;
            int now = cake[i].r;
            tmp = pi*now*now+cake[i].w;
            int cnt = 1;
            for(int j = 0;j < cake.size()&&cnt<k;j++){
                if(i == j) continue;
                if(cake[j].r > now) continue;
                tmp += cake[j].w;
                cnt++;
            }
            if(cnt==k) ans = max(ans,tmp);
        }
        printf("Case #%d: %.7f\n",cas,ans);
    }
}
