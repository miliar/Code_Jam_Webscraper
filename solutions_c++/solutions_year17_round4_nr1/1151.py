#include <bits/stdc++.h>
 
#define gc getchar
#define ii(x) scanf(" %d", &x)
#define ill(x) scanf(" %lld", &x)
#define ll long long
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define all(x) x.begin(),x.end()
#define fill(a,b) memset(a, b, sizeof(a))
#define rep(i,a,b) for(i=a;i<b;i++)
#define per(i,a,b) for(i=a;i>=b;i--)
#define pii pair<int, int>
 
using namespace std;
 
void in(int &x){
    register int c=gc();
    x=0;
    for(;(c<48||c>57);c=gc());
    for(;c>47&&c<58;c=gc()){x=(x<<1)+(x<<3)+c-48;}
}

int a[105], cnt[5];

int main()
{
	int t, n, i, j, p, tt;
	cin >> t; rep(tt, 1, t + 1){
		cin >> n >> p;
		fill(cnt, 0);
		rep(i, 0, n){
			cin >> a[i];
			a[i] %= p;
			cnt[a[i]]++;
		}
		//rep(i, 0, p) cout << cnt[i] << " "; cout << endl;
		int ret = cnt[0];
		if(p == 2){
			ret += cnt[1] / 2;
			cnt[1] %= 2;
			if(cnt[1]) ret++;
		}else if(p == 3){
			if(cnt[1] <= cnt[2]){
				ret += cnt[1];
				cnt[2] -= cnt[1];
				cnt[1] = 0;
				ret += cnt[2] / 3;
				cnt[2] %= 3;
				if(cnt[2]) ret++;
			}else{
				ret += cnt[2];
				cnt[1] -= cnt[2];
				cnt[2] = 0;
				ret += cnt[1] / 3;
				cnt[1] %= 3;
				if(cnt[1]) ret++;
			}
		}else{
			ret += cnt[2] / 2;
			cnt[2] %= 2;
			if(cnt[1] <= cnt[3]){
				ret += cnt[1];
				cnt[3] -= cnt[1];
				cnt[1] = 0;
				ret += cnt[3] / 4;
				cnt[3] %= 4;
				if(cnt[2]) ret += cnt[3] == 3 ? 2 : 1;
				else if(cnt[3]) ret++;
			}else{
				ret += cnt[3];
				cnt[1] -= cnt[3];
				cnt[3] = 0;
				ret += cnt[1] / 4;
				cnt[1] %= 4;
				if(cnt[2]) ret += cnt[1] == 3 ? 2 : 1;
				else if(cnt[1]) ret++;
			}
		}
		cout << "Case #" << tt << ": " << ret << endl;
	}

	return 0;
}