#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <utility>

using namespace std;


int T, N, K;
int R[1007], H[1007];
long double  h[1007], a[1007];
pair<long double, int> p[1007];


int main(){

    cin >> T;
    for(int t = 1; t <= T; t++){

        long double answer = 0.0;
        long double pi = 3.141592653589793;
        
        cout.precision(30);

        cin >> N >> K;
        for(int i = 0; i < N; i++){
            cin >> R[i] >> H[i];
            p[i] = make_pair(pi * H[i] * R[i] * 2, i);;
            h[i] = p[i].first;
            a[i] = pi * R[i] * R[i];
        }
        sort(p, p+N);
        for(int i = 0; i <= (N/2)-1; i++){
            pair<long double, int> temp = p[i];
            p[i] = p[N-i-1];
            p[N-i-1] = temp;
        }

        long double maxS = a[p[0].second];
        int maxSI = 0;
        for(int i = 0; i < K; i++){
            answer += p[i].first;
            if(maxS < a[p[i].second]){
                maxS = a[p[i].second];
                maxSI = p[i].second;
            }
        }
        answer += maxS;

        //now we possibly have to make one chage
        for(int i = K; i < N; i++){
            if(h[p[i].second]+a[p[i].second] > h[p[K-1].second] + maxS){
                answer = answer - maxS - h[p[K-1].second];
                maxS = a[p[i].second];
                p[K-1] = make_pair(h[p[i].second], p[i].second);
                answer = answer + maxS + h[p[i].second];
            }
        }


        cout << "Case #" << t << ": " << answer << endl;


        
    }


    return 0;
}

