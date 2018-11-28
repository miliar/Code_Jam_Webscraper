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
#include <unordered_map>

using namespace std;
typedef long long LL;

int n, p;
int a[110];
int b[110];

int main() {
	freopen("fresh_chocolate.in","r",stdin);
	freopen("fresh_chocolate.out","w",stdout);
	int tc, nt=1;
	cin>>tc;
	while (tc--) {
		memset(b,0,sizeof(b));
		cin>>n>>p;
		for (int i=0;i<n;i++) {
			cin>>a[i];
			a[i]%=p;
			b[a[i]]++;
		}
		int ret=0;
		if (p==2) {
			ret=b[1]/2;
		} else if (p==3) {
			int dif=max(b[1],b[2])-min(b[1],b[2]);
			ret=min(b[1],b[2])+2*((int)(dif/3));
			if (dif%3==2) ret++;
		} else {
			ret=min(b[1],b[3])+b[2]/2;
			int dif=max(b[1],b[3])-min(b[1],b[3]);
			if (b[2]%2==0) {
				int clean=(dif+3)/4;
				ret+=dif-clean;
			} else {
				if (dif>2) {
					ret+=2;
					dif-=2;
					int clean=(dif+3)/4;
					ret+=dif-clean;
				} else {
					ret+=dif;
				}
			}
		}
		ret=max(ret, 0);
		cout<<"Case #"<<nt++<<": "<<n-ret<<endl;
	}
}
