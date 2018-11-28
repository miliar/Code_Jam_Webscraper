#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <string>
#include <cstring>
#include <queue>
#include <functional>
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
	REP(caseno, 1, T) {
        cout << "Case #" << caseno << ": ";
        int N, K;
        cin >> N >> K;
        priority_queue<int> q;
        q.push(N);
        REP(i,1,K-1) {
            int x = q.top();
            q.pop();
            x--;
            int l1 = x/2;
            int l2 = x - l1;
            if (l1 > 0)
                q.push(l1);
            if (l2 > 0)
                q.push(l2);
        }
        int x = q.top();
        x--;
        int min = x/2;
        int max = x-min;
        cout << max << " " << min << "\n";
    }
	return 0;
}