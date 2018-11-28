#include <bits/stdc++.h>

#define IOS std::ios_base::sync_with_stdio(false); std::cin.tie(0); std::cout.tie(0);

using namespace std;

vector<int> vec;

int main() {
	IOS
	int casos;
	cin >> casos;

	for(int caso = 1; caso <= casos; caso++) {
		vec.clear();
		cout << "Case #" << caso << ": ";
		int n, p;
		int ans = 0;
		cin >> n >> p;
		for(int i = 0; i < n; i++) {
			int a;
			cin >> a;
			vec.push_back(a%p);
		}
		//cerr << "deb: ans = " << ans << ", n = " << vec.size() << endl;
		
		sort(vec.begin(), vec.end());

		while(vec.size() != 0 && vec[0] == 0) {
			vec.erase(vec.begin());
			ans++;
		}

		reverse(vec.begin(), vec.end());
		set<int> st;
		n = vec.size();
		//cerr << "deb: ans = " << ans << ", n = " << vec.size() << endl;
		for(int i = 0; i < n; i++) {
			for(int k = 0; k < n; k++) {
				if(i==k) continue;
				if(st.find(i) != st.end() || st.find(k) != st.end())
					continue;
				if(( vec[i] + vec[k] )%p  == 0) {
					st.insert(k);
					st.insert(i);
					ans++;
				}
			}
		}
		vector<int> temp;

		for(int i = 0; i < n; i++) {
			if(st.find(i) != st.end())
				continue;
			temp.push_back(vec[i]);
		}
		vec = temp;
		st.clear();
		n = vec.size();

		//cerr << "deb: ans = " << ans << ", n = " << vec.size() << endl;
		if(p > 2) {
			sort(vec.begin(), vec.end());
			reverse(vec.begin(), vec.end());
			for(int i = 0; i < n; i++) {
				for(int k = 0; k < n; k++) {
					for(int m = 0; m < n; m++) {
						if(i == k || k == m || i == m) continue;
						if(st.find(i) != st.end() || st.find(k) != st.end() || st.find(m) != st.end())
							continue;
						if(( vec[i] + vec[k] + vec[m] )%p  == 0) {
							st.insert(k);
							st.insert(i);
							st.insert(m);
							ans++;
						}
					}
				}
			}
			temp.clear();
			for(int i = 0; i < n; i++) {
				if(st.find(i) != st.end())
					continue;
				temp.push_back(vec[i]);
			}
			vec = temp;
			st.clear();
			n = vec.size();
			//cerr << "deb: ans = " << ans << ", n = " << vec.size() << endl;
		}

		ans += n/p;
		if(n%p != 0) ans++;
		cout << ans;
		cout << endl;
		//cerr << "Caso " << caso << " resuelto " << ans << endl;
	}

	return 0;
}