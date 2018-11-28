#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#define pb push_back
#define pf push_front
#define fi first
#define se second
#define sz size
#define eps 1e-7
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


pair<int,int>  v[200];

int main(){
	readf("B");
	int TC,cs = 0,N,M,i,ans=0;
	cin >> TC;
	while(TC--){
		cin>>N >> M;
		for(int i=0;i<N;i++){
			cin>>v[i].fi>>v[i].se;
		}
		for(int i=N;i<M+N;i++){
			cin>>v[i].fi>>v[i].se;
		}
		if(max(N,M)==2){
			sort(v,v+N+M);
			if(min(v[1].se-v[0].fi,v[0].se+1440-v[1].fi) > 720){
				ans=4;
			}
			else{
				ans=2;
			}
		}
		if(max(N,M)==1){
			ans=2;
		}
		
		cout<<"Case #"<<++cs<<": "<<ans<<"\n";
	}
}

