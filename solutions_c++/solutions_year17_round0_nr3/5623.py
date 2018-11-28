#include <bits/stdc++.h>

using namespace std;

multiset<long long> st;
long long n,k;
int q;

main(){
	//ios_base::sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL);

	freopen("C-small-1-attempt0.in","r",stdin);
	freopen("1.txt","w",stdout);

	cin >> q;

	for(int test = 1; test <= q; ++test){
		st.clear();

		cin >> n >> k;

		st.insert(n);

		for(int i = 0;i < k - 1; i++){
			set<long long>::iterator it = st.end();

			it--;
			long long sz = *it;
			st.erase(it);
			if(sz % 2){
				st.insert(sz / 2);
				st.insert(sz / 2);
			}
			else {
                st.insert(sz / 2 - 1);
                st.insert(sz / 2);
			}
		}

		set<long long>::iterator it = st.end();

		it--;

		long long sz = *it;
		cout << "Case #" << test << ":" << " ";

		if(sz == 1) cout << "0" << " " << "0" << "\n";
		else{
			if(sz % 2) cout << sz / 2 << " " << sz / 2 << "\n";
			else cout << sz / 2 << " " << sz / 2 - 1 << "\n";
		}
	}
}
