#include <iostream>
#include <algorithm>
//#include "stdio.h"
#include <string>
using namespace std;


int main() {
	int t;
	cin >> t;

	int hd, ad, hk, ak, b, d;
	for (int tcount = 1; tcount <= t; ++tcount) {
		cin >> hd >> ad >> hk >> ak >> b >> d;
		cout << "Case #" << tcount << ": ";

		int bm;
		if (b == 0)
			bm = 0;
		else
			bm = ceil(((double)(hk - ad)) / b);
		int dm;
		if (d == 0)
			dm = 0;
		else
			dm = ceil((double)(ak) / d);

		int mintcount = 10000000;

		for (int bc = 0 ; bc <= bm; ++bc)
			for (int dc = 0; dc <= dm; ++dc) {
				int bufc = bc;//buff for bc times
				int debc = dc;//defuff for dc times

				int mhp = hd;
				int mat = ad;
				int ehp = hk;
				int eat = ak;
				bool healflag = false;
				int tcount = 0;

				while (true) {
					++tcount;
					if (mhp < hd && ((debc == 0 && eat >= mhp) || (debc > 0 && eat - d >= mhp)) && (debc > 0 || bufc > 0 || mat < ehp)) {
						// should heal
						if (healflag)
							goto fail;
						mhp = hd;
						healflag = true;
						goto enemy;
					}
					else
						healflag = false;

					if (debc > 0) {
						eat -= d;
						--debc;
						goto enemy;
					}
					if (bufc > 0) {
						mat += b;
						--bufc;
						goto enemy;
					}
					//Attack
					ehp -= mat;
					if (ehp <= 0)
						goto win;

				enemy:
					mhp -= eat;
					if (mhp <= 0)
						goto fail;
				}

			fail:
				continue;
			win:
				if (tcount < mintcount)
					mintcount = tcount;
			}

		if (mintcount == 10000000)
			cout << "IMPOSSIBLE\n";
		else
			cout << mintcount << endl;

	}

	return 0;
}