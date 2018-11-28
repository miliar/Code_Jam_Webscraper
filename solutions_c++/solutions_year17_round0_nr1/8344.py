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
    	string s;
    	int k;
    	cin>>s>>k;
    	int ans=0;
    	FOR(i,0,sz(s)-k) if(s[i]=='-') {
    		ans++;
    		FOR(j,i,i+k-1) s[j]='-'+'+'-s[j];
    	} 
    	bool ok=true;
    	FOR(i,0,sz(s)-1) if(s[i]=='-') ok=false;
    	cout<<"Case #"<<it<<": ";
    	if(ok) cout<<ans<<endl; else cout<<"IMPOSSIBLE"<<endl;
    }
}
