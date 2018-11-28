#include<bits/stdc++.h>
#define lli long long int
#define test()  int test;cin>>test;while(test--)
const lli MOD = 1000000007ll;

using namespace std;

int main() {
  	freopen("in", "r", stdin);
  	freopen("out", "w", stdout);
	std::ios_base::sync_with_stdio(false);
  	int tt;
  	cin >> tt;
  	for (int qq = 1; qq <= tt; qq++) {
    	cout << "Case #" << qq << ": ";
    	int n,r,o,y,g,b,v;
    	cin >> n >> r >> o >> y >> g >> b >> v;
    	int l = max(max(r,y),b);
    	if(l>n/2){
    	    cout << "IMPOSSIBLE\n";
    	    continue;
    	}
    	int ar[n];
    	int st[3];
    	st[0]=r;
    	st[1]=y;
    	st[2]=b;
    	sort(st,st+3);
    	int p=0;
    	for(int i=2;i>=0;i--){
    	    if(st[i]==r){
    	        for(int i=0;i<r;i++){
    	            ar[p] = 1;
    	            p+=2;
    	            if(p>=n){
    	                p=1;
    	            }
    	        }
    	        r=-1;
    	    }
    	    if(st[i]==y){
    	        for(int i=0;i<y;i++){
    	            ar[p] = 2;
    	            p+=2;
    	            if(p>=n){
    	                p=1;
    	            }
    	        }
    	        y=-1;
    	    }
    	    if(st[i]==b){
    	        for(int i=0;i<b;i++){
    	            ar[p] = 3;
    	            p+=2;
    	            if(p>=n){
    	                p=1;
    	            }
    	        }
    	        b=-1;
    	    }
    	}
    	for(int i=0;i<n;i++){
    	    if(ar[i]==1){
    	        cout << "R";
    	    }
    	    else if(ar[i]==2){
    	        cout << "Y";
    	    }
    	    else{
    	        cout << "B";
    	    }
    	}
    	cout << endl;
    	
    }
  return 0;
}
