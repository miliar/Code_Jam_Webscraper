#include <bits/stdc++.h>
void dout() { std::cout << std::endl; }

template <typename Head, typename... Tail>
void dout(Head H, Tail... T) {
	#ifdef DESH
		std::cout << H << ' ';
		dout(T...);
	#endif
}

struct Item{
	int pos, s;
};

struct Seg{
	double from, to;
	int s;
};

double solve() {
	//dout("=============================");
	int d, n; scanf("%d %d", &d, &n);
	
	std::vector<Item> items;
	for (int i = 0; i < n; i++) {
		int pos, s; scanf("%d %d", &pos, &s);
		items.push_back(Item{pos, s});
	}
	
	std::sort(items.begin(), items.end(), [](const Item &left, const Item &right) {
		return left.pos > right.pos;
	});
	
	std::vector<Seg> segments;
	segments.push_back(Seg{(double)items[0].pos, (double)d, items[0].s});
		
	for (int i = 1; i < n; i++) {
		int curPos = items[i].pos;
		int newPos = curPos;
		int curS = items[i].s;
		double prevH = 0;
		while (!segments.empty()) {
			double prevFrom = segments.back().from;
			double prevTo 	= segments.back().to;
			int prevS		= segments.back().s;
			
			double curH = (prevTo - curPos) / curS;
			prevH += (prevTo - prevFrom) / prevS;
			
			if (curH == prevH) {
				segments.pop_back();
				segments.push_back(Seg{(double)curPos, prevTo, curS});
				break;
			} else if (curH < prevH) {
				double tMeet = (prevFrom - newPos) / (curS - prevS);
				double meet = curPos + tMeet * curS;
				
				segments.pop_back();
				segments.push_back(Seg{meet, prevTo, prevS});
				segments.push_back(Seg{(double)curPos, meet, curS});
				break;
			} else {
				newPos += curS * prevH;
				segments.pop_back();
			}
		}
		if (segments.empty()) {
			segments.push_back(Seg{(double)curPos, (double)d, curS});
		}
	}
	
	double t;
	for (Seg seg : segments) {
		//dout("seg", seg.from, seg.to, seg.s);
		t += (seg.to - seg.from) / seg.s;
	}
			
	return d / t;
}

int main() {
	int q; scanf("%d", &q);
	
	for (int i = 1; i <= q; i++) {
		printf("Case #%d: %.6f\n", i, solve());
	}

	return 0;
}
