#include "bits/stdc++.h"
using namespace std;
#define rep(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define rer(i,l,u) for(int (i)=(int)(l);(i)<=(int)(u);++(i))
#define reu(i,l,u) for(int (i)=(int)(l);(i)<(int)(u);++(i))
static const int INF = 0x3f3f3f3f; static const long long INFL = 0x3f3f3f3f3f3f3f3fLL;
typedef vector<int> vi; typedef pair<int, int> pii; typedef vector<pair<int, int> > vpii; typedef long long ll;
template<typename T, typename U> static void amin(T &x, U y) { if (y < x) x = y; }
template<typename T, typename U> static void amax(T &x, U y) { if (x < y) x = y; }


template<int... Sizes>
struct MultidimensionalIndex;
template<>
struct MultidimensionalIndex<> {
	MultidimensionalIndex() {}
	int getTotalSize() const { return 1; }
	int getIndexAcc(int acc) const { return acc; }
};
template<int Head, int... Tail>
struct MultidimensionalIndex<Head, Tail...> : MultidimensionalIndex<Tail...> {
	using Base = MultidimensionalIndex<Tail...>;
	enum { size = Head };
	template<typename... TailT>
	MultidimensionalIndex(TailT... tail) : Base(tail...) {}
	int getTotalSize() const { return size * Base::getTotalSize(); }
	template<typename... TailT>
	int getIndexAcc(int acc, int head, TailT... tail) const {
#ifdef _DEBUG
		assert(0 <= head && head < size);
#endif
		return Base::getIndexAcc(acc * size + head, tail...);
	}
};
template<int... Tail>
struct MultidimensionalIndex<0, Tail...> : MultidimensionalIndex<Tail...> {
	using Base = MultidimensionalIndex<Tail...>;
	const int size;
	template<typename... TailT>
	MultidimensionalIndex(int head, TailT... tail) : size(head), MultidimensionalIndex<Tail...>(tail...) {}
	int getTotalSize() const { return size * Base::getTotalSize(); }
	template<typename... TailT>
	int getIndexAcc(int acc, int head, TailT... tail) const {
#ifdef _DEBUG
		assert(0 <= head && head < size);
#endif
		return Base::getIndexAcc(acc * size + head, tail...);
	}
};

template<typename Val, int... Sizes>
struct DP : MultidimensionalIndex<Sizes...> {
	using Base = MultidimensionalIndex<Sizes...>;
	std::vector<Val> dp;
	template<typename... SizesT>
	DP(SizesT... sizes) : Base(sizes...) {}
	void init(Val val) { dp.assign(Base::getTotalSize(), val); }
	void init() { dp.assign(Base::getTotalSize(), Val()); }
	template<typename... SizesT>
	decltype(dp[0]) operator()(SizesT... indices) { return dp[Base::getIndexAcc(0, indices...)]; }
	template<typename... SizesT>
	Val operator()(SizesT... indices) const { return dp[Base::getIndexAcc(0, indices...)]; }
	void swap(DP &that) { dp.swap(that.dp); }
};

int main() {
	int T;
	scanf("%d", &T);
	for (int ii = 0; ii < T; ++ ii) {
		int N; int P;
		scanf("%d%d", &N, &P);
		array<int, 4> cnt = { {} };
		rep(i, N) {
			int G;
			scanf("%d", &G);
			++ cnt[G % P];
		}
		DP<int, 0, 0, 0, 0, 0> dp(cnt[0] + 1, cnt[1] + 1, cnt[2] + 1, cnt[3] + 1, P);
		dp.init(-1);
		dp(0, 0, 0, 0, 0) = 0;
		rer(a, 0, cnt[0]) rer(b, 0, cnt[1]) rer(c, 0, cnt[2]) rer(d, 0, cnt[3]) rep(p, P) {
			int x = dp(a, b, c, d, p);
			if (x == -1) continue;
			int y = x + (p == 0 ? 1 : 0);
			if (a < cnt[0])
				amax(dp(a + 1, b, c, d, (p + 0) % P), y);
			if (b < cnt[1])
				amax(dp(a, b + 1, c, d, (p + 1) % P), y);
			if (c < cnt[2])
				amax(dp(a, b, c + 1, d, (p + 2) % P), y);
			if (d < cnt[3])
				amax(dp(a, b, c, d + 1, (p + 3) % P), y);
		}
		int ans = -1;
		rep(p, P)
			amax(ans, dp(cnt[0], cnt[1], cnt[2], cnt[3], p));
		printf("Case #%d: %d\n", ii + 1, ans);
	}
	return 0;
}
