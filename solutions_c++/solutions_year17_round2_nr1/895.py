#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#define pb push_back
#define pf push_front
#define eps 1e-7
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

#define n 1005

int main(){
	int TC,cs = 0;
	readf("AL");
	cin >> TC;
	//readf("");
	while(TC--){
		int D,N;
		cin >> D >> N;
		double  K[n],S[n];
		double dist = 0, time = 0;
		for(int i=1;i<=N;i++){
			cin >> K[i] >> S[i];
//			dist += D - K[i];
			time = max((D-K[i])/S[i],time);
//			cout << K[i] << " " << S[i] << "\n";
		}
		cout << "Case #" << ++cs << ": ";
		dist = D / time;
		printf("%.8f\n",dist);
	}
}

