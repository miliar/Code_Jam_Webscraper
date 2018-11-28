#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
#include <utility>
#include <map>
#include <vector>
#include <set>
#include <cmath>
#include <utility>
#include <queue>
#include <deque>

#define rep(i,a,n) for(int i=a;i<=n;i++)
#define REP(i,a,n) for(int i=a;i<n;i++)
#define mp make_pair
#define pb push_back
#define SZ(x) ((int) (x).size())


using namespace std;

typedef  long long  LL;
typedef  vector<int> VI;
typedef  pair<int,int> PII;


int main(){
	ios::sync_with_stdio(false);
	int n;
	cin>>n;
	rep(pp, 1, n) {
		printf("Case #%d: ", pp);
		LL x;
		cin>>x;
		vector<int> seq;
		while(x) {
			seq.pb(x%10);
			x = x / 10;
		}
		int len = seq.size();
		bool flag = false;
		REP(i, 0, len) {
			if(flag) {
				seq[i]--;
				flag = false;
				for(int j=i-1;j>-1;j--) {
					seq[j]=9;
				}
			}	
			if(i==len-1)
				break;
			if(seq[i] < seq[i+1]){
				flag = true;
			}
		}
		x = 0;
		for(int i=len-1;i>-1;i--) {
			x = x * 10;
			x = x + 1LL * seq[i];
		}
		cout<<x<<endl;
	}
	return 0;
}