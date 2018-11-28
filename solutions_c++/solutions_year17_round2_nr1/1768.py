#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <cstdio>
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
	    int d;
	    int N;
	    cin>>d>>N;
	    double max = -1;
	    REP(i,0,N-1) {
	        int a,b;
	        cin>>a>>b;
	        double x = ((double)(d-a))/b;
	        if(x>max) {
	            max = x;
	        }
	    }
	    //cout<<d/max<<"\n";
	    printf("%.7lf\n",d/max);
	}
	return 0;
}
