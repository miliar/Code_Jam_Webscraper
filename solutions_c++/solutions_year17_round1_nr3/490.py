#include <iostream>

#define INF -2

using namespace std;

int T[101][101][101][101];
int B, D;
int initial_Hd;

void update(int &T, int t) {
	if (t >= 0) {
		if (T == -2 || T > t) {
			T = t;
		}
	}
}

int sum1(int t) {
	if (t == INF) {
		return INF;
	} else {
		return t + 1;
	}
}

int solve(int Hd, int Ad, int Hk, int Ak) {
	int Hd_, Ad_, Hk_, Ak_, tmp;
	if (T[Hd][Ad][Hk][Ak] == -1) {
		T[Hd][Ad][Hk][Ak] = INF;
		// option 1: attack
		Hd_ = Hd, Ad_ = Ad, Hk_ = Hk, Ak_ = Ak;
		Hk_ = max(Hk - Ad, 0);
		if (Hk_ == 0) {
			tmp = 1;
		} else {
			Hd_ = max(Hd - Ak, 0);
			if (Hd_ > 0) {
				tmp = sum1(solve(Hd_, Ad_, Hk_, Ak_));
			} else {
				tmp = INF;
			}
		}
		update(T[Hd][Ad][Hk][Ak], tmp);
		// option 2: buff
		Hd_ = Hd, Ad_ = Ad, Hk_ = Hk, Ak_ = Ak;
		if (B > 0 && Ad < Hk) {
			Ad_ = min(Ad + B, Hk);
			Hd_ = max(Hd - Ak, 0);
			if (Hd_ > 0) {
				tmp = sum1(solve(Hd_, Ad_, Hk_, Ak_));
			}
			update(T[Hd][Ad][Hk][Ak], tmp);
		}
		// option 3: cure
		Hd_ = Hd, Ad_ = Ad, Hk_ = Hk, Ak_ = Ak;
		Hd_ = initial_Hd;
		Hd_ = max(Hd_ - Ak_, 0);
		if (Hd_ > Hd) {
			update(T[Hd][Ad][Hk][Ak], sum1(solve(Hd_, Ad_, Hk_, Ak_)));
		}
		// option 4: debuff
		Hd_ = Hd, Ad_ = Ad, Hk_ = Hk, Ak_ = Ak;
		if (D > 0 && Ak_ > 0) {
			Ak_ = max(Ak_ - D, 0);
			Hd_ = max(Hd - Ak_, 0);
			if (Hd_ > 0) {
				update(T[Hd][Ad][Hk][Ak], sum1(solve(Hd_, Ad_, Hk_, Ak_)));
			}
		}
	}
	return T[Hd][Ad][Hk][Ak];
}

int main() {
	int nTests;
	cin >> nTests;
	for (int test = 1; test <= nTests; ++test) {
		int Hd, Ad, Hk, Ak;
		cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
		for (int Hd_ = 0; Hd_ <= Hd; ++Hd_) {
			for (int Ad_ = Ad; Ad_ <= max(Ad, Hk); ++Ad_) {
				for (int Hk_ = 0; Hk_ <= Hk; ++Hk_) {
					for (int Ak_ = 0; Ak_ <= Ak; ++Ak_) {
						T[Hd_][Ad_][Hk_][Ak_] = -1;
					}
				}
			}
		}
		initial_Hd = Hd;
		int ans = solve(Hd, Ad, Hk, Ak);
		cout << "Case #" << test << ": ";
		if (ans == INF) {
			cout << "IMPOSSIBLE" << endl;
		} else {
			cout << ans << endl;
		}
	}
	return 0;
}
