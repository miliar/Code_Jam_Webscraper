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
	   cin>>s;
	   int n = s.size();
	   REP(i,0,n-2) {
	       if(s[i]>s[i+1]) {
	           int curr = s[i];
	           int j;
	           for(j = i-1;j>=0;j--) {
	               if(s[j]==curr) {
	                   ;
	               } 
	               else {
	                   break;
	               }
	           }
	           s[j+1]--;
	           REP(k,j+2,n-1) {
                   s[k] = '9';
               }
	       }
	   }
	   string s2;
	   int start;
	   REP(i,0,n-1) {
	       if(s[i]!='0') {
	           start = i;
	           break;
	       }
	   }
	   REP(i,start,n-1) {
	       s2 = s2+s[i]; 
	   }
	   cout<<s2<<"\n";
	}
	return 0;
}