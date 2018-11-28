#include <bits/stdc++.h>
#define maxx 100005
#define inf 2000000000
#define mod 1000000007
#define pii pair<int,int>
#define piii pair<pii,pii>
#define pli pair<long long,int>
#define pll pair<long long,long long>
#define f first
#define s second
#define in(x) scanf("%d",&x)
#define IN(x) scanf("%lld",&x)
#define inch(x) scanf("%s",x)
#define indo(x) scanf("%lf",&x)
#define pb push_back

typedef long long ll;
typedef unsigned long long ull;

using namespace std;

struct data{
    int x[55];
    int idx;
};

int t, n, p;
int r[55], ptr[55], L[55], R[55];
data q[55];

bool cmp(data a, data b){
    return r[a.idx] < r[b.idx];
}

void setLR(int idx){
    double X = 1.0 * q[idx].x[ptr[idx]];
    double Y = 1.0 * r[idx];
    double lft = ceil(X / (1.1 * Y));
    double rght = floor(X / (0.9 * Y));
    L[idx] = lft, R[idx] = rght;
}

int check(){
    int lft = 1, rght = 1000000;
    int mid;
    int in = 0;
    for(int i = 1; i < n; i++){
        if(R[i] < R[in]){
            in = i;
        }
    }
    while(lft <= rght){
        mid = (lft + rght) >> 1;
        int state = 1;
        for(int i = 0; i < n; i++){
            if(mid < L[i] || mid > R[i]){
                state = 0;
                break;
            }
        }
        if(state){
            return 1;
        }else{
            if(mid > R[in]){
                rght = mid - 1;
            }else{
                lft = mid + 1;
            }
        }
    }
    return 0;
}
int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    in(t);
    for(int cases = 1; cases <= t; cases ++){
        in(n); in(p);
        for(int i = 0; i < n; i++){
            in(r[i]);
        }
        for(int i = 0; i < n; i++){
            for(int j = 0; j < p; j++){
                in(q[i].x[j]);
            }
            q[i].idx = i;
            sort(q[i].x, q[i].x + p);
        }
        sort(q, q + n, cmp);
        sort(r, r + n);
        for(int i = 0; i < n; i++){
            ptr[i] = 0;
        }
        int ans = 0;
        int ok = 1;
        while(ok){
            for(int i = 0; i < n; i++){
                setLR(i);
            }
            if(check()){
                ans++;
                for(int i = 0; i < n; i++){
                    ptr[i]++;
                    if(ptr[i] == p){
                        ok = 0;
                    }
                }
            }else{
                int in = 0;
                for(int i = 1; i < n; i++){
                    if(R[i] < R[in]){
                        in = i;
                    }
                }
                ptr[in]++;
                if(ptr[in] == p){
                    ok = 0;
                }
            }
        }
        printf("Case #%d: ",cases);
        printf("%d\n",ans);
    }
    return 0;
}
