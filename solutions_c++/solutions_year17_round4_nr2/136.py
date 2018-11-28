#include<cstdio>
#include<map>
#include<algorithm>
#include<cstring>
using namespace std;

const int MAX = 1000 + 10;
int p[MAX], b[MAX];
int s[MAX];
int n, c, m;

bool check(int x) {
    int sum = 0;
    for(int i = 1 ; i <= n ; i++) {
        sum += s[i];
        if(sum > i * x) return false;
    }
    return true;
}

int main() {
    int TN;
    scanf("%d", &TN);
    for(int casen = 1 ; casen <= TN ; casen++) {
        memset(s, 0, sizeof(s));
        printf("Case #%d: ", casen);
        int l = 0, r = 1000000000;
        scanf("%d %d %d", &n, &c, &m);
        map<int,int> mt;
        for(int i = 0 ; i < m ; i++) {
            scanf("%d %d", &p[i], &b[i]);
            s[p[i]]++;
            mt[b[i]]++;
            l = max(l, mt[b[i]]);
        }
        while(l < r) {
            int mid = (l+r)/2;
            if(check(mid)) {
                r = mid;
            } else {
                l = mid+1;
            }
        }
        int ss = 0;
        for(int i = 1 ; i <= n ; i++) {
            if(s[i] > l) ss += s[i] - l;
        }
        printf("%d %d\n", l, ss);
    }      
    return 0;
}
