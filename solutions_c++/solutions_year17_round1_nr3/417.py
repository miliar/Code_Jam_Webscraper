#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <climits>
#include <sstream>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;

#define MP make_pair
#define PB push_back
typedef long long LL;

string testfile = "C-small-attempt5";

const int MAXN = 100+1;

int Hd,Ad,Hk,Ak,B,D;

int f[MAXN][MAXN][MAXN][MAXN];

int solve(int hd,int ad,int hk,int ak) {
	if (hk<=ad) return 1;
	if (f[hd][ad][hk][ak]!=-1) return f[hd][ad][hk][ak];

	//f[hd][ad][hk][ak] = INT_MAX/2;
	int ret = INT_MAX/2;
	//cout<<' '<<hd<<' '<<ad<<' '<<hk<<' '<<ak<<endl;

	if (B>0 && ad<hk && hd-ak>0) ret = min(ret,solve(hd-ak,min(ad+B,hk),hk,ak)+1);
	if (D>0 && ak>0 && hd-max(0,ak-D)>0) ret = min(ret,solve(hd-max(0,ak-D),ad,hk,max(0,ak-D))+1);
	if ((ak>0 || ad>0) && hd-ak>0) ret = min(ret,solve(hd-ak,ad,hk-ad,ak)+1);
	if (Hd-ak!=hd && Hd-ak>0) ret = min(ret,solve(Hd-ak,ad,hk,ak)+1);

	return f[hd][ad][hk][ak] = ret;
}

int sim(int b,int d) {
	int hd = Hd;
	int ad = Ad;
	int hk = Hk;
	int ak = Ak;

	int cnt = 1;
	bool cure = true;

	while (true) {
		if (hk<=ad) {
			return cnt;
		}

		if (ak>=hd) {
			if (d>0) {
				int tmp_ak = max(ak-D,0);
				if (tmp_ak<hd) {
					ak = tmp_ak;
					--d;
					cure = true;
				}
				else {
					if (Hd>ak) {
						if (!cure) return INT_MAX;
						hd = Hd;
						cure = false;
					}
					else return INT_MAX;
				}
			}
			else if (Hd>ak) {
				if (!cure) return INT_MAX;
				hd = Hd;
				cure = false;
			}
			else return INT_MAX;
		}
		else {
			if (d>0) {
				int tmp_ak = max(ak-D,0);
				if (tmp_ak<hd) {
					ak = tmp_ak;
					--d;
					cure = true;
				}
				else {
					if (Hd>ak) {
						if (!cure) return INT_MAX;
						hd = Hd;
						cure = false;
					}
					else return INT_MAX;
				}
			}
			else
			if (b>0) {
				ad += B;
				--b;
				cure = true;
			}
			else {
				hk -= ad;
				cure = true;
			}
		}
		hd -= ak;

		//cout<<cnt<<' '<<hd<<' '<<ad<<' '<<hk<<' '<<ak<<endl;

		++cnt;
	}
}

void run() {
	cin>>Hd>>Ad>>Hk>>Ak>>B>>D;

//	memset(f,-1,sizeof(f));
//	int ret = solve(Hd,Ad,Hk,Ak);
//	if (ret>=INT_MAX/2) cout<<"IMPOSSIBLE"<<endl;
//	else cout<<ret<<endl;
	//sim(0,20);
	int ans = INT_MAX;
	for (int i = 0; i<255; ++i)
		for (int j = 0; j<255; ++j) {
			int tmp = sim(i,j);
			if (ans>tmp) {
				//cout<<tmp<<' '<<i<<' '<<j<<endl;
				ans = tmp;
			}
		}
	if (ans==INT_MAX) cout<<"IMPOSSIBLE"<<endl;
	else cout<<ans<<endl;
}

int main() {
	freopen((testfile+".in").c_str(),"r",stdin);
	freopen((testfile+".out").c_str(),"w",stdout);
	int testn;
	cin>>testn;
	for (int loop = 1; loop<=testn; ++loop) {
		cout<<"Case #"<<loop<<": ";

		run();
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
