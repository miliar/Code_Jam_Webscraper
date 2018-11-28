#include <bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(n);++i)
#define ALL(A) A.begin(), A.end()

using namespace std;

typedef long long ll;
typedef pair<int, int> P;

const int MAX_N = (int)1e6 + 6;

bool stall[MAX_N];
int LS[MAX_N];
int RS[MAX_N];
int maxLS[MAX_N];
int minLS[MAX_N];

void disp_stall(int n, int s){
	cout << "k: " << setw(3) << s << ' ';
	rep (i, n){
		cout << (stall[i] ? 'O' : '.');
	} // end rep
	cout << endl;
}

P calc(int n, int k){
	memset(stall, false, sizeof(stall));


	P res = P(0,0);
	for (int s = 0; s < k; ++s){
		memset(LS, 0, sizeof(LS));
		memset(RS, 0, sizeof(RS));
		memset(maxLS, 0, sizeof(maxLS));
		memset(minLS, 0, sizeof(minLS));
//		disp_stall(n,s);
		for (int i = 0; i < n; ++i){
			int ls = 0;
			for (int j = i - 1; j >= 0; --j){
				if (stall[j]) break;
				++ls;
			} // end for
			LS[i] = ls;
			int rs = 0;
			for (int j = i + 1; j < n; ++j){
				if (stall[j]) break;
				++rs;
			} // end for
			RS[i] = rs;
		} // end for

		int minVal = 0;
		rep (i, n){
			if (stall[i]) continue;
			minLS[i] = min(LS[i], RS[i]);
			minVal = max(minVal, minLS[i]);
			maxLS[i] = max(LS[i], RS[i]);
		} // end rep

		vector<int> cand; cand.clear();
		rep (i, n){
			if (stall[i]) continue;
			if (minVal == minLS[i]){
				cand.push_back(i);
			} // end if
		} // end rep
	
		if (cand.size() == 1){
			stall[cand[0]] |= true;
			res = P(minVal, maxLS[cand[0]]);
			continue;
		} // end if

		vector<int> cand2; cand2.clear();
		int maxVal = 0;
		rep (i, cand.size()){
			if (maxVal < maxLS[cand[i]]){
				maxVal = maxLS[cand[i]];
			} // end if
		} // end rep

		rep (i, cand.size()){
			if (maxVal == maxLS[cand[i]]){
				cand2.push_back(cand[i]);
			} // end if
		} // end rep

		if (!cand2.empty())
			stall[cand2[0]] |= true;
		res = P(maxVal, minVal);
	} // end for

	return res;
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int T; cin >> T;
	for (int t = 1; t <= T; ++t){
		int n, k; cin >> n >> k;
		P res = calc(n,k);
		cout << "Case #" << t << ": " << res.first << ' ' << res.second << endl;
	} // end for	
	return 0;
}
