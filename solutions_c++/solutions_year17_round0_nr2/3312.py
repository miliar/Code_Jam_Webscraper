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

LL n;
vector<int> v;

int main() {
	freopen("tidy_numbers.in","r",stdin);
	freopen("tidy_numbers.out","w",stdout);
	int tc, nt=1;
	cin>>tc;
	while (tc--) {
		cin>>n;
		v.clear();
		while (n>0) {
			v.push_back(n%10);
			n/=10;
		}
		reverse(v.begin(), v.end());
		cout<<"Case #"<<nt++<<": ";
		int dg=v.size();
		if (dg==1) {
			cout<<v[0]<<endl;
			continue;
		} else {
			bool ok=true;
			for (int i=0;i<dg-1;i++)
				if (v[i]>v[i+1]) ok=false;
			if (ok) {
				for (int i=0;i<dg;i++) cout<<v[i];
				cout<<endl;
				continue;
			}
		}
		bool found=false;
		for (int i=dg-1;i>=1;i--) {
			bool ok=true;
			int cur=v[i-1]-1;
			if (cur==0) continue;
			for (int j=i-2;j>=0;j--,cur=v[j+1])
				if (v[j]>cur) ok=false;
			if (ok) {
				for (int j=0;j<i-1;j++) cout<<v[j];
				cout<<v[i-1]-1;
				for (int j=i;j<dg;j++) cout<<9;
				cout<<endl;
				found=true;
				break;
			}
		}
		if (!found) {
			for (int i=0;i<dg-1;i++) cout<<9;
			cout<<endl;
		}
	}
}
