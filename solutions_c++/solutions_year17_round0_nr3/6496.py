#include <iostream>
#include <vector>
#include <algorithm>
#include <string.h>
#include <set>

using namespace std;
#define sz(s) (int)((s).size())
#define FOR(i,a,b) for(int i=a; i<=b; ++i)
#define pb push_back
#define mp make_pair

typedef long long Int;

pair<int,int> get(int n, int k) {
  	pair<int,int> ans;
  	multiset<int> x;
  	x.insert(-n);
  	FOR(iter,1,k) {
  		int f = -*x.begin();
  		x.erase(x.begin());
  		int len1 = f/2;
  		int len2 = (f-1)/2;
  		ans = mp(len1, len2);
  		x.insert(-len1);
  		x.insert(-len2);
  	}
  	return ans;
}
int main()
{
    freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);
    int t;cin>>t;
    FOR(it,1,t) {
    	cerr<<it<<endl;
    	int n,k;
    	cin>>n>>k;
    	pair<int,int> ans = get(n,k);
    	cout<<"Case #"<<it<<": "<<ans.first<<" "<<ans.second<<endl;
    }
}
