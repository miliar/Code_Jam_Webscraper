#include <bits/stdc++.h>

using namespace std;

#define fi first
#define se second

typedef pair<int, int> ii;
typedef pair<int, ii> iii;

int main(){
    int t, n, k, l, r, d;

    scanf("%d", &t);

    for( int tc = 1; tc <= t; tc++ ){
        scanf("%d %d", &n, &k);

        priority_queue<iii> pq;

        l = n/2, r = n/2;
        if ( n % 2 == 0 ){
            l--;
        }

        pq.push(iii(max(l, r), ii(l, r)));
        pq.push(iii(min(l, r), ii(l, r)));

        for( int j = 1; j < k; j++ ){
            iii info = pq.top();

            d = info.fi;
            l = info.se.fi;
            r = info.se.se;

            pq.pop();

            l = d/2;
            r = d/2;
            if ( d % 2 == 0 ){
                l--;
            }
            pq.push(iii(max(l, r), ii(l, r)));
            pq.push(iii(min(l, r), ii(l, r)));
            
        }
        
        printf("Case #%d: %d %d\n", tc, max(l,r), min(l, r));
    }
    
}