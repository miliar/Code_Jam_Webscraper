#include<iostream>
#include<algorithm>
#include<queue>
#include<cmath>
using namespace std;
int n,m,k,t,r,c;
char a[26][26];
int main(){
	ios::sync_with_stdio(false);
	//freopen("infile.in","r",stdin);
	//freopen("outfile.txt","w",stdout);
	cin >> t;
	for(int u=1; u<=t ;u++){
		cin >> r >> c;
		int tno=0;
		for(int i=1; i<=r ;i++){
			for(int j=1; j<=c ;j++){
				cin >> a[i][j];
				if(a[i][j]!='?') tno=i;
			}
		}
		if(tno==0){
			for(int i=1; i<=r ;i++){
				for(int j=1; j<=c ;j++){
					a[i][j]='A';
				}
			}
		}
		else{
			for(int i=1; i<=r ;i++){
				bool no=true;
				for(int j=1; j<=c ;j++){
					if(a[i][j]!='?'){
						no=false;
						break;
					}
				}
				if(!no){
					for(int j=2; j<=c ;j++) if(a[i][j-1]!='?' && a[i][j]=='?') a[i][j]=a[i][j-1];
					for(int j=c-1; j>=1 ;j--) if(a[i][j+1]!='?' && a[i][j]=='?') a[i][j]=a[i][j+1];
				}
			}
			for(int i=1; i<=c ;i++){
				for(int j=2; j<=r ;j++) if(a[j-1][i]!='?' && a[j][i]=='?') a[j][i]=a[j-1][i];
				for(int j=r-1; j>=1 ;j--) if(a[j+1][i]!='?' && a[j][i]=='?') a[j][i]=a[j+1][i];
			}
		}
		cout << "Case #" << u << ":\n";
		for(int i=1; i<=r ;i++){
			for(int j=1; j<=c ;j++){
				cout << a[i][j];
			}
			cout << endl;
		}
	}
}
