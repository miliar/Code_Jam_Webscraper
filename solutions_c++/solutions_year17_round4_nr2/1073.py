#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <vector>
using namespace std;

#define MAXN 205

void solve() {
	int line[1005][3];
	memset(line,0,sizeof(line));

	int ans=0,pro=0;
	int n,c,m;
	scanf("%d%d%d",&n,&c,&m);

	int p,b;
	for (int i=0;i<m;i++) {
		scanf("%d%d",&p,&b);
		line[p][b]++;
	}
	if (c==2) {
		int c_cnt = 0, tmp;
		int r_max = -1, r_idx;
		int r_max_2 = -1;
		for (int i=1;i<=n;i++) {
			if (line[i][1]>=1 && line[i][2]>=1) {
				c_cnt++;
				tmp = min(line[i][1],line[i][2]);
				if (tmp>=r_max) {
					r_max = tmp;
					r_idx = i;
				}
			}
		}
		//cerr<<"c_cnt : "<<c_cnt<<endl;
		if (c_cnt>=2) {
			for (int i=1;i<=n;i++) if (i!=r_idx){
				if (line[i][1]>=1 && line[i][2]>=1) {
					tmp = min(line[i][1],line[i][2]);
					ans += tmp;
					line[i][1] -= tmp;
					line[i][2] -= tmp;
					if (tmp>r_max_2) {
						r_max_2 = tmp;
					}
				}
			}

			ans += r_max_2;
			line[r_idx][1] -= r_max_2;
			line[r_idx][2] -= r_max_2;

			if (r_max > r_max_2) {
				c_cnt = 1;
			} else {
				c_cnt = 0;
			}
		}
		if (c_cnt == 1) {
			int k; // for match
			for (k=1;k<=2;k++) {
				for (int i=1;i<=n;i++) if (i!=r_idx) {
					if (line[i][k]>0) {
						if (line[r_idx][3-k]>line[i][k]) {
							ans += line[i][k];
							line[r_idx][3-k] -= line[i][k];
							line[i][k] = 0;
						} else {
							ans += line[r_idx][3-k];
							line[i][k] -= line[r_idx][3-k];
							line[r_idx][3-k] = 0;
							break;
						}
					}
				}
			}
			if (line[r_idx][1]>0 && line[r_idx][2]>0) {
				//cerr<<"here"<<endl;
				tmp = min(line[r_idx][1],line[r_idx][2]);
				if (r_idx>1) {
					pro += tmp;
					ans += tmp;
					line[r_idx][1] -= tmp;
					line[r_idx][2] -= tmp;
					ans += (line[r_idx][1]+line[r_idx][2]);
				} else {
					ans += (line[r_idx][1]+line[r_idx][2]);
				}
				printf("%d %d\n",ans,pro);
				return;
			} else {
				c_cnt = 0;
			}
		}
		if (c_cnt == 0) {
			int cnt[5];
			cnt[1]=cnt[2]=0;
			for (int k=1;k<=2;k++) {
				for (int i=1;i<=n;i++)
					cnt[k]+=line[i][k];
			}
			tmp = min(cnt[1],cnt[2]);
			ans += tmp;
			cnt[1] -= tmp;
			cnt[2] -= tmp;
			ans += (cnt[1]+cnt[2]);
		}

		printf("%d %d\n",ans,pro);
	}

}

int main() {
	int tt;
	cin>>tt;
	for (int cs=1;cs<=tt;cs++){
		printf("Case #%d: ",cs);
		solve();
	}

	return 0;
}