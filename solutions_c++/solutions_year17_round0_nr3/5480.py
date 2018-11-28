#include <cstdio>
#include <map>

using namespace std;

int main() {
	int t, cs;
	int n, k;
	int l, r;
	int i;
	map<int, int, greater<int> > spaces;

	scanf("%d", &t);
	for(cs = 1; cs <= t; cs++) {
		spaces.clear();

		scanf("%d%d", &n, &k);
		spaces[n] = 1;
		for(i = 0; i < k; i++) {
			//print(spaces);
			auto biggest = spaces.begin();
			int space = biggest->first - 1;
			--(biggest->second);
			if(biggest->second == 0) {
				spaces.erase(biggest);
			}

			l = space / 2 + space % 2;
			r = space / 2;
			//printf("ins: l %d, r %d\n", l, r);
			bool doL = l > 0, doR = r > 0;

			if(l > 0) ++(spaces[l]);
			if(r > 0) ++(spaces[r]);
		}

		printf("Case #%d: %d %d\n", cs, l > r? l : r, l < r? l : r);
		
	}
}