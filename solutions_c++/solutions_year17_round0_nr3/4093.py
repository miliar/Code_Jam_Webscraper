#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#define pb push_back
#define fi first
#define se second
#define sz size
#define fod find_by_order
#define fastio ios::base_sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL);
#define ofk order_of_key
#define val(x) cout << "Value dari "<< #x << " adalah " << x  << "\n"
#define tr tree<int,null_type,less<int>,rb_tree_tag,tree_order_statistics_node_update>
typedef long long ll;
using namespace __gnu_pbds;
using namespace std;

void readf(string x){
	freopen((x+".in").c_str(),"r",stdin);
	freopen((x+".out").c_str(),"w",stdout);
}


int read()
{
	bool min = 0;
	int  result = 0;
	char ch;
	ch = getchar();
	while(1)
	{
		if(ch == '-') break;
		if(ch >='0' && ch <= '9') break;
		ch = getchar();
	}
	if(ch == '-') min = 1;else result = ch-'0';
	while(1)
	{
		ch =getchar();
		if(ch< '0' || ch>'9') break;
		result = result * 10 + (ch-'0');
	}
	if(min) return -result;
	return result;
}

int main(){
	readf("C");
	ll TC,cs=0;
	cin >> TC;
	while(TC--){
		ll N,K;
		cin >> N >> K;
		cout << "Case #" << ++cs << ": ";
		if(K == 1) {
			cout << (double) ceil((double)(N-1)/2) << " " <<  (N-1)/2 << "\n";
			continue;
		}
		K--;
		ll ki =(double)ceil((double)(N-1)/2),ka = (N-1)/2;
		while(K != 0){
			if(K % 2 == 1){
				ll tmp = ki;
				ki = (double) ceil((double) (tmp-1)/2) ;
				ka = (tmp-1)/2; 
			}
			else{
				ll tmp = ka-1;
				ki = (double) ceil((double) (tmp)/2) ;
				ka = (tmp)/2; 
			}
			K= (K-1)/2;
		}
		cout << ki << " " << ka << "\n";
	}
}

