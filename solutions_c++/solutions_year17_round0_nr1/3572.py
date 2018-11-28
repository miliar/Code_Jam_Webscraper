//R.S.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> pii; 
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)
#define F2(i,a,b) for(int i=a;i<=b;i++)
#define F3(i,a,b) for(int i=a;i>=b;i--)
#define pb push_back

void flip(char &a) {
	if (a == '-')
		a = '+';
	else
		a = '-';
}

int main() {
	int T;
	cin >> T;
	F0(t,T) {
		string a;
		int k, b = 0, c = 0, d = 0;
		cin >> a >> k;
		F0(i, sz(a)) {
			if (a[i] == '-' && i < sz(a) - k + 1) {
				F0(j, k) {
					flip(a[i+j]);
				}
				c++;
			} else if (a[i] == '-') {
				d = 1;
				break;
			}
		}
		if (d)
			printf("Case #%d: IMPOSSIBLE\n", t+1);
		else
			printf("Case #%d: %d\n", t+1, c);
	}
	return 0;
}