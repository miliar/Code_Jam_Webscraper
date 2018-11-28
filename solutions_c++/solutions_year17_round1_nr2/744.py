#include<bits/stdc++.h>
#define mp make_pair
#define fs first
#define sc second
#define pb push_back
using namespace std;

int need[100];

vector<pair<int,int> > bisa[100];
int piv[100];

int main(){
	freopen("B-large.in","r",stdin);
	freopen("haha.txt","w",stdout);
	int t; cin>>t;
	for(int tmp=0;tmp<t;tmp++){
		int n,p; cin>>n>>p;
		for(int sem=0;sem<n;sem++){
			cin>>need[sem];
		}
		for(int sem=0;sem<n;sem++){
			for(int i=0;i<p;i++){
				int x; cin>>x;
				int bagi1 = ceil( (double) (10 * x)/(11 * need[sem]) );
				int bagi2 = (10 * x)/(9 * need[sem]) ;
				if(bagi1 <= bagi2){
					bisa[sem].pb(mp(bagi1,bagi2));
				}
			}
			sort(bisa[sem].begin(),bisa[sem].end());
		}
		int jaw = 0;
		memset(piv,0,sizeof(piv));
		
		for(int sem=0;sem<bisa[0].size();sem++){
			int l = bisa[0][sem].fs;
			int r = bisa[0][sem].sc;
			bool can = true;
			for(int i=1;i<n;i++){
				while(piv[i] < bisa[i].size() && bisa[i][piv[i]].sc < l){
					piv[i]++;
				}
				if(piv[i] < bisa[i].size()){
					if(bisa[i][piv[i]].fs <= r){
						piv[i]++;
					}else{
						can = false;
						break;
					}
				}else{
					can = false;
					break;
				}
			}
			if(can){
				jaw++;
			}
		}
		for(int sem=0;sem<n;sem++){
			bisa[sem].clear();
		}
		printf("Case #%d: %d\n",tmp+1,jaw);
	}
}

