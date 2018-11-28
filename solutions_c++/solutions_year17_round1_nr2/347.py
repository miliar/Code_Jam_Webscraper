#include <bits/stdc++.h>
#define EPS 1e-7
using namespace std;

int t,n,p,x;
char ch;
int r[100];
int r2[100];


int main() {
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&t);
    for(int tc = 1; tc <= t; tc++){
        int sol = 0;
        scanf("%d%d",&n,&p);
        vector<multiset<int>> q(n);
        for(int i = 0; i < n; i++) scanf("%d",&r[i]);
        for(int i = 0; i < n; i++){
            for(int j = 0; j < p; j++){
                scanf("%d",&x);
                q[i].insert(x);
            }
        }
        vector<int> erased(n,-1);
        for(int k : q[0]){
            bool found = 1;
            int R = floor(k/((double)r[0]*0.9));
            int L = ceil(k/((double)r[0]*1.1));
            if(L > R) continue;
            for(int i = 1; i < n; i++){
                bool found2 = 0;
                for(int j : q[i]){
                    int R2 = floor(j/((double)r[i]*0.9));
                    int L2 = ceil(j/((double)r[i]*1.1));
                    if(L2 > R || L > R2) continue;
                    L = max(L,L2);
                    R = min(R,R2);
                    found2 = 1;
                    q[i].erase(q[i].find(j));
                    erased[i] = j;
                    break;
                }
                if(!found2){
                    found = 0;
                    break;
                }
            }
            if(found) sol++;
            else{
                for(int i = 0; i < n; i++){
                    if(erased[i] != -1) q[i].insert(erased[i]);
                }
            }
        }
        printf("Case #%d: %d\n",tc,sol);
    }
}