#include <bits/stdc++.h>

#define rep2(x,fr,to) for(int (x)=(fr);(x)<(to);(x)++)
#define rep(x,to) for(int (x)=0;(x)<(to);(x)++)
#define repr(x,fr,to) for(int (x)=(fr);(x)>=(to);(x)--)
#define all(c) (c).begin(),(c).end()
#define sz(v) (int)(v).size()

using namespace std;
typedef long long ll; typedef vector<int> VI; typedef pair<int,int> pii;
const ll mod = 1e9+7;


void fnc00(int qt){
	
	int N,R,O,Y,G,B,V;
	string mt="ROYGBV";
	vector<int> cl(6);
	cin >>N; // >>R >>O >>Y >>G >>B >>V;
	rep(i,6) cin >> cl[i];
	int mx=*max_element(all(cl));
	if(mx > N/2){
			printf("Case #%d: IMPOSSIBLE\n", qt+1);
			return;
	}
	
	string ans;
	vector<pii> t(6);
	rep(i,6) t[i] = pii(cl[i],i);
	sort(t.rbegin(), t.rend());
	ans = string(N, ' ');
	int svi=-1;
	//rep(i,N) if(i%2==0){
	//	if(ans[i]==' ' && cl[mx]>0){  ans[i]= mt[mx]; cl[mx]--; svi=i;}
	//}
	//for(auto x :t) printf("%d:%d, ",x.first,x.second); puts("");
	int j=0;
	rep(i,6){
		while(t[i].first>0){
			ans[j] = mt[t[i].second];
			j+=2;
			t[i].first--;
			if(j>N-1) break;
		}
		if(j>N-1) break;
	}
	//for(auto x :t) printf("%d:%d, ",x.first,x.second); puts("");
	rep(i,N) if(ans[i]==' '){
		rep(j,6) if(t[j].first>0){
			ans[i]=mt[t[j].second];
			t[j].first--;
			break;
		}
	}
	
	printf("Case #%d: %s\n", qt+1, ans.c_str());

}

int main()
{
	//cin.tie(0); ios_base::sync_with_stdio(false);
	int t; cin >> t;
	rep(i, t) fnc00(i);
	
	
	return 0;
}