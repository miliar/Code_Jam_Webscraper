#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int T;
    cin >> T;

    long long int D, N;
    long long int K, S;
    for(int f = 1; f <= T; f++){
        cin >> D >> N;
        double t = 0.0, ans;
        for(int i = 0; i < N; i++){
            cin >> K >> S;
           double v = (double) (D - K) / S;
            if(v > t){
                t = v;
            }
        }
        ans = (double) D / t;
        cout << "Case #" << f << ": ";
        printf("%.8lf\n", ans);
    }

    return 0;
}
