#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
#define F first
#define S second

int custRides[1010];
pair<int,int> pb[1010];

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int tcs;
	cin>>tcs;
	for (int tc=1;tc<=tcs;tc++) {
		int n,c,m;
		cin>>n>>c>>m;
		for (int i=0;i<m;i++) {
			int p,b;
			cin>>p>>b;
			pb[i]={p,b};
		}
		sort(pb,pb+m);
		int rides=0;
		for (int i=1;i<=c;i++) custRides[i]=0;
		int lim=0;
		int seat=0;
		for (int i=0;i<m;i++) {
			lim+=rides*(pb[i].F-seat);
			seat=pb[i].F;
			while (lim<i+1) {
				rides++;
				lim+=pb[i].F;
			}
			custRides[pb[i].S]++;
			if (custRides[pb[i].S]>rides) {
				rides++;
				lim+=pb[i].F;
			}
		}
		int promo=0;
		int curCnt=0;
		int cur=-1;
		for (int i=0;i<m;i++) {
			if (pb[i].F!=cur) {
				promo+=max(0,curCnt-rides);
				cur=pb[i].F;
				curCnt=1;
			} else curCnt++;
		}
		promo+=max(0,curCnt-rides);
		cout<<"Case #"<<tc<<": "<<rides<<" "<<promo<<"\n";
	}
}
