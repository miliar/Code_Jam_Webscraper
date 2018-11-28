#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
using namespace std;
struct S{
    double r, h;
}data[1010], tmp[1010];
bool cmp(S a, S b){
    return a.h * a.r > b.h * b.r;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int T;
    cin >> T;
    
    int n, k;
    for(int f = 1; f <= T; f++){
        cin >> n >> k;
        for(int i = 0; i < n; i++){
            cin >> data[i].r >> data[i].h;
        }
        double ans = 0.0;
        for(int i = 0; i < n; i++){
            int tc = 0;
            for(int j = 0; j < n; j++){
                if(i != j && data[i].r >= data[j].r){
                    tmp[tc++] = data[j];
                }
            }
            if(tc < k-1){
                continue;
            }
            sort(tmp, tmp + tc, cmp);
            double tans = data[i].r * data[i].r * M_PI + 2.0 * M_PI * data[i].r * data[i].h;
            for(int j = 0; j < k - 1; j++){
                tans += 2.0 * M_PI * tmp[j].r * tmp[j].h;
            }
            if(tans > ans){
                ans = tans;
            }
        }

        cout << "Case #" << f << ": ";
        printf("%.10f\n", ans);
    }

    return 0;
}
