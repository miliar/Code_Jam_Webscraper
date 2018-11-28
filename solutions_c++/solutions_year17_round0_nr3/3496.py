#include <bits/stdc++.h>
#define endl '\n'
#define lli long long int
#define forn(i, n) for(int i=0;i<n;i++)
#define pii pair<int,int>
#define psi pair<int,pii>
#define fi first
#define se second
#define pb(a) push_back(a)

using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int t, u = 1;
	int n,k,last;
	cin>>t;
	while(t--) {
		cin>>n>>k;
		priority_queue< psi, vector<psi>, greater<psi> > q;
		q.push(psi(-n, pii(1, n)));
		set<int> s;
		s.insert(n + 1);
		s.insert(0);
		while(k--) {
			int a = q.top().se.fi;
			int b = q.top().se.se;
			q.pop();
			last = (a + b) / 2;
			s.insert(last);

			q.push(psi(-last + a, pii(a, last - 1)));
			q.push(psi(-b + last, pii(last + 1, b)));
		}
		s.erase(last);
		set<int> :: iterator it = s.upper_bound(last);
		int uno = abs(last - *it);
		--it;
		int dos = abs(last - *it);
		if(uno < dos) swap(uno, dos);
		uno--,dos--;
		cout<<"Case #"<<u++<<": "<<uno<<" "<<dos<<endl;
	}
	return 0;
}
