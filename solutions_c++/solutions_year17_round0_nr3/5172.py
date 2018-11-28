#include<bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define F first
#define S second
#define ll long long
#define ld long double
#define sz(a) ((int)(a).size())
#define clr(a,v) memset(a, v, sizeof(a))
#define all(a) (a).begin(),(a).end()
#define pii pair<int,int>
#define pdd pair<ld,ld> 
#define rep(i,a,b) for(int i=a; i<b; i++)
#define dec(i,a,b) for(int i=a; i>=b; i--)
#define ler freopen("inspection.in","r",stdin);freopen("inspection.out","w",stdout)
#define fastio ios::sync_with_stdio(0), cin.tie(0)
#define debug cout<<"!!?!!\n"
#define N 100007
using namespace std;

struct seg{
	int l, r;
	seg(int a, int b){ l=a; r=b;}
};
bool operator<(seg x, seg y){
	if(x.r-x.l != y.r-y.l) return (x.r-x.l)>(y.r-y.l);
	return x.r<y.r;
}

int t, n, k;
int main(){
	cin >> t;
	rep(caso,1,t+1){
		cin >> n >> k;
		set <seg> q;
		q.insert(seg(1,n));
		
		int ans, menor, maior;
		rep(i,0,k){
			assert(sz(q)>0);
			seg aux= *q.begin();
			q.erase(q.begin());
			
			ans=(aux.l+aux.r)/2;
			if(ans!=aux.l) q.insert(seg(aux.l,ans-1));
			if(ans!=aux.r) q.insert(seg(ans+1,aux.r));
			menor= (ans-aux.l);
			maior= (aux.r-ans);
		}
		cout << "Case #" << caso << ": " << maior << " " << menor << endl;
	}
}












