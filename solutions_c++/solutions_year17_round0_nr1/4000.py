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
//	readf("A-large");
	int T,cs= 0;
	cin >> T;
	while(T--){
		string tmp;
		int K;
		cin >> tmp;
		cin >> K;
		int x[1005];
		for(int i=0;i<tmp.size();i++){
			if(tmp[i] == '-') x[i] = 0;
			else x[i] = 1; 
		}
		cout << "Case #" << ++cs << ": ";
		vector<int> sim;
		int ind = 0;
		int ans = 0;
		int hitung = 0;
		for(int i=0;i<tmp.size();i++){
		//	if(i + K == tmp.size() + 1 )break;
			int nxt = i+K-1;
			if(hitung % 2 == 1){
				x[i] = (x[i] ^ 1);
			//	cout << x[i] << " " << i << "\n";
			}
			if(i + K < tmp.size()+1)
			if(x[i] == 0){
				hitung++;
				ans++;
				sim.pb(nxt);
				x[i] = x[i] ^ 1;
			//	cout << i << "\n";
			}
			if(sim.size() > ind && i == sim[ind]){
				hitung--;
				ind++;
			}
		}
		bool ok =0;
		for(int i=0;i<tmp.size();i++){
			if(x[i] == 0) {
				ok = 1;
				break;
			}
		}
		if(ok) cout << "IMPOSSIBLE\n";	
		else cout << ans << "\n";
	}
}

