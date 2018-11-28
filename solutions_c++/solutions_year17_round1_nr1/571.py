#include <bits/stdc++.h>
using namespace std;
//debug
#ifdef grief
#define debug(...) do{\
	fprintf(stderr , "%s - %d : (%s) = " , __PRETTY_FUNCTION__ , __LINE__ , #__VA_ARGS__ );\
	_DO(__VA_ARGS__);\
}while(0)
template<typename I> void _DO(I&&x){
	cerr<<x<<endl;
}
template<typename I,typename...T> void _DO(I&&x,T&&...tail){
	cerr<<x<<" , ";
	_DO(tail...);
}
#else
#define debug(...)
#endif
//type
typedef long long ll;
typedef pair<int,int> pii;
typedef long long ll;
typedef pair<ll,ll> pll;
typedef priority_queue<pll,vector<pll>,greater<pll> > heap;
//macro
#define SZ(x) ((ll)(x).size())
#define ALL(x) (x).begin(),(x).end()
#define F first
#define S second
#define mkp make_pair
#define pb push_back
const ll INF=4e18;
const ll MAX=1e6+5;
const ll MOD=1e9+7;
//}}}
char box[30][30];
int r,c;
bool che(int x){
	for(int i=0;i<c;i++){
		if(box[x][i]!='?')	return 0;
	}
	return 1;
}
int main(){
	ios_base::sync_with_stdio(0); cin.tie(0);
	freopen("input.in","r",stdin);
	freopen("answer.out","w",stdout);
	int tt;
	cin>>tt;
	for(int t=1;t<=tt;t++){
		cin>>r>>c;
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				cin>>box[i][j];
			}
		}
		for(int i=0;i<r;i++){
			char now='?';
			for(int j=0;j<c;j++){
				if(box[i][j]!='?')	now=box[i][j];
				else				box[i][j]=now;
			}
			now='?';
			for(int j=c-1;j>=0;j--){
				if(box[i][j]!='?')	now=box[i][j];
				else				box[i][j]=now;
			}
		}
		for(int i=1;i<r;i++)
			if(che(i))
				for(int j=0;j<c;j++)
					box[i][j]=box[i-1][j];
		for(int i=r-2;i>=0;i--)
			if(che(i))
				for(int j=0;j<c;j++)
					box[i][j]=box[i+1][j];
		cout<<"Case #"<<t<<":\n";
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				cout<<box[i][j];
			}
			cout<< '\n';
		}
	}
	return 0;
}

