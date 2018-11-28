#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <vector>
#include <sstream>
#include <stack>
#include <queue>
#include <map>
#include <climits>
#include <cstdio>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <iomanip>
#include <functional>
using namespace std;
#define db(a) (cout << (#a) << " = " << (a) << endl)
typedef long long ll;

ll K[1024];
ll S[1024];

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int T;
	cin>>T;
	for(int t=0;t<T;t++)
	{
		ll D,N;
		cin>>D>>N;
		for(ll i=0;i<N;i++) cin>>K[i]>>S[i];
		double erg = static_cast<double>(D-K[0])/static_cast<double>(S[0]);
		for(ll i=1;i<N;i++) erg = max(erg, static_cast<double>(D-K[i])/static_cast<double>(S[i]));
		erg = static_cast<double>(D) / erg;
		cout << "Case #" << t+1 << ": " << fixed << setprecision(6) << erg << "\n";
	}
  return 0;
}
