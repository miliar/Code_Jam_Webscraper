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
	REP(caseno, 1, T) {
		string str;
		cin >> str;
		cout << "Case #" << caseno << ": ";
		int N = str.length();
		int changedIdx = -1;
		for (int i = N-1; i >= 1; i--) {
			if (str[i-1] > str[i]) {
				str[i-1]--;
				str[i] = '9';
				changedIdx = i;
			}
		}
		if (changedIdx != -1) {
			REP(i, changedIdx, N-1) {
				str[i] = '9';
			}
		}
		int idx = 0;
        while (idx < N && str[idx] == '0') idx++;
        cout << str.substr(idx) << "\n";
		//cout << str << "\n";
	}
	return 0;
}