#include <bits/stdc++.h>

//LIFE IS NOT A PROBLEM TO BE SOLVED

using namespace std;

#define rep(i,a,b) for(int i = int(a); i < int(b) ; i++)
#define pb push_back
#define mp make_pair
#define F first
#define S second

typedef pair < int, int > ii;
typedef pair < ii, int > iii;

int R, C;
char mat[30][30];
char ans[30][30];
int vis[30][30];

vector <ii> v;

bool my_comp(ii a, ii b){
	int um=a.F*a.S, dois=b.F*b.S;
	return um >= dois ? true : false;
}
int main(){
	
	freopen("A.in", "r", stdin);
	freopen("A.sol", "w", stdout);

	rep(i, 1, 26){
		rep(j, 1, 26){
			v.pb(mp(i, j));
		}
	}
	
	sort(v.begin(), v.end(), my_comp);
	
	int T, z=1; cin >> T;
	
	while(T--){
		
		cin >> R >> C;
		rep(i, 0, R) cin >> mat[i];
		set <char> vis;
		
		rep(w, 0, v.size()){
			int a=v[w].F, b=v[w].S;
			if(a<=R && b<=C){
				rep(i, 0, R){
					if(i+a>R) break;
					rep(j, 0, C){
						if(j+b>C) break;
						int cnt=0, yep=1, x, y;
						rep(k, i, i+a){
							rep(l, j, j+b){
								if(mat[k][l]!='?'){
									if(cnt){
										yep=0;
										break;
									}
									x=k, y=l;
									cnt++;
								}
							}
						}
						if(yep && cnt && !vis.count(mat[x][y])){
							//cout << mat[x][y] << " " << x << " " << y << "  " << a << " " << b<< '\n';
							vis.insert(mat[x][y]);
							rep(k, i, i+a){
								rep(l, j, j+b){
									mat[k][l]=mat[x][y];
								}
							}
						}
					}
				}
			}
		}
		
		printf("Case #%d:\n", z++);
		rep(i, 0, R) cout << mat[i] << '\n';
		
	}
	
	
	return 0;
	
}
