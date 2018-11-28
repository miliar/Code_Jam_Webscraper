/* Author : Jordhy Fernando */
#include<bits/stdc++.h>
#define ll long long
#define For(i,j,n) for(int i = j; i < n; i++)
#define EPS 1e-12

using namespace std;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

int main(){
    int T;
    cin >> T;
    for(int i = 1; i <= T; i++) {
        ll pembagi = 1;
        ll ans;
        ll N, K;
        cin >> N >> K;
        while((pembagi << 1) <= K){
            pembagi = pembagi << 1;
        }
        ans = (N - K) / pembagi;
        cout << "Case #" << i << ": ";
        if(ans % 2 == 0){
            cout << ans/2 << " " << ans/2 << endl;
        }
        else{
            cout << ans/2 + 1 << " " << ans/2 << endl;
        }
    }
	return 0;
}
