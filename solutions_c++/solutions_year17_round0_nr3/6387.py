#include <cstdio>
#include <queue>
#include <cstring>
#include <algorithm>
#include <functional>

#define MAX 1000010
typedef long long int lli;

struct trio {
	lli back, pos, next;
};

bool sorting (trio i, trio j) {
	if (std::min ((i.pos - i.back), (i.next - i.pos)) != 
		std::min ((j.pos - j.back), (j.next - j.pos)))
		return std::min ((i.pos - i.back), (i.next - i.pos)) < 
			std::min ((j.pos - j.back), (j.next - j.pos));

	if (std::max ((i.pos - i.back), (i.next - i.pos)) == 
		std::max ((j.pos - j.back), (j.next - j.pos)))
		return i.pos > j.pos;

	return std::max ((i.pos - i.back), (i.next - i.pos)) < 
		std::max ((j.pos - j.back), (j.next - j.pos)) ;
}

int main () {
	lli n, k, count;
	int t;
	bool stalls [MAX];
	
	trio oft;
	scanf ("%d", &t);
	for (int i = 1; i <= t; i++) {
		scanf ("%lld%lld", &n, &k);

		memset (stalls, 0, n);
//		while (!queue.empty())
//			queue.pop();
		std::priority_queue <trio, std::vector<trio>, 
			std::function<bool(trio, trio)>> queue(sorting);
	
		count = 0;
		queue.push ({-1,(n-1)/2,n});
		while (count < k) {
			oft = queue.top();
//			printf ("(%lld,%lld,%lld)\n", oft.back, oft.pos, oft.next);
			queue.pop();

			if (stalls[oft.pos])
				continue;
			stalls[oft.pos] = true;
			count++;

			queue.push ({oft.back, (oft.back + oft.pos)/2, oft.pos});
			queue.push ({oft.pos, (oft.pos + oft.next)/2, oft.next});
		}

		printf ("Case #%d: %lld %lld\n", i, 
			std::max ((oft.pos - oft.back), (oft.next - oft.pos))-1,
			std::min ((oft.pos - oft.back), (oft.next - oft.pos))-1);
	}
	return 0;
}
