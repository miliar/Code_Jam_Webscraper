#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    for (int t=1; t<=T; t++) {
        int res=0;
        int n, p;
        scanf("%d%d", &n, &p);
        vector<int> v(4);
        for (int i=0; i<n; i++) {
            int x;
            scanf("%d", &x);
            v[x%p]++;
        }
        res=v[0];
        if (p==2) {
            res+=(v[1]+1)/2;
        } else if (p==3) {
            if (v[1]>v[2]) swap(v[1], v[2]);
            res+=v[1];
            v[2]-=v[1];
            res+=(v[2]+2)/3;
        } else {
            if (v[1]>v[3]) swap(v[1], v[3]);
            res+=v[1];
            v[3]-=v[1];
            res+=v[2]/2;
            v[2]%=2;            
            res+=v[3]/4;
            v[3]%=4;            
            if (v[2] || v[3]) res++;
            if (v[2]==1 && v[3]==3) res++;
        }

        printf("Case #%d: %d\n", t, res);
    }
}

