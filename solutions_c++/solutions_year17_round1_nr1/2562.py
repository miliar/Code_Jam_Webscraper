/* 
	author: Bhrigu Gupta
		aka “bhrigudov”
*/

#include <bits/stdc++.h>

using namespace std;

#define fo(i,a,b) for(i=a;i<b;i++)
#define rf(i,b,a) for(i=b; i>=a; i--)
#define tr(c, i) for(auto i= c.begin(); i!= c.end(); i++) 
#define pb push_back
#define mp make_pair
#define ub upper_bound
#define lb lower_bound
#define inp(str) getline(cin, str)
#define INF 1e11
#define MX 30

typedef long long ll;
typedef vector<int> vi;

int R, C;
char g[MX][MX];

void FillRow1() {
	int i, j, k;

	fo(i,1,R+1) {
		fo(j,1,C+1) {
			if(g[i][j]!='?') {
				fo(k,1,j+1) g[1][k] = g[i][j];
				while(k<=C) {
					g[1][k] = g[i][k];
					k++;
				}
				return;
			}
		}
	}
}

bool isRowEmpty(int row) {
	for(int i=1; i<=C; i++) if(g[row][i]!='?') return false;
	return true;
}

void FillEmpryRow(int row) {
	for(int i=1; i<=C; i++) g[row][i] = g[row-1][i];
}

void Fill() {
	int i, j;

	if(g[1][1]=='?') FillRow1();

	fo(i,1,R+1) {
		if(isRowEmpty(i)) FillEmpryRow(i);
		else {
			vi idx;
			char temp;

			fo(j,1,C+1) if(g[i][j]!='?') idx.pb(j);

			int st = 1;
			for(int item: idx) {
				temp = g[i][item];
				fo(j, st, item) g[i][j] = temp;
				st = item+1;
			} 
			fo(j,st,C+1) g[i][j] = temp;

		}
	}
}

int main(int argc, char const *argv[])
{
	ios_base::sync_with_stdio(false); 

	int n, i, j, t, k, ans, temp;

	cin>>t;
	fo(k,1,t+1)
	{
		cin>>R>>C;
		fo(i,1,R+1) fo(j,1,C+1) cin>>g[i][j];

		Fill();

		cout<<"Case #"<<k<<":\n";
		fo(i,1,R+1) {
			fo(j,1,C+1) cout<<g[i][j];
			cout<<"\n";
		}
	}

	return 0;
}