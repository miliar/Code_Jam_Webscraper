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

int n, m;
char a[30][30];

int main() {
	freopen("alphabet_cake.in","r",stdin);
	freopen("alphabet_cake.out","w",stdout);
	int tc, nt=1;
	cin>>tc;
	while (tc--) {
		cout<<"Case #"<<nt++<<":"<<endl;
		cin>>n>>m;
		for (int i=0;i<n;i++)
			for (int j=0;j<m;j++) cin>>a[i][j];
		for (int i=0;i<n;i++) {
			int pos=-1;
			for (int j=0;j<m;j++)
				if (a[i][j]!='?') {
					pos=j;
					break;
				}
			if (pos==-1) continue;
			for (int j=0;j<m;j++) {
				if (a[i][j]=='?') a[i][j]=a[i][pos];
				else pos=j;
			}
		}
		int r=-1;
		for (int i=0;i<n && r==-1;i++)
			for (int j=0;j<m && r==-1;j++)
				if (a[i][j]!='?') {
					r=i;
					break;
				}
		for (int i=0;i<n;i++) {
			if (a[i][0]=='?') {
				for (int j=0;j<m;j++)
					a[i][j]=a[r][j];
			} else r=i;
		}
		for (int i=0;i<n;i++) {
			for (int j=0;j<m;j++) cout<<a[i][j];
			cout<<endl;
		}
	}
}
