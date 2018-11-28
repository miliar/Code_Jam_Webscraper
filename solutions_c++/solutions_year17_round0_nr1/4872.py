#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <numeric>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define showv(v) For(i, v) { cout << *i << ' ';} cout << endl;
#define maxv(v) *max_element(all(v))
#define minv(v) *min_element(all(v))

typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<char> vc;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef vector<vector<char> > vcc;
typedef vector<bool> vb;
typedef long long ll;
typedef long double ld;

vi converter (string signs) {

    vi resultList;
    // cout << signs.length() << endl;
    for (int i=0; i < signs.length(); i++) {
        if (signs[i] == '+')
            resultList.pb(1);
        else
            resultList.pb(0);
    }
    return resultList;
}

void flipper(vi numbers, int K) {
    
    int flipFlag=1, flipCount=0;//, lastSign = numbers[0];

	while (flipFlag==1) {
		flipFlag=0;
		for (int i=0; i < numbers.size()-(K-1); i++) {
			if (numbers[i]==0) {
				rep2 (j, i, i+K) { numbers[j]=!(numbers[j]); }
				flipFlag=1;
				flipCount++;
			}
		}
	}
	if (accumulate(all(numbers),0) < numbers.size())
		cout << "IMPOSSIBLE" << endl;
	else
    	cout << flipCount << endl;

}

int N;
int main(int argc, char *args[]) {
    if (argc == 2 && strcmp(args[1], "small") == 0) {
        freopen("small.in","rt",stdin);
        freopen("small.out","wt",stdout);
    }
    else if (argc == 2 && strcmp(args[1], "large") == 0) {
        freopen("large.in","rt",stdin);
        freopen("large.out","wt",stdout);
    }
    else {
	    freopen("test-in.txt", "rt", stdin);
        freopen("test-out.txt", "wt", stdout);
    }
    
    cout << setprecision(6) << fixed;
    
    cin>>N;
    rep2(nn,1,N+1) {

    	// vector<int> numbers;

    	string signList; cin >> signList;
    	int K; cin >> K;

        printf("Case #%d: ", nn);

        flipper(converter(signList), K);
    }
	
    return 0;
}