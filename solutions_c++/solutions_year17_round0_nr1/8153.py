#include <bits/stdc++.h>

using namespace std;

int T, N, K, a[1050], f[1050], ans[1050];
string s;

int calc(int K){
    memset(f, 0, sizeof(f));
    int res = 0, sum = 0;
    for(int i = 0; i + K <= N; i++){
        if((a[i]+sum) % 2 != 1) {
            res++;
            f[i] = 1;
        }
        sum += f[i];
        if(i - K + 1 >= 0)sum -= f[i - K + 1];
    }

    for(int i = N - K + 1; i < N; i++){
        if((a[i]+sum) % 2 != 1)return -1;
        if(i - K + 1 >=0)sum-=f[i - K + 1];
    }
    return res;
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin >> T;
    for(int i = 1; i <= T; i++){
        cin >> s;
        N=s.length();
        for(int j = 0; j < N; j++){
            if(s[j]=='+')a[j] = 1;
            else a[j]=0;
        }
        cin >> K;
        ans[i] = calc(K);
    }
    for(int i = 1; i <= T; i++){
        if(ans[i]!=-1)cout<<"Case #"<<i<<": "<<ans[i]<<endl;
        else cout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
    }


}
