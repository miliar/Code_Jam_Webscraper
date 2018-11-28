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

bool tidy(int n) {
	int last = n%10;
	n/=10;
	while(n) {
		if(n%10 > last) return false;
		last = n%10;
		n/=10;
	}
	return true;
}

int get(int n) {
  	int ans;
  	FOR(i,1,n) if(tidy(i)) ans=i;
  	return ans;
}
int main()
{
    freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);
    int t;cin>>t;
    FOR(it,1,t) {
    	cerr<<it<<endl;
    	int n;
    	cin>>n;
    	int ans = get(n);
    	cout<<"Case #"<<it<<": "<<ans<<endl;
    }
}
