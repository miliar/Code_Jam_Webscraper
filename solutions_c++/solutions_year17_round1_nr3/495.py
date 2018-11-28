#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cassert>
#include <iomanip>
#include <algorithm>
using namespace std;

using ll = long long int;
ifstream fin("3.in");
ofstream fout("3.out");

ll ceil_div(ll a, ll b) {
	assert(a >= 0 && b >= 0);
	return (a / b) + (bool)(a % b);
}

int main() {
	int T;
	fin >> T;
	for (int t = 1; t <= T; t++) {
		fout << "Case #" << t << ": ";

		ll hd, ad, hk, ak, B, D;
		fin >> hd >> ad >> hk >> ak >> B >> D;




		ll x, y; // x B's and y attack's;
		if (B == 0) {
			x = 0;
		}
		else {
			ll guess = (sqrt((double)hk*B) - ad) / (double)B;
			ll score = ~(((ll)1) << 63);
			for (int i = -5; i < 5; i++) {
				ll new_x = guess + i;
				if (new_x < 0)
					new_x = 0;
				ll new_score = new_x + ceil_div(hk, ad + B*new_x);
				if (new_score < score) {
					score = new_score;
					x = new_x;
				}
			}
		}
		y = ceil_div(hk, ad + B*x);


		// w D's and z heal's
		ll best_score = ~(((ll)1) << 63);
		ll last_heal = -1;
		for (int w = 0; w < 100; w++) {
			ll atack = ak;
			ll z = 0;
			ll damage = 0;
			bool impossible = false;
			for (int iter = 0; iter < w + x + y; iter++){ // iter is the index of the turn not counting heals
				if (iter < w) {
					if (damage + atack - D < hd) {
						atack-=D;
						if (atack < 0)
							atack = 0;
					}
					else {
						damage = 0;
						z++;
						iter--;
						if (iter == last_heal) {
							impossible = true;
							break;
						}
						last_heal = iter;
					}
				}
				else {
					if (damage + atack < hd || iter == w+x+y-1) {
						
					}
					else {
						damage = 0;
						z++;
						iter--;
						if (iter == last_heal) {
							impossible = true;
							break;
						}
						last_heal = iter;
					}
				}
				damage += atack;
			}
			if (!impossible) {
				ll score = z + w;
				if (score < best_score)
					best_score = score;
			}
		}

		if (best_score == ~(((ll)1) << 63))
			fout << "IMPOSSIBLE" << endl;
		else
			fout << best_score + x + y << endl;
	}
}
