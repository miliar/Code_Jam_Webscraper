#include<bits/stdc++.h>
#define int long long
using namespace std;
#define rep(i,n) for(int i=0;i<(n);++i)
#define INF (1ll<<60)
typedef pair<int, int> pii;
#define L first
#define S second
#define all(s) s.begin(),s.end()
#define pb push_back

int Ac, Aj;
struct activity {
	int s, t, type;//1:c,2:j
	activity() {}
	activity(int s,int t,int type):s(s),t(t),type(type){}
	bool operator <(activity& o)const {
		return s < o.s;
	}
};
activity acts[220];
int sche[24 * 60 * 2];
vector<pii> cc, jj, cj, jc;
int C, J;
int solve() {
	cin >> Ac >> Aj;
	rep(i,Ac) {
		int c, d;
		cin >> c >> d;
		acts[i] = activity(c, d, 1);
		C += d - c;
	}
	rep(i,Aj) {
		int j, k;
		cin >> j >> k;
		acts[i + Ac] = activity(j, k, 2);
		J += k - j;
	}
	sort(acts, acts + Ac + Aj);
	int prev = -1;
	rep(i,Ac+Aj) {
		if(i) {
			if(acts[i].type==prev) {
				if(prev==1) {
					cc.pb(pii(acts[i].s - acts[i - 1].t, acts[i - 1].t));
				}else if(prev==2) {
					jj.pb(pii(acts[i].s - acts[i - 1].t, acts[i - 1].t));
				}
				else { assert(0); }
			}else {
				if(acts[i].type==2) {
					//cj
					cj.pb(pii(acts[i].s - acts[i - 1].t, acts[i - 1].t));
				}else {
					//jc
					jc.pb(pii(acts[i].s - acts[i - 1].t, acts[i - 1].t));
				}
			}
		}
		prev = acts[i].type;
		for (int j = acts[i].s; j < acts[i].t;++j) {
			sche[j] = acts[i].type;
		}
	}
	if(acts[0].type==acts[Ac+Aj-1].type) {
		if(acts[0].type==1) {
			cc.pb(pii(acts[0].s + 1440 - acts[Ac + Aj - 1].t, acts[Ac + Aj - 1].t));
		}else if(acts[0].type==2) {
			jj.pb(pii(acts[0].s + 1440 - acts[Ac + Aj - 1].t, acts[Ac + Aj - 1].t));
		}else {
			assert(0);
		}
	}else {
		if (acts[0].type == 1) {
			//jc
			jc.pb(pii(acts[0].s + 1440 - acts[Ac + Aj - 1].t, acts[Ac + Aj - 1].t));
		}
		else if (acts[0].type == 2) {
			//cj
			cj.pb(pii(acts[0].s + 1440 - acts[Ac + Aj - 1].t, acts[Ac + Aj - 1].t));
		}
	}
	//cerr << "C" << C << endl;
	sort(all(cc));
	rep(i,cc.size()) {
		C += cc[i].L;
		if(C>720) {
			C -= cc[i].L;
			for (int s = cc[i].S; C < 720;++s) {
				sche[s] = 1;
				C++;
			}
			break;
		}else {
			for (int s = cc[i].S; s < cc[i].S + cc[i].L;++s) {
				sche[s] = 1;
			}
		}
	}
	sort(all(jj));
	rep(i, jj.size()) {
		J += jj[i].L;
		if (J>720) {
			J -= jj[i].L;
			for (int s = jj[i].S; J < 720; ++s) {
				sche[s] = 2;
				J++;
			}
			break;
		}
		else {
			for (int s = jj[i].S; s < jj[i].S + jj[i].L; ++s) {
				sche[s] = 2;
			}
		}
	}
	//cerr << "C" << C << endl;
	if (C < 720) {
		swap(cc, cj);
		sort(all(cc));
		rep(i, cc.size()) {
			C += cc[i].L;
			if (C > 720) {
				C -= cc[i].L;
				for (int s = cc[i].S; C < 720; ++s) {
					sche[s] = 1;
					C++;
				}
				break;
			}
			else {
				for (int s = cc[i].S; s < cc[i].S + cc[i].L; ++s) {
					sche[s] = 1;
				}
			}
		}
		swap(cc, cj);
	}
	if(C<720) {
		swap(cc, jc);
		sort(all(cc));
		rep(i, cc.size()) {
			C += cc[i].L;
			if (C > 720) {
				C -= cc[i].L;
				for (int s = cc[i].S + cc[i].L - 1; C < 720; --s) {
					sche[s] = 1;
					C++;
				}
				break;
			}
			else {
				for (int s = cc[i].S; s < cc[i].S + cc[i].L; ++s) {
					sche[s] = 1;
				}
			}
		}
		swap(cc, jc);
	}
	//cerr << "C" << C << endl;

	swap(C, J);
	if (C < 720) {
		swap(cc, jc);
		sort(all(cc));
		rep(i, cc.size()) {
			C += cc[i].L;
			if (C > 720) {
				C -= cc[i].L;
				for (int s = cc[i].S; C < 720; ++s) {
					sche[s] = 1;
					C++;
				}
				break;
			}
			else {
				for (int s = cc[i].S; s < cc[i].S + cc[i].L; ++s) {
					sche[s] = 1;
				}
			}
		}
		swap(cc, jc);
	}
	if (C<720) {
		swap(cc, cj);
		sort(all(cc));
		rep(i, cc.size()) {
			C += cc[i].L;
			if (C > 720) {
				C -= cc[i].L;
				for (int s = cc[i].S + cc[i].L - 1; C < 720; --s) {
					sche[s] = 1;
					C++;
				}
				break;
			}
			else {
				for (int s = cc[i].S; s < cc[i].S + cc[i].L; ++s) {
					sche[s] = 1;
				}
			}
		}
		swap(cc, cj);
	}
	swap(C, J);

	if (C<720) {
		for (int i = acts[0].s; i < acts[0].s + 1440; ++i) {
			if (sche[i] == 0) {
				sche[i] = 1;
				C++;
			}
		}
	}

	if(J<720) {
		for (int i = acts[0].s; i < acts[0].s + 1440;++i) {
			if (sche[i] == 0) {
				sche[i] = 2;
				J++;
			}
		}
	}
	//cerr << C << "a" << J << endl;
	if(!(C == 720 && J == 720)) {
		cerr << endl;
		for (int i = acts[0].s; i < acts[0].s + 1440; ++i) {
			cerr << sche[i] << " ";
		}
		assert(0);
	}
	
	int pre = sche[acts[0].s];
	int ans = 0;
	for (int i = acts[0].s + 1; i < acts[0].s + 1440; ++i) {
		if (sche[i] != pre) {
			ans++;
		}
		pre = sche[i];
	}
	if (sche[acts[0].s] != sche[acts[0].s + 1439])ans++;
	return ans;
}

signed main() {
	int t;
	cin >> t;
	cout << setprecision(15);
	rep(i, t) {
		int ans = solve();
		cout << "Case #" << i + 1 << ": " << ans << endl;
		C = 0;
		J = 0;
		memset(acts,0,sizeof(acts));
		memset(sche, 0, sizeof(sche));
		cc.clear();
		jj.clear();
		cj.clear();
		jc.clear();
	}
}
