#include <bits/stdc++.h>

using namespace std;

struct Interv{
	int l, r;
	
	Interv (int l, int r) : l(l), r(r) {}
	
	bool operator < (const Interv & i2) const {
		int len1 = r-l, len2 = i2.r - i2.l;
		if (len1 == len2)
			return l < i2.l;
			
		return len1 > len2;
	} 
	
	int mij () const {
		return l + (r-l)/2;
	}
	
	int getl() const {
		return (mij() - l);
	}
	
	int getr() const {
		return (r - mij());
	}
}; 


int main() {

	int n, k, tst;
	cin>>tst;
	
	
	for (int t = 0; t < tst; t++) {
		cin>>n>>k;
		int mi, ma;
		set <Interv> sset;
		
			
		sset.emplace(0, n-1);
		
		for (int i = 0; i < k; i++) {
			const auto & it = sset.begin();
			auto iv = *it;
			sset.erase(it);
			int m = iv.mij();
			if (m > iv.l)
				sset.emplace(iv.l, m-1);
			if (m < iv.r)
				sset.emplace(m+1, iv.r);
				
			int l = iv.getl(), r = iv.getr();
			ma = max(r, l);
			mi = min(r, l);
		}
		
		cout<<"Case #"<<t+1<<": "<<ma<<" "<<mi<<endl;
		
	}

	return 0;
}
