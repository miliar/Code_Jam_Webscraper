#include <bits/stdc++.h>
 
using namespace std;
 
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, int> plli;
typedef pair<double,double> pdd;
typedef pair<string,int> psi;
const int MOD = 1e9 + 7;

const int N = 1000100;

set < pii > st;

int t , n , k;


void push(int idx , int len){
	if(idx < 1)
		return;
	if(idx > n)
		return;
	st.insert(make_pair(len,-idx));
}
int main() {
    freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for(int it = 1 ; it <= t ; it++){
		scanf("%d%d",&n,&k);
		st.clear();
		st.insert(make_pair(n,-1));
		int mn = 0;
		int mx = 0;
		for (int p = 0 ; p < k; ++p){
			pii cur = *(--st.end());
			st.erase(cur);
			cur.second = -cur.second;
			int idx = cur.second + (cur.first/2);
			if(cur.first%2 == 0)
				idx--;
			int ln = (idx - cur.second);
			push(cur.second,ln);
			int sn = ((cur.first + cur.second - 1)  - idx);
			push(idx+1,sn);
			if(p == k - 1){
				mn = min(ln,sn);
				mx = max(ln,sn);
			}
		}
		printf("Case #%d: %d %d\n",it,mx,mn);
	}
    return 0;
}