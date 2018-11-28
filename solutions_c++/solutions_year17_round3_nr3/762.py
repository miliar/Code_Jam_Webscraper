#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
using namespace std;
int N, K;
double p[55], U;
double ABS(double x){
    return (x>0)?(x):(-x);
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int T;
    cin >> T;
    for(int f = 1; f <= T; f++){
        cin >> N >> K;
        cin >> U;
        for(int i = 0; i < N; i++){
            cin >> p[i];
        }
        p[N] = 1.0;
        double ans;
        if(N == 1){
            ans = min(p[0] + U, 1.0);
        }else{
            while(U > 1e-8){
                sort(p, p+N);
                int cur = 1;
                while(ABS(p[cur] - p[cur-1]) < 1e-8) cur++;
                if(U >= (p[cur] - p[cur-1]) * (double) cur){
                    double plus = p[cur] - p[cur-1];
                    for(int i = 0; i < cur; i++){
                        p[i] += plus;
                    }
                    U -= plus * (double) cur;                    
                }else{
                    double plus = U / (double) cur;
                    for(int i = 0; i < cur; i++){
                        p[i] += plus;
                    }
                    break;
                }
            }
            ans = 1.0;
            for(int i = 0; i < N; i++){
                ans *= p[i];
            }

        }
        cout << "Case #" << f << ": ";
        printf("%.10f\n", ans);
    }

    return 0;
}
