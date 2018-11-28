#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <bitset>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef long long ll;
typedef vector<ll> vlli;

#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i!=(c).end(); i++)
#define present(c,e) ((c).find(e) != (c).end())
#define cpresent(c,e) (find(all(c),e) != (c).end())
#define REP(i,a,b) for(int i=int(a); i<=int(b); i++)

int main() {
	int T,t;
	cin>>T;
	t = 0;
	while (T--) {
	    t++;
	   cout<<"Case #"<<t<<": ";
	   string s;
	   int k;
	   cin>>s>>k;
	   int count = 0;
	   int n = s.size();
	   REP(i,0,n-k) {
	       if(s[i]=='-') {
	           count++;
	           REP(j,i+1,i+k-1) {
	               if(s[j]=='-') {
	                   s[j] = '+';
	               }
	               else {
	                   s[j] = '-';
	               }
	           }
	       }
	   }
	   int flagi = -1;
	   REP(i,n-k+1,n-1) {
	       if(s[i]=='-') {
	           flagi = 1;
	           break;
	       }
	   }
	   if(flagi==1) {
	       cout<<"IMPOSSIBLE\n";
	   }
	   else {
	       cout<<count<<"\n";
	   }
	}
	return 0;
}