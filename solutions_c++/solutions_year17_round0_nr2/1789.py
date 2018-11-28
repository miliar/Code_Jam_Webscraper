#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

#define For(i,a,b)  for(int i=(a);i<(b);++i)
#define rep(i,n)    For(i,0,(n))

string solve()
{
	string N;

	cin >> N;

	bool retry;
	do {
		retry = false;
		rep(i, N.size() - 1) {
			if(N[i] > N[i+1]) {
				--N[i];
				For(j, i + 1, N.size()) {
					N[j] = '9';
				}
				retry = true;
				break;
			}
		}
	} while(retry);

	if(N[0] == '0')
		return N.substr(1);
	else
		return N;
}

int main()
{
	int T;
	cin >> T;

	rep(i, T)
		cout << "Case #" << (i + 1) << ": " << solve() << endl;
}
