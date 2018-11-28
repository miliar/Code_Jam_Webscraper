#include <bits/stdc++.h>
#define PI 3.14159265358
using namespace std;

struct Cake{
    double r;
    double h;
}cake[1005];

bool cmp_beside(const Cake &a, const Cake &b){
    if((a.r)*(a.h)!=(b.r)*(b.h))
        return (a.r)*(a.h)>(b.r)*(b.h);
    else
        return (a.r)>(b.r);
}

bool cmp_r(const Cake &a, const Cake &b){
    return (a.r)>(b.r);
}

int main(){
    //ios_base::sync_with_stdio(false);
    //cin.tie(0);
    freopen("A-large.in", "r", stdin);
    freopen("output_a.txt", "w", stdout);
    int T, n, k;
    double sur, maxr;
    cin >> T;
    for(int t=1; t<=T; ++t){
        sur = 0;
        maxr = 0;
        cin >> n >> k;
        for(int i=0; i<n; ++i){
            cin >> cake[i].r >> cake[i].h;
        }
        sort(cake, cake+n, cmp_beside);
        for(int i=0; i<k; ++i){
            sur += 2 * PI * cake[i].r * cake[i].h;
            if( cake[i].r > maxr){
                maxr = cake[i].r;
            }
        }
        //sort(cake, cake+k, cmp_r);
        sort(cake+k, cake+n, cmp_r);
//        for(int i=0; i<k; ++i){
//            cout << cake[i].r <<" "<< cake[i].h <<"\n";
//        }
        sur += PI *maxr* maxr;
            double diff = 0;
            int idx = -1;
            for(int i=k; i<n; i++){
                if( cake[i].r > maxr && diff < (cake[i].r)*(cake[i].r)*PI-maxr*maxr*PI + 2*PI*cake[i].r*cake[i].h-2*PI*cake[k-1].r*cake[k-1].h ){
                    diff = (cake[i].r)*(cake[i].r)*PI-maxr*maxr*PI + 2*PI*cake[i].r*cake[i].h-2*PI*cake[k-1].r*cake[k-1].h;
                    idx = i;
                }
            }
            if(idx != -1) sur += diff;
            cout.precision(10);
        cout << "Case #" << t << ": " << fixed << sur << "\n";
    }
    return 0;
}
