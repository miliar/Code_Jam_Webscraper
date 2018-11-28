#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <utility>
#include <queue>
#include <map>
using namespace std;

typedef long long LL;
typedef unsigned int UINT32;

string calc()
{
    LL N, K;
    cin >> N >> K;

    map<LL, LL> m;
    m[-N] = 1;
    while (K > 1) {
        map<LL, LL>::iterator it = m.begin();
        LL n = -it->first;
        if (it->second >= K) {
            break;
        }

        LL a = n / 2;
        LL b = n / 2 - int(n%2==0);
        K -= it->second;
        m[-a] += it->second;
        m[-b] += it->second;
        m.erase(it);
    }

    map<LL, LL>::iterator it = m.begin();
    LL n = -it->first;
    LL a = n / 2;
    LL b = n / 2 - int(n%2==0);

    //string line;
    //getline(cin, line);

    stringstream S;
    S << a << ' ' << b;
    return S.str();
}

int main(void)
{
	int N;
	cin >> N;

    // NOTE: if using getline() to read the input, the following two lines should be
    // added to read the line sepeartor in the first line. 
    //string line;
    //getline(cin, line);
	for (int i=1; i<=N; ++i) {
		cout << "Case #" << i << ": " << calc() << endl;
	}

	return 0;
}
