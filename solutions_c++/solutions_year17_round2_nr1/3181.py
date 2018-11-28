#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

double maximum(double times[], int N){
    int etalon = 0;
    for (int j = 1; j < N; j++)
        if (times[j] > times[etalon])
            etalon = j;
    return times[etalon];
}

int main(){
    //freopen("A-large.in","r", stdin);
    //freopen("output.txt", "w", stdout);
    int cases, N, dest, k, speed;
    cin >> cases;
    for(int i = 0; i < cases; i++){
        cin >> dest >> N;
        double times[N];
        for (int j = 0; j < N; j++){
            cin >> k >> speed;
            times[j] = double(dest - k) / speed;
        }
        printf("Case #%d: %f\n", i+1, dest / maximum(times, N));
    }
    return 0;
}
