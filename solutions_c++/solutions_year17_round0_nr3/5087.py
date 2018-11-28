#include<bits/stdc++.h>
using namespace std;
int main() {
	int t;
	cin>>t;
	int casenum = 0, ans;
	while(t--) {
		set<int> s;
		map<int, int> m;
		s.erase(s.begin(), s.end());
		casenum++;
		int n, k;
		cin>>n>>k;
		s.insert(n);
		m[n]++;
		set<int>::iterator it;
		for(int i = 0; i < k-1; i++) {
			it = s.end();
			it--;
			int val = *it;
			m[val]--;
			if(m[val] == 0) s.erase(it);
			s.insert((int)val/2 - (val%2 == 0));
			m[(int)val/2 - (val%2 == 0)]++;
			s.insert((int)val/2);
			m[(int)val/2]++;
			/*for (it = s.begin(); it != s.end(); it++) {
    			cout << " " << *it<<" "<<m[*it]<<"   ";
			}
			cout<<endl;*/
		}
		it = s.end();
		it--;
		ans = *it;
		if(ans == 0)
			cout<<"Case #"<<casenum<<": "<<0<<" "<<0<<endl;
		else
			cout<<"Case #"<<casenum<<": "<<(int)ans/2<<" "<<(int)ans/2 - (ans%2 == 0)<<endl;
	}
}
