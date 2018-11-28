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
	int t;
	cin>>t;
	string x;
	repi(cc,1,t+1) {
		cin >> x;
		for(char &p : x) p -= '0';
		for(int i = 0; i < x.size()-1;++i) {
			if(x[i] > x[i+1]) {
				int j = i;
				while(j >= 0 && x[j] == x[i]) j--;
				++j;
				x[j]--;
				for(i=j+1; i <x.size();++i) x[i] = 9;

				break;
			}
		}
		int b = 0;
		cout << "Case #"<<cc<<": ";
		for(char p : x) {
			if(p!=0 && b==0) {
				cout<<char(p+'0');
				b=1;
			} else if(b==1) {
				cout<<char(p+'0');
			}
		}
		cout << endl;
	}
	return 0;
}