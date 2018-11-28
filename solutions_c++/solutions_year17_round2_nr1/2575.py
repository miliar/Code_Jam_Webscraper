#include <bits/stdc++.h>
using namespace std;

int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);

    int T, D, N;
    int K[2000], S[2000];

    cin >> T;
    for(int t = 0; t < T; t++){
        cin >> D >> N;
        double time = 0;
        double maxTime = 0;
        for(int n = 0; n < N; n++){
            cin >> K[n] >> S[n];
            time = (D-K[n])*1.0/S[n];
            if(maxTime < time){
                maxTime = time;
            }
        }
        printf("Case #%d: %.6f\n", t+1, D*1.0/maxTime);
    }


    return 0;
}
