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
#define ler freopen("ebola.in","r",stdin);freopen("ebola.out","w",stdout)
#define fastio ios::sync_with_stdio(0), cin.tie(0)
#define debug cout<<"!!?!!\n"
using namespace std; 
#define EPS 1e-9L
#define MOD 1000000007
#define INF 2000000000000000000LL
#define MAXN 100005

int t;
int n, r, o, y, g, b, v;
vector <int> uni;
vector <int> aux;

void bota(int x, int pos){
	aux.clear();
	rep(i,0,pos+1) aux.pb(uni[i]);
	aux.pb(x);
	rep(i,pos+1,sz(uni)) aux.pb(uni[i]);
	uni.clear();
	rep(i,0,sz(aux)) uni.pb(aux[i]);
}

void add(int x){
	rep(i,0,sz(uni)){
		if(uni[i]==uni[(i+1)%sz(uni)] && uni[i]!=x){
			bota(x,i);
			return;
		}
	}
	rep(i,0,sz(uni)){
		if(uni[i]!=x && uni[(i+1)%sz(uni)]){
			bota(x,i);
			return;
		}
	}
	rep(i,0,sz(uni)){
		if(uni[i]!=x){
			bota(x,i);
			return;
		}
	}
	uni.pb(x);
}

bool ok(){
	rep(i,0,sz(uni)){
		if(uni[i]==uni[(i+1)%sz(uni)]) return false;
	}
	return true;
}

map <int,char> mapa;

int main(){
	cin >> t;
	rep(caso,1,t+1){
		cin >> n >> r >> o >> y >> g >> b >> v;
		uni.clear();
			
		int cont[3], usado[3];
		cont[0]=r;
		cont[1]=y;
		cont[2]=b;
		sort(cont,cont+3);
		
		clr(usado,0);
		rep(i,0,3){
			if(r==cont[i] && !usado[i]){
				mapa[i]='R';
				usado[i]=1;
				break;
			}
		}
		rep(i,0,3){
			if(y==cont[i] && !usado[i]){
				mapa[i]='Y';
				usado[i]=1;
				break;
			}
		}
		rep(i,0,3){
			if(b==cont[i] && !usado[i]){
				mapa[i]='B';
				usado[i]=1;
				break;
			}
		}
		
		rep(i,0,cont[2]) uni.pb(2); 
		rep(i,0,cont[1]) add(1);
		rep(i,0,cont[0]) add(0);
		
		cout << "Case #" << caso << ": ";
		if(!ok()) cout << "IMPOSSIBLE\n";
		else{
			rep(i,0,sz(uni))
				cout << mapa[uni[i]];
			cout << endl;
		}
	}
}










