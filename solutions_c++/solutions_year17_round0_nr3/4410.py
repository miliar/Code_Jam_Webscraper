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
	   ll N,k;
	   cin>>N>>k;
	   map<ll,int> count;
	   count[N] = 1;
	   REP(i,0,k-2) {
	       typeof(count.rbegin()) it = count.rbegin();
	       ll maxv = it->first;
	       ll left = (maxv-1)/2;
	       ll right = (maxv)/2;
	       if(present(count,left)) {
	       		count[left]++;
	       }
	       else {
	       		count[left] = 1;
	       } 

	       if(present(count,right)) {
	       		count[right]++;
	       }
	       else {
	       		count[right] = 1;
	       } 
	       if(count[maxv]==1) {
	       		count.erase(maxv);
	       }
	       else {
	       		count[maxv]--;
	       }
	   }
	   typeof(count.rbegin()) it = count.rbegin();
       ll maxv = it->first;
       ll left = (maxv-1)/2;
       ll right = (maxv)/2;
       cout<<right<<" "<<left<<"\n";
	}
	return 0;
}