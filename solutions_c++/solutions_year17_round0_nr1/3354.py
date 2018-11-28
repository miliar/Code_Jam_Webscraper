#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <fstream>
#include <cstring>

using namespace std;
typedef long long LL;

bool a[1010];

int main() {
	freopen("oversized_pancake_flipper.in","r",stdin);
	freopen("oversized_pancake_flipper.out","w",stdout);
	int tc, nt=1;
	cin>>tc;
	while (tc--) {
		string s;
		int n;
		cin>>s>>n;
		int ret=0;
		for (int i=0;i<s.size();i++) {
			a[i]=(s[i]=='+');
		}
		for (int i=0;i<=s.size()-n;i++)
			if (!a[i]) {
				for (int j=0;j<n;j++) a[i+j]=!a[i+j];
				ret++;
			}
		bool ok=true;
		for (int i=s.size()-n;i<s.size();i++)
			if (!a[i]) ok=false;
		cout<<"Case #"<<nt++<<": ";
		if (ok) cout<<ret<<endl;
		else cout<<"IMPOSSIBLE"<<endl;
	}
}
