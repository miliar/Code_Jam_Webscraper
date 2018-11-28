#include <bits/stdc++.h>
#define pb push_back
#define mk make_pair
#define fi first
#define se second
#define For(i,a,b) for(int (i)=(a);(i) < (b); ++(i))
using namespace std;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef long long ll;
typedef vector<bool> vb;
const int N=100;

int n, p, a[N];

int main(void) {
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	For(tt, 1, 1+T) {
		cin >> n >> p;
		vi isr(n+1,0);
		int ans=0;
		//cout << p << endl;
		for (int i = 0; i<n; i++) {
			cin >> a[i];
			if (a[i]%p==0) {
				isr[i]=1;
				ans++;
			}
		}


		for (int i = 0; i<n ;i++)  
			for (int j = i+1; j<n; j++){
				if (!isr[i] && !isr[j] && (a[j] + a[i]) % p == 0) {
					isr[i] = isr[j] = 1;
				//	cout << i << " " << j << endl;
					ans++;
				}
			}

		for (int i = 0; i<n ;i++) if(!isr[i])
			for (int j = i+1; j<n; j++) if(!isr[j])
				for (int k = j+1; k<n; k++) if (!isr[k])
					if (!isr[i] && !isr[j] && !isr[k] && (a[i]+a[j]+a[k])%p == 0) {
						isr[i]=isr[j]=isr[k]=1;
						ans++;
					}

		for (int i = 0; i<n ;i++) if(!isr[i])
			for (int j = i+1; j<n; j++) if(!isr[j])
				for (int k = j+1; k<n; k++) if (!isr[k])
					for (int h = k+1; h<n; h++) if (!isr[h]) {
						if ( !isr[i] && !isr[j] && !isr[k] && !isr[h] && (a[i]+a[j]+a[k]+a[h])%p == 0) {
							isr[i]=isr[j]=isr[k]=isr[h] = 1;
							ans++;
						}
					}

		for (int i = 0; i<n; i++)
			if (!isr[i]) {ans++; break;}

		cout << "Case #" << tt <<": ";
		cout << ans << "\n";

	}
	
	
	return 0;
}
