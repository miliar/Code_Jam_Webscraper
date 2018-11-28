#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<algorithm>
#include<bitset>
#include<list>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<cmath>
#include<string>
#include<cstring>
#include<sstream>
#include<climits>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> msi;

#define S(x) scanf("%d",&x)
#define SD(x) scanf("%lf",&x)
#define SL(x) scanf("%lld",&x)
#define pb(x) push_back(x)
#define mp make_pair
#define F(i, a, b) for (int i = int(a); i < int(b); i++)
#define forit(it, a) for (it = (a).begin(); it != (a).end(); it++)
#define M(x, i) memset(x,i,sizeof(x))

/* -------------------CODE GOES HERE---------------------- */

int main() {
	
	int T; S(T);
	string s;
	int n;
	int tst = 1;
	bool l;

	while(T--){
		
		l = true;
		cin>>s;
		n = s.length();

		for(int i = n-2; i >= 0; i--){
			
			if(s[i] <= s[i+1]) continue;

			s[i] = s[i] - 1;

			F(j,i+1,n){
				s[j] = '9';
			}
		}

		cout<<"Case #"<<tst++<<": ";
		F(i,0,n){
			if(l && s[i] == '0'){
				continue;
			}
			if(l && s[i] != '0'){
				l = false;
			}
			cout<<s[i];
		}
		cout<<endl;
	}
}
