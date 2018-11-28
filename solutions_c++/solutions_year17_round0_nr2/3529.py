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

void dec(char &a) {

}

int main() {
	int T;
	cin >> T;
	F0(t,T) {
		printf("Case #%d: ", t+1);

		string a;
		cin >> a;

		int flag;
		do {
			flag = 0;
			F0(i, sz(a)) {
				if (flag == 0 && i < sz(a)-1 && a[i] > a[i+1]){
					a[i]--;
					flag = 1;
				} else if (flag == 1) {
					a[i] = '9';
				}
			}
		} while (flag == 1);

		int i = 0;
		while (a[i] == '0') i++;
		cout << a.substr(i);

		printf("\n");
	}
	return 0;
}