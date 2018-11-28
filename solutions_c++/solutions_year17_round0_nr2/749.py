#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const int N = 1100;
int t, cas = 1;
int p[N], cnt;
ll n;

void solve(){
    cnt = 0;
    while(n > 0){
        p[cnt++] = (n % 10);
        n /= 10;
    }

    p[cnt] = 0;
    for(int i=0;i<cnt;i++){
        if(p[i] < p[i+1]){
            p[i+1]--;
            for(int j=i;j>=0;j--) p[j] = 9;
        }
    }

    int k = cnt;
    while(p[k] == 0) k--;
    for(int i=k;i>=0;i--) cout << p[i];
    cout << endl;

}

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    while(t--){
        cin >> n;
        printf("Case #%d: ", cas++);
        solve();
    }
	return 0;
}

