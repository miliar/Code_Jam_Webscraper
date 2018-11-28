#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>


using namespace std;

const int N = 1500;

int dp[N][N];

int n,k;

int add(int &x,int y){
	if (y == -1) return 0;
	if (x == -1) x = y;
	else x = min(x,y);
}

string s;

int a[N];

int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("outputA.txt","w",stdout);
	ios_base::sync_with_stdio(false);
	int T; cin >> T;
	int nc = 0;
	while(T--){
		cin >> s >> k;
		n = s.length();
		for (int i =  0;i < n;i++)
			a[i + 1] = (s[i] == '+');
        //for (int i = 1;i <= n;i++) cout << a[i] << " "; cout << endl;
        int ans = 0;
        for (int i = k;i <= n;i++)
            if (a[i - k + 1] == 0)
                for (int j = i - k + 1;j <= i;j++)
                    a[j] ^= 1,ans++;
        int flag = 0;
        for (int i = 1;i <= n;i++) if (a[i] == 0) flag = 1;
		cout << "Case #"<< ++nc << ": ";
		if (flag) cout << "IMPOSSIBLE" <<endl;
		else cout << ans / k <<endl;
	}
}
