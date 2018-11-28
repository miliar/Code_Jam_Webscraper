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
	int n;
	char c;
};

void solve() {
	int n, r, o, y, g, b, v;
	scanf("%d %d %d %d %d %d %d", &n, &r, &o, &y, &g, &b, &v);
	// o = r + y
	// g = y + b
	// v = b + r
	
	std::vector<Item> a;
	a.push_back(Item{r, 'R'});
	a.push_back(Item{y, 'Y'});
	a.push_back(Item{b, 'B'});
	
	std::sort(a.begin(), a.end(), [](const Item &left, const Item &right) {
		if (left.n != right.n) {
			return left.n > right.n;
		}
		return left.c < right.c;
	});
	
	//dout("=============================");
	//dout("1", a[0].n, a[0].c);
	//dout("2", a[1].n, a[1].c);
	//dout("3", a[2].n, a[2].c);
	
	if (a[0].n > a[1].n + a[2].n) {
		std::cout << "IMPOSSIBLE";
		return;
	}
	
	std::string s;
	for (int i = 0; i < a[0].n; i++) {
		s += a[0].c;
		if (a[1].n > 0) {
			s += a[1].c;
			if (a[1].n + a[2].n > a[0].n - i) {
				s += a[2].c;
				a[2].n--;
			}
			
			a[1].n--;
		} else {
			s += a[2].c;
			a[2].n--;
		}
	}
		
	std::cout << s;
}

int main() {
	int q; scanf("%d", &q);
	
	for (int i = 1; i <= q; i++) {
		printf("Case #%d: ", i);
		solve();
		printf("\n");
	}

	return 0;
}
