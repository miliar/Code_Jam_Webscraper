#include <bits/stdc++.h>
using namespace std;

#define MEM(arr,val)memset((arr),(val), sizeof (arr))
#define PI (acos(0)*2.0)
#define FASTER ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define ALL(v)v.begin(),v.end()
#define PB(v)push_back(v)

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

ll gcd(ll a,ll b){return b == 0 ? a : gcd(b,a%b);}
ll lcm(ll a,ll b){return a*(b/gcd(a,b));}

/**
 * __builtin_popcount(int d) // count bits
 * __builtin_popcountll(long long d)
 * strtol(s, &end, base); // convert base number
 */
//----------------------------------------------------------------------//

int R,C;
vector<string> G;
vector<string> G2;

//int paint(int r1, int c1, int r2, int c2){
//
//	set<int> F;
//	char c;
//	for (int i = r1; i <= r2 &&  F.size()  <= 1; ++i) {
//		for (int j = c1; j <= c2 &&  F.size()  <= 1; ++j) {
//			if(G[i][j] != '?'){
//				c = G[i][j];
//				F.insert(G[i][j]);
//			}
//		}
//	}
//
//	if( F.size() == 1){
//		for (int i = r1; i <= r2; ++i) {
//			for (int j = c1; j <= c2; ++j) {
//				G[i][j] = c;
//			}
//		}
//	}
//
//	return
//}


bool iscolor(int r1, int c1, int r2, int c2, char col){

	bool has_col = false;


	for (int i = r1; i <= r2; ++i) {
		for (int j = c1; j <= c2; ++j) {
			if(G[i][j]!='?' && G[i][j] != col)return false;
//			printf("G[%d][%d] = %c\n",i,j, G[i][j]);
			if(G[i][j] == col)has_col=true;
		}
	}

//	printf("has color = %d\n", has_col);
	return has_col;
}

void paint(int r1, int c1, int r2, int c2, char c){

	for (int i = r1; i <= r2; ++i) {
		for (int j = c1; j <= c2; ++j) {
			G[i][j] = c;
		}
	}
}


int main(){
	FASTER;

	int t;
	cin >> t;
	int Case=1;
	while(t--){
		cin >> R >> C;

		G.assign(R, "");

		for (int i = 0; i < R; ++i) {
			cin >> G[i];
		}

		int vis[300];MEM(vis,0);

		for (int i = 0; i < R; ++i) {
			for (int j = 0; j < C; ++j) {

				char c = G[i][j];
				if(c =='?' || vis[c] )continue;
				vis[c]=1;


				int R1,C1,R2,C2;R1=R2=C1=C2=0;
				int best = 0;

				for (int r1 = 0; r1 < R; ++r1) {
					for (int c1 = 0; c1 < C ; ++c1) {

						for (int r2 = r1; r2 < R ; ++r2) {
							for (int c2 = c1; c2 < C; ++c2) {


								bool iscol = iscolor(r1,c1,r2,c2, c);

//								if(G[i][j] == 'A'){
//									printf("col1 = %c \t %d %d %d %d\thas_col = %d\n",c,r1,c1,r2,c2,iscol);
//								}

								if(!iscol)continue;
//
								int area = (r2-r1+1) * (c2 - c1 + 1);
//
								if(area > best){
									best = area;
									R1=r1;
									R2=r2;
									C1=c1;
									C2=c2;
								}


							}
						}
					}
				}

//				printf("col = %c \t %d %d %d %d\n",c,R1,C1,R2,C2);
				paint(R1,C1,R2,C2,c);

			}
		}



		cout << "Case #" << (Case++) <<":" << endl;
		for (int i = 0; i < R; ++i)cout << G[i] << endl;
	}



	return 0;
}
