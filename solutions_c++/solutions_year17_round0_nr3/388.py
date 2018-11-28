#include <bits/stdc++.h>
using namespace std;

long long t1, t2;
long long N, K;

int ans(){
    if(K == N){
        t1 = 0;
        t2 = 0;
        return 0;
    }

    long long n = N - 1;
    long long a = n / 2;
    long long b = n - a;

    long long k = K - 1;
    long long ka = k / 2;
    long long kb = k - ka;

    if(K == 1){
        t1 = b;
        t2 = a;
        return 0;
    }

    if(K == 2){
        N = b;
        K = 1;
        ans();
        return 0;
    }

    if(n % 2 == 0){
        N = b;
        K = kb;
        ans();
        return 0;
    }else{
        if (k % 2 == 0){
            N = a;
            K = ka;
            ans();
            return 0;
        }else{
            N = b;
            K = kb;
            ans();
            return 0;
        }
    }
}

int main(){

    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

    int T;
    cin >> T;
    for(int c=1;c<=T;c++){
        cin >> N >> K;
        ans();
        cout << "Case #" << c << ": " << t1 << " " << t2 << endl;
    }
}
