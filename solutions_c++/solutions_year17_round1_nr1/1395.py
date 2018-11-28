#include<bits/stdc++.h>
#define ll long long
#define pb push_back

using namespace std;

char s[100][100];
bool vis[100];

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int t,n,m,i,j,cc,k;
	int cnt;
	cin>>t;
	for(cc=1;cc<=t;cc++){
		cout<<"Case #"<<cc<<": \n";
		cin>>n>>m;
		for(i=1;i<=n;i++){
			for(j=1;j<=m;j++){
				cin>>s[i][j];
			}
		}

		for(i=1;i<=n;i++){
			for(j=1;j<=m;j++){
				if(s[i][j]!='?'){
					char x=s[i][j];
					for(k=j-1;k>=1;k--){
						if(s[i][k]=='?'){
							s[i][k]=x;
						}
						else{
							break;
						}
					}
					for(k=j+1;k<=m;k++){
						if(s[i][k]=='?'){
							s[i][k]=x;
						}
						else{
							break;
						}
					}
				}
			}
		}

		for(j=1;j<=m;j++){
			for(i=1;i<=n;i++){
				if(s[i][j]!='?'){
					char x=s[i][j];
					for(k=i-1;k>=1;k--){
						if(s[k][j]=='?'){
							s[k][j]=x;
						}
						else{
							break;
						}
					}
					for(k=i+1;k<=n;k++){
						if(s[k][j]=='?'){
							s[k][j]=x;
						}
						else{
							break;
						}
					}

				}
			}
		}

		for(i=1;i<=n;i++){
			for(j=1;j<=m;j++){
				cout<<s[i][j];
			}
			cout<<endl;
		}


	}



	return 0;	
}
