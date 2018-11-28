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

int main() {
	int T;
	cin >> T;
	F0(t,T) {
		printf("Case #%d: ", t+1);

		priority_queue<int> Q;
		int n, k;
		cin >> n >> k;
		Q.push(n);

		F0(i, k) {
			int a = Q.top();
			Q.pop();
			if (a % 2 == 1) {
				if(i == k-1) printf("%d %d", (a - 1)/2, (a - 1)/2);
				if ((a - 1)/2 > 0) {
					Q.push((a - 1)/2);
					Q.push((a - 1)/2);
				}
			} else {
				if(i == k-1) printf("%d %d",  a/2, a/2 - 1);
				Q.push(a/2);
				if (a/2 - 1 > 0) Q.push(a/2 - 1);
			}
		}

		printf("\n");
	}
	return 0;
}