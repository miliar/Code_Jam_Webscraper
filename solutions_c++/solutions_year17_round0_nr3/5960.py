#include <bits/stdc++.h>
using namespace std;

int main() {	
	freopen("C-small-1-attempt0.in", "r", stdin);
freopen("out.txt", "w", stdout);
    int nc;
    cin >> nc;

    for (int caso = 1; caso <= nc; caso++) {
        int k, n;
        cin >> k >> n;

	multiset<int, greater<int> > s;
	s.insert(k);

        for (int i = 0; i < n-1; i++) {
		auto it1 = s.begin(), it2 = it1;
		it2++;
            int sz = *it1;

            int l = (sz-1)/2, r = sz/2;
	    
	
		s.erase(it1,it2);	
		s.insert(l);
		s.insert(r);
        }
        int sz = *s.begin();

        cout << "Case #" << caso<< ": " << sz/2 << ' ' << (sz-1)/2 << endl;
    }

    return 0;
}
