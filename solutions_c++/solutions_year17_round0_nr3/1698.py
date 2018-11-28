#include <bits/stdc++.h>
#define ll long long
using namespace std;
int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	ll t, n, k, ma, mi, a, b, cta = 0, ctb = 0, c, d, ctd=0, ctc=0;
	cin>>t;
	for(ll tc = 1; tc<=t; tc++){
		cin>>n>>k;
		stack <pair<ll, ll> > l, r, L, R;
		ma = n;
		mi = -1;
		r.push(make_pair(ma, 1));
		l.push(make_pair(mi, -1));
		while(ma!=0){
			map <ll, ll> m;
			map <ll, ll> :: iterator it;
			if(ma>0 && ma%2){
				a = ma/2;
				cta = r.top().second*2;
				m.insert(make_pair(a, cta));
			}
			else if(ma>0){
				a = ma/2-1;
				cta = r.top().second;
				b = ma/2;
				ctb = r.top().second;
				m.insert(make_pair(a, cta));
				m.insert(make_pair(b, ctb));
			}
			if(mi>0 && mi%2){
				c = mi/2;
				ctc = l.top().second*2;
				it = m.find(c);
				if(it!=m.end()){
					it->second += ctc;
				}
				else{
					m.insert(make_pair(c, ctc));
				}
			}
			else if(mi>0){
				c = mi/2-1;
				ctc = l.top().second;
				it = m.find(c);

				if(it!=m.end()){
					it->second += ctc;
				}
				else{
					m.insert(make_pair(c, ctc));
				}
				d = mi/2;
				ctd = l.top().second;
				it = m.find(d);
				if(it!=m.end()){
					it->second += ctd;
				}
				else{
					m.insert(make_pair(d, ctd));
				}
			}
			it = m.begin();
			if(m.size()==2){
				a = it->first;
				cta = it->second;
				++it;
				b = it->first;
				ctb = it->second;
				if(a>b){
					r.push(make_pair(a, cta));
					l.push(make_pair(b, ctb));
				}
				else{
					l.push(make_pair(a, cta));
					r.push(make_pair(b, ctb));
				}
			}
			else{
				a = it->first;
				cta = it->second;
				l.push(make_pair(-1, -1));
				r.push(make_pair(a, cta));
			}
			ma = max(r.top().first, l.top().first);
			mi = min(r.top().first, l.top().first);
		}
		while(!r.empty()){
			a = l.top().first, b = l.top().second;
			L.push(make_pair(a, b));
			a = r.top().first, b = r.top().second;
			R.push(make_pair(a, b));
			l.pop();
			r.pop();
		}
		while(k>0){
			k -= R.top().second;
		//	cout<<R.top().first<<" "<<R.top().second<<endl;
			if(k<=0){
				if(R.top().first%2)
					a = b = R.top().first/2;
				else
					a = R.top().first/2, b = R.top().first/2-1;
				break;
			}
			if(L.top().second>0){
			k -= L.top().second;
			if(k<=0){
				if(L.top().first%2)
					a = b = L.top().first/2;
				else
					a = L.top().first/2, b = L.top().first/2-1;
				break;
			}
			}
			R.pop();
			L.pop();
		}
		cout<<"Case #"<<tc<<": ";
		cout<<a<<" "<<b<<endl;
	}
	return 0;
}
