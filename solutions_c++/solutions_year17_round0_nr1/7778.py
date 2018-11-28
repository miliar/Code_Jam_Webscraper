#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(i=a;i<b;++i)
#define repi(i,a,b) for(int i=a;i<b;++i)
#define F first
#define S second
#define mp(a,b) make_pair(a,b)
#define pii pair<int,int>
#define ppi pair<pii,int>
#define ppp pair<pii,pii>
#define vi vector<int>
#define sc(a) scanf("%d",&a)
#define pb(a) push_back(a)
#define pr(a) printf("%d",a)
#define prn(a) printf("%d\n",a)
#define scll(a) scanf("%lld",&a)
#define prll(a) printf("%lld",a)
#define prlln(a) printf("%lld\n",a)
typedef long long LL;

int main() {
	// your code goes here
	int t;
	cin>>t;
	string x;
	repi(cc,1,t+1) {
		int k;
		cin >> x >> k;
		int b = 1;
		int sw = 0;
		for(int i = 0 ; i < x.size();++i ) {
			int j = i;
			if(x[i] == '-' && i+k <= x.size()) {
				while(j < i+k) {
					if(x[j]=='-') x[j] = '+';
					else x[j] = '-';
					++j;
				}
				++ sw;
				
			//	cout << i << endl;
			}
			if(x[i] == '-') b= 0;
		}
		cout << "Case #"<<cc<<": ";
		if(b==0) cout<<"IMPOSSIBLE" << endl;
		else cout << sw << endl;
	}
	return 0;
}