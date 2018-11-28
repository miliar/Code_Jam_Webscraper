#include <bits/stdc++.h>
#include <unordered_map>
#include <tuple>

using namespace std;


struct pair_hash {
    template <class T1, class T2>
    std::size_t operator () (const std::pair<T1,T2> &p) const {
        auto h1 = std::hash<T1>{}(p.first);
        auto h2 = std::hash<T2>{}(p.second);

        // Mainly for demonstration purposes, i.e. works but is overly simple
        // In the real world, use sth. like boost.hash_combine
        return h1 ^ h2;  
    }
};

long long GL, GR;
unordered_map<pair<long long, long long>, pair<long long, long long>, pair_hash> DP;

pair<long,long> utill(long long n, long long k){
	auto v = make_pair(n, k);
	if(DP.count(v) > 0 ) return DP[v];


	long long L = n / 2 ;
	long long R = n - L - 1;
	if(k == 1){
		long long mm = min(L, R);
		long long mmx = max(L,R);
		if(mm < min(GL, GR)){
			GL = L;
			GR = R;
		} if(mm == min(GL, GR) && max(GL, GR) < mmx){
			GL = L;
			GR = R;
		}
		return{L, R};
	}

	if(k > 1){

		long long kr = (k-1)/2;
		long long kl = k-1 - kr;

		pair<long long, long long> lx{-1LL,-1LL};
		pair<long long, long long> rx{-1LL,-1LL};

		
		if(kr > 0) rx = utill(R, kr);
		if(kl > 0) lx = utill(L, kl);

		long long lm = min(lx.first, lx.second);
		long long rm = min(rx.first, rx.second);
		
		if( lm >= rm && rm >= 0){
			R = lx.first;
			L = lx.second;
		} else {
			R = rx.first;
			L = rx.second;
		}
	}

	auto x = make_pair(L, R);
	if(x.second >= 0 && x.first >= 0){
		if(x.first < x.second) swap(x.first, x.second);
		DP[v] = x;

	}

	return x;
}


pair<long, long> utill2(long long len, long long k){
	long long mid = (len + 2 + 1) / 2;

	if(k == 1){ //insert in the mid
		long long L = mid - 1 - 1;
		long long R = len + 2 - mid - 1;

		return {L, R};
	}
	
	if( mid * 2 == len + 2 + 1){
		return utill2(len/2 , k/2);
	} else {
		auto lx = utill2(len - len/2, k - k/2);
		auto rx = utill2(len/2, k/2);

		long long lmm = min(lx.first, lx.second);
		long long rmm = min(rx.first, rx.second);
		
		long long lmmx = max(lx.first, lx.second);
		long long rmmx = max(rx.first, rx.second);

		if(lmm < rmm){
			return lx;
		} else if(lmm > rmm){
			return rx;
		} else if(lmm == rmm){
			if(lmmx >= rmmx) return lx;
			return rx;
		}
	}
}

pair<long long, long long> v2(long long N, long long K){
	vector<bool> used(N+2);
	used[0] = used[N+1] = true;

	long long LD, RD;
	
	map<long long, int> lowerBst;
	map<long long, int> upperBst;
	upperBst[0] = 0;
	lowerBst[0] = 0;
	upperBst[N+1] = N+1;
	lowerBst[-(N+1)] = N+1;

	while(K){
		LD = RD = -1LL;
		int j=0;
		
		for(long long i=0; i < used.size(); ++i){
			if(!used[i]) {
				auto itlx = lowerBst.lower_bound(-i);
				long long lx = i - itlx->second - 1;

				auto itrx = upperBst.lower_bound(i);
				long long rx = itrx->second   - i - 1;

				long long mm = min(lx, rx);
				long long mmx = max(lx, rx);

				if(mm > min(LD, RD) || LD == -1LL){
					LD = lx;
					RD = rx;
					j =  i;
				} else if( LD == -1LL || (mm == min(LD, RD) && mmx > max(LD, RD))){
					LD = lx;
					RD = rx;
					j =  i;
				}
			}
		}

		used[j] = true;
		upperBst[j] = j;
		lowerBst[-j] = j;
		--K;
	}

	return {LD, RD};
}


class cmp {
public:
  cmp(){}

  bool operator() (const pair<int, int> &a, const pair<int, int> &b) const {
    int la = a.second - a.first;
		int lb = b.second - b.first;

		if(la > lb) return false;
		if(la < lb) return true;
		return a.first < b.first;
  }
};

pair<int, int> v3(long long N, long long K){
	

	auto x = [](pair<int, int> a, pair<int, int> b){
		int la = (a.second - a.first)/2;
		int lb = (b.second - b.first)/2;

		if(la != lb) return la < lb;
		
		return a.first > b.first;
	};

	int LD, RD, D, L, R;
	priority_queue<pair<int,int>, vector<pair<int, int>>, cmp> Q;
	Q.push(make_pair(1, N+2));

	
	auto t = Q.top();
	while(Q.size() <= K){
		int j;
		t = Q.top(); Q.pop();
		L = t.first;
		R = t.second;

		D = R - L;
		LD = D / 2;
		RD = D - LD;


		auto left = make_pair(L, L + LD);
		auto right = make_pair(L + LD, R);

		Q.push(left);
		Q.push(right);
	}


	return {LD-1, R - L - LD-1};
}
int main(int argc, char const *argv[]) {
	int T;
	cin >> T;

	long long N, K;
	GR = GL = 1LL<<30LL;
	for(int daCase = 1; daCase <= T; ++daCase){
		cin >> N >> K;
		//pair<long long, long long> v = make_pair(N, K);
		//if()
		//utill(N, K);
		//auto x = DP[v];
		auto x = v3(N, K);
		int mm = max(x.first, x.second);
		int mx = min(x.first, x.second);
		cout << "Case #" << daCase << ": " << mm << " " << mx << endl;
		//cout << "Case #" << daCase << ": " << max(GR, GL) << " " << min(GL, GR) << endl;
	}




	return 0;
}