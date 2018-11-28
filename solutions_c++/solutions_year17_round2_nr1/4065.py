#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
typedef struct _H{
    double loc;
    double speed;
} HORSE;
bool cmp(struct _H a, struct _H b){
    return a.loc < b.loc;
}
HORSE horse[1010];
int main() {
    int D, N;
    int T, i, j, cnt;
    
    double tot, ans, dist;
    cnt = 0;
    cin>> T;
    
    while(T--) {
        cin >> D >> N;
        for ( i = 0; i < N; i++) {
            cin >> horse[i].loc >> horse[i].speed; 
        }
        sort(horse, horse+N, cmp);
        horse[N].loc = D;
        tot = 0;
        double ttime;
        
        for (i = N-1; i >= 0; i--) {
            ttime = (D - horse[i].loc) / horse[i].speed;
            if ( tot < ttime )
                tot = ttime;
            
           // cout << ttime<<'*'<<tot << endl;
            
            //horse[i].speed
            //tot horse
           
        }
        ans = (double)D / tot;
        // for (i = 0; i < N; i++) {
        //     cout << horse[i].loc <<"*"<< horse[i].speed<<endl; 
        // }
       
        cout <<"Case #"<<++cnt <<": ";
        printf("%.6f\n", ans);
        
    }
    return 0;
}
