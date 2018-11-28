#include <cstdio>
#include <set>
using namespace std;

struct Seg{
	long long length; long long count;
	Seg(long long length, long long count):length(length),count(count){;}
};

bool operator < (const Seg& l, const Seg& r) {
	return l.length > r.length;
}

void add(set<Seg> &S, Seg t){
	set<Seg>::iterator x;
	if ((x = S.find(t)) == S.end()) {
		S.insert(t);
	} else {
		Seg y = *x;
		S.erase(x);
		S.insert(Seg(y.length, t.count + y.count));
	}
}

void solve(){
	set<Seg> S;
	long long n, k; scanf("%lld%lld", &n, &k);
	S.insert(Seg(n, 1));
	long long sum = 0, length = n;
	while (sum < k){
		
		set<Seg>::iterator vs = S.begin();
		Seg s = *vs;
		S.erase(vs);
		length = s.length;
		sum += s.count;
		if ((length % 2) == 0){

			if (length / 2 != 0)
				add(S, Seg(length / 2, s.count));
			if (length / 2 - 1 != 0)
				add(S, Seg(length / 2 - 1, s.count));
		} else {
			if (length / 2 != 0)
				add(S, Seg(length / 2, s.count * 2));
		}
	}

	if ((length % 2) == 0)
		printf("%lld %lld\n", length / 2, length / 2 - 1);
	else
		printf("%lld %lld\n", length / 2, length / 2);
}

int main(){
	freopen("C.in", "r", stdin);
	int T; scanf("%d", &T);
	for (int Tcase = 0; Tcase < T; Tcase++){
		printf("Case #%d: ", Tcase + 1);
		solve();
	}
	
}
