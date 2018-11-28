#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int Times;
char lineEnd[15];

int main() {

    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);

    scanf("%d", &Times);
    gets(lineEnd);
    for (int times = 1; times <= Times; ++times) {
        printf("Case #%d: ", times);
		
		int hd, ad, hk, ak, b, d;
		scanf("%d%d%d%d%d%d", &hd, &ad, &hk, &ak, &b, &d);
		
		int ld = 0, rd = 0;
		if (d != 0) {
			rd = (ak - 1) / d + 1;
		}
		
		int lb = 0, rb = 0;
		if (b != 0) {
			rb = (hk - ad - 1) / b + 1;
		}
		
		int ans = 800;
		for (int i = ld; i <= rd; ++i) {
			for (int j = lb; j <= rb; ++j) {
				bool flag = false;
				
				int res = 0;
				int hdn = hd, adn = ad, hkn = hk, akn = ak;
				
				for (int k = 0; k < i; ++k) {
					int aknafter = akn > d ? akn - d : 0;
					if (hdn <= aknafter) {
						hdn = hd - akn;
						if (hdn <= aknafter) {
							flag = true;
							break;
						}
						res += 1;
					}
					
					akn = aknafter;
					hdn -= akn;
					res += 1;
				}
				if (flag) continue;
				
				for (int k = 0; k < j; ++k) {
					if (hdn <= akn) {
						hdn = hd - akn;
						if (hdn <= akn) {
							flag = true;
							break;
						}
						res += 1;
					}
					
					adn += b;
					hdn -= akn;
					res += 1;
				}
				if (flag) continue;
								
				while (hkn > 0) {
					if (hdn <= akn && hkn > adn) {
						if (hd - hdn <= akn) {
							flag = true;
							break;
						}
						hdn = hd - akn;
						res += 1;
					}
					
					hkn -= adn;
					hdn -= akn;
					res += 1;
				}
				if (flag) continue;
								
				if (res < ans) ans = res;
			}
		}
		if (ans == 800) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
    }
	
    return 0;
}
