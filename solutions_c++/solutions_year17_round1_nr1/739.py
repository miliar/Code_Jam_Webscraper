#include<bits/stdc++.h>
#define mp make_pair
#define fs first
#define sc second
#define pb push_back
using namespace std;

string baca[30];
string jawab[30];

int main(){
	freopen("A-large.in","r",stdin);
	freopen("haha.txt","w",stdout);
	int t; cin>>t;
	for(int tmp=0;tmp<t;tmp++){
		int n,m; cin>>n>>m;
		int last = -1;
		for(int sem=0;sem<n;sem++){
			cin>>baca[sem];
			jawab[sem] = baca[sem];
			for(int i = 0;i<baca[sem].length();i++){
				if(baca[sem][i] != '?'){
					last = sem;
				}
			}
		}
		int akhir = 0;
		for(int sem=0;sem<n;sem++){
			int ada = false;
			int mulai = 0;
			int sek = sem;
			if(sem == last) sek = n-1;	
			for(int i = 0;i<baca[sem].length();i++){
				if(baca[sem][i] != '?'){
					ada = true;
					for(int j=akhir;j<=sek;j++){
						for(int k=mulai;k<=i;k++){
							jawab[j][k] = baca[sem][i];
						}
					}
					mulai = i+1;
				}
			}
			if(mulai != m){
				for(int j=akhir;j<=sek;j++){
					for(int k=mulai;k<m;k++){
						jawab[j][k] = baca[sem][mulai-1];
					}
				}
			}
			if(ada){
				akhir = sem+1;
			}
			if(sem==last) break;
		}
		printf("Case #%d:\n",tmp+1);
		for(int sem=0;sem<n;sem++){
			cout<<jawab[sem]<<"\n";
		}
	}
}

