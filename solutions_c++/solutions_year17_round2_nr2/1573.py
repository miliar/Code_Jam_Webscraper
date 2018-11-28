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
        int flag = -1;
	    t++;
	    cout<<"Case #"<<t<<": ";
	    int N;
	    cin>>N;
	    vi v(12,-1);
	    REP(i,0,5) {
	        cin>>v[i];
	    }
	    vi ans(N,-1);
	    int index = -1;
        int max = -1;
        REP(j,0,5) {
           if(v[j]>max) {
               max = v[j];
               index = j;
           }
        }
       ans[0] = index;
       v[index]--;
	    REP(i,1,N-1) {
	       int index = -1;
	       int max = 0;
	       for(int k = 0;k<=5;k++) {
	           int j = (ans[0]+k)%6;
	           if(j==ans[i-1]) continue;
	           if(v[j]>max) {
	               max = v[j];
	               index = j;
	           }
	       }
	       if(index==-1) {
		        flag = 1;
		        break;
	       }
	       ans[i] = index;
	       v[index]--;
	    }
	    if(flag == 1) {
			cout<<"IMPOSSIBLE\n";
			continue;
	    }
	    char array[6] = {'R','O','Y','G','B','V'};
	    string s(N,'\0');
	    REP(i,0,N-1) {
	        s[i] = array[ans[i]];
	    }
	    if(s[N-1]==s[0]) {
			cout<<"IMPOSSIBLE\n";
	    }
	    else {
	        cout<<s<<"\n";
	    }
	}
	return 0;
}