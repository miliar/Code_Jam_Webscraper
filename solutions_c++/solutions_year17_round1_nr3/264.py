#include <stdio.h>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
using namespace std;

const long long lim = 1e18;

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	int Test; scanf ("%d",&Test); for (int Case=1;Case<=Test;Case++){
		printf ("Case #%d: ",Case);

		long long hd,ad,hk,ak,b,d;
		scanf ("%lld %lld %lld %lld %lld %lld",&hd,&ad,&hk,&ak,&b,&d);

		long long nowans = lim;
		if (false){
			int ddd,bbb;
			for (int deb=0;deb<=100;deb++){
				for (int buf=0;buf<=100;buf++){
					long long phd = hd, pad = ad, phk = hk, pak = ak;
					int db = deb, bf = buf; long long turn = 0;
					while (db > 0 && phk > 0 && phd > 0){
						if (phd <= max(0ll,pak-d)) phd = hd;
						else pak = max(0ll,pak-d), db--;
						phd -= pak;
						turn++;
						if (turn > 10000) break;
					}
					while (bf > 0 && phk > 0 && phd > 0){
						if (phd <= pak) phd = hd;
						else pad += b, bf--;
						phd -= pak;
						turn++;
						if (turn > 10000) break;
					}
					while (phk > 0 && phd > 0){
						if (phd <= pak && phk - pad > 0) phd = hd;
						else phk -= pad;
						turn++;
						if (phk <= 0) break;
						phd -= pak;
						if (turn > 10000) break;
					}

					if (phk <= 0){
						if (nowans > turn){
							nowans = turn;
							ddd = deb;
							bbb = buf;
						}
					}
				}
			}
		}

		long long phk = hk - 1, count = (hk + ad - 1) / ad, buff = 0;

		if (ad >= hk){
			puts("1");
			continue;
		}
		if (hd <= ak - d){
			puts("IMPOSSIBLE");
			continue;
		}

		if (b){
			for (long long i=1;i<=phk;i++){
				long long j = phk / (phk / i);
				if (ad <= i){
					long long u = (i - ad + b - 1) / b;
					if (ad + u * b <= j){
						long long cnt = phk / i + 1 + u;
						if (count > cnt){
							count = cnt;
							buff = u;
						}
					}
				}
				i = j;
			}
			if (ad <= hk){
				long long u = (hk - ad + b - 1) / b;
				long long cnt = 1 + u;
				if (count > cnt){
					count = cnt;
					buff = u;
				}
			}
		}

		long long ans = lim;
		auto test = [&](long long u){
			long long turn = 0, hp = hd, dm = ak;
			while (u){
				long long l = 1, r = u, a = 0;
				while (l <= r){
					long long m = (l + r) / 2;
					long long lf = hp - m * dm + d * m * (m + 1) / 2;
					if (m == u){
						if (dm - u * d <= 0){
							lf = hp - (m-1) * dm + d * m * (m - 1) / 2;
						}
					}
					if (lf > 0){
						a = m;
						l = m + 1;
					}
					else r = m - 1;
				}

				if (a == 0) return;

				if (u == a){
					turn += u;
					long long lf = hp - u * dm + d * u * (u + 1) / 2;
					if (dm - u * d <= 0){
						lf = hp - (u-1) * dm + d * u * (u - 1) / 2;
					}
					hp = lf;
					dm -= u * d;
					if (dm < 0) dm = 0;
					u = 0;
				}
				else{
					turn += a + 1;
					dm -= a * d;
					if (dm < 0) dm = 0;
					hp = hd - dm;
					u -= a;
				}
			}

			if (hd <= dm)
				return;

			if (dm == 0){
				ans = min(ans,turn+count);
				return;
			}

			long long rem = count;
			long long now = (hp + dm - 1) / dm;
			if (rem <= now){
				ans = min(ans,turn+rem);
				return;
			}
			turn += now;
			rem -= now - 1;
			hp = hd - dm;

			long long cyc = (hp + dm - 1) / dm;
			if (cyc == 1)
				return;
			if (rem >= (cyc - 1) * 3){
				long long os = rem / (cyc - 1) - 2;
				if (os < 0) os = 0;
				turn += os * cyc;
				rem -= os * (cyc - 1);
			}

			while (rem > cyc){
				turn += cyc;
				rem -= cyc - 1;
			}
			turn += rem;
			ans = min(ans,turn);
		};
		
		long long phd = hd - 1;
		test(0);
		if (d){
			test((ak+d-1)/d);
			for (long long i=1;i<=phd;i++){
				long long j = phd / (phd / i);
				if (j <= ak){
					long long u = (ak - j + d - 1) / d;
					if (i <= ak - u * d) test(u);
				}
				i = j;
			}
		}

		if (ans == lim) puts("IMPOSSIBLE");
		else printf ("%lld\n",ans);
	}

	return 0;
}