#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <string>
#include <cstring>
#include <queue>
#include <algorithm>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef long long int ll;

#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i!=(c).end(); i++)
#define present(c,e) ((c).find(e) != (c).end())
#define cpresent(c,e) (find(all(c),e) != (c).end())
#define REP(i,a,b) for(int i=int(a); i<=int(b); i++)
#define mp make_pair
#define ff first
#define ss second

int main() {
	int T;
	cin >> T;
	REP(caseno,1,T) {
        string s;
        int K;
        cin >> s >> K;
        int N = s.length();
        int flips = 0;
        REP(i, 0, N-K) {
            if (s[i] == '-') {
                flips++;
                REP(j,0,K-1) {
                    s[i+j] = (s[i+j]=='-')?'+':'-';
                }
            }
        }
        bool possible = true;
        REP(i, N-K, N-1) {
            if (s[i] == '-') {
                possible = false;
                break;
            }
        }
        cout << "Case #" << caseno << ": ";
        if (possible) cout << flips << "\n";
        else cout << "IMPOSSIBLE" << "\n";
    }
	return 0;
}   