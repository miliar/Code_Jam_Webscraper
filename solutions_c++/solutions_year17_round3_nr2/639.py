#include <bits/stdc++.h>

using namespace std;

struct seg{
    int l,r,n;
    bool operator<(const seg &a)const{
        return l < a.l;
    }
    seg(){}
    seg(int l,int r,int n):l(l),r(r),n(n){}
};

vector<seg> temp;
vector<int> q[2];

void solve(){
    int T;
    scanf("%d",&T);
    for(int cs = 1;cs <= T;cs++){
        for(int i = 0;i < 2;i++)
        q[i].clear();
        temp.clear();
        int c,j;
        scanf("%d%d",&c,&j);
        int tc,tj;
        tc = tj = 720;
        for(int i = 0;i < c;i++){
            int a,b;
            scanf("%d%d",&a,&b);
            temp.push_back(seg(a,b,1));
            tj -= b-a;
        }
        for(int i = 0;i < j;i++){
            int a,b;
            scanf("%d%d",&a,&b);
            temp.push_back(seg(a,b,0));
            tc -= b-a;
        }
        //printf("tc=%d tj=%d\n",tc,tj);
        sort(temp.begin(),temp.end());
        int ans = 0;
        for(int i = 0;i < temp.size();i++){
            int dur = temp[(i+1)%temp.size()].l-temp[i].r;
            while(dur<0) dur += 1440;
            if(temp[i].n==temp[(i+1)%temp.size()].n){
                if(dur == 0) continue;
                ans+=2;
                q[temp[i].n].push_back(dur);
            }
            else{
                ans++;
            }
        }
        sort(q[0].begin(),q[0].end());
        sort(q[1].begin(),q[1].end());
        for(int i = 0;i < q[0].size()&&tc>=q[0][i];i++){
            tc -= q[0][i];
            ans -=2;
        }
        for(int i = 0;i < q[1].size()&&tj>=q[1][i];i++){
            tj -= q[1][i];
            ans -= 2;
        }
        printf("Case #%d: %d\n",cs,ans);
    }
}

int main(){
    freopen("B-large (1).in","r",stdin);
    freopen("B.out","w",stdout);
    solve();
    return 0;
}
