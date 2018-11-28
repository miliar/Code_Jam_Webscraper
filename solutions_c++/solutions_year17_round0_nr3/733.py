#include <iostream>
#include <cstring>
#include <cstdio>
#include <map>
#include <set>
using namespace std;
typedef long long LL;
map<LL, LL> M;
set<LL> S;
inline void Insert(LL v, LL t){
	if(M[v] == 0) S.insert(-v);
	M[v] += t;
}
inline void Erase(LL v, LL t){
	if(M[v] == t) S.erase(-v);
	M[v] -= t;
}
inline LL Find(LL v){
	return M[v];
}
LL T, n, k;
int main(){
	//freopen("a.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	cin>>T;
	for(int Case = 1; Case <= T; Case++){
		cin>>n>>k; k--;
		cout<<"Case #"<<Case<<": ";
		S.clear(); M.clear();
		Insert(n, 1);
		
		while(k > 0){
			LL v = *S.begin(); v = -v;
			LL t = Find(v);
			if(t >= k){
				Erase(v, k);
				if(v&1) Insert(v/2, 2*k);
				else { Insert(v/2, k); Insert(v/2-1, k); }
				k = 0;
			} else {
				Erase(v, t);
				if(v&1) Insert(v/2, 2*t);
				else { Insert(v/2, t); Insert(v/2-1, t); }
				k -= t;
			}
		}
		LL v = *S.begin(); v = -v;
		if(v&1) cout<<v/2<<" "<<v/2<<endl;
		else cout<<v/2<<" "<<v/2-1<<endl;
	}
}
