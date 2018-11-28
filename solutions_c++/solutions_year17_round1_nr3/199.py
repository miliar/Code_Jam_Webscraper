#include <bits/stdc++.h>

using namespace std;

struct Info {
	int Hd, Ad, Hk, Ak, step;
	
	Info() {
		Hd = Ad = Hk = Ak = step = 0;
	}
	
	Info(int tHd, int tAd, int tHk, int tAk, int tStep) : 
		Hd(tHd), Ad(tAd), Hk(tHk), Ak(tAk), step(tStep) {}
	
	Info attack() {
		return Info(Hd - Ak, Ad, Hk - Ad, Ak, step + 1);
	}
	
	Info buff(int b) {
		return Info(Hd - Ak, min(Ad + b, 100), Hk, Ak, step + 1);
	}
	
	Info cure(int h) {
		return Info(h - Ak, Ad, Hk, Ak, step + 1);
	}
	
	Info debuff(int d) {
		Ak = max(0, Ak - d);
		return Info(Hd - Ak, Ad, Hk, Ak, step + 1);
	}
};

int Hd, Ad, Hk, Ak, B, D, dem;

char vis[101][101][101][101];

int findMin() {
	dem++;
	list <Info> Q;
	Q.push_back(Info(Hd, Ad, Hk, Ak, 0));
	vis[Hd][Ad][Hk][Ak] = dem;
	while (!Q.empty()) {
		Info u = Q.front(), v;
		Q.pop_front();
		// Attack
		v = u.attack();
		if (v.Hk <= 0)
			return v.step;
		if (v.Hd > 0 && vis[v.Hd][v.Ad][v.Hk][v.Ak] < dem) {
			vis[v.Hd][v.Ad][v.Hk][v.Ak] = dem;
			Q.push_back(v);
		}
		// Buff
		v = u.buff(B);
		if (v.Hd > 0 && vis[v.Hd][v.Ad][v.Hk][v.Ak] < dem) {
			vis[v.Hd][v.Ad][v.Hk][v.Ak] = dem;
			Q.push_back(v);
		}
		// Cure
		v = u.cure(Hd);
		if (v.Hd > 0 && vis[v.Hd][v.Ad][v.Hk][v.Ak] < dem) {
			vis[v.Hd][v.Ad][v.Hk][v.Ak] = dem;
			Q.push_back(v);
		}
		// Debuff
		v = u.debuff(D);
		if (v.Hd > 0 && vis[v.Hd][v.Ad][v.Hk][v.Ak] < dem) {
			vis[v.Hd][v.Ad][v.Hk][v.Ak] = dem;
			Q.push_back(v);
		}
	}
	return -1;
}

int main() {
	int _T;
	cin >> _T;
	dem = 0;
	for(int _t = 1; _t <= _T; _t++) {
		cout << "Case #" << _t << ": ";
		cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
		int res = findMin();
		if (res != -1)
			cout << res << "\n";
		else 
			cout << "IMPOSSIBLE\n";
	}
	return 0;
}