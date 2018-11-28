#include<bits/stdc++.h>
using namespace std;
typedef unsigned long long ULL;

string solve(ULL n, ULL k)
{
	string ans;
	unordered_map<ULL, ULL> umap;
	set<ULL> pq;

	pq.insert(n);
	umap[n] = 1ULL;
	while(true) {
		auto pointer = pq.rbegin();
		ULL len = *pointer;
		pq.erase(--pq.end());
		
		ULL num = umap[len],
			Ls = (len+1ULL)/2ULL-1ULL,
			Rs = len-1ULL-Ls;

		umap.erase(umap.find(len));

		if(k<=num) {
			ans = to_string(Rs)+" "+to_string(Ls);
			break;
		}else {
			k -= num;
			auto pointer1 = pq.find(Ls);
			auto pointer2 = pq.find(Rs);

			if(pointer1 == pq.end())
				pq.insert(Ls);
			if(umap.find(Ls) == umap.end())
				umap[Ls] = 0ULL;
			umap[Ls] += num;

			if(pointer2 == pq.end())
				pq.insert(Rs);
			if(umap.find(Rs) == umap.end())
				umap[Rs] = 0ULL;
			umap[Rs] += num;
		}
	}

	return ans;
}

int main()
{
	ios_base::sync_with_stdio(false);
	freopen("C-large.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int t;
	cin >> t;

	for(int i=1; i<=t; ++i) {
		ULL n, k;
		cin >> n >> k;
		cout << "Case #" << i << ": " << solve(n, k) << "\n";
	}

	return 0;
}
