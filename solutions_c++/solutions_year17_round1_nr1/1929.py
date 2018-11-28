#include<bits/stdc++.h>
using namespace std;
int main (){
		int t;
		cin>>t;
		for (int z=1;z<=t;z++){
				int r,c;cin>>r>>c;
				string s[30];
				int a[30];
				for (int i=0;i<r;i++) cin>>s[i];
				cout<<"Case #"<<z<<":\n";
				int flag=0;
				for (int i=0;i<r;i++){
						for (int j=0;j<c;j++){
								if (s[i][j]!='?')flag=1;
						}
				}
				if (!flag){
						for (int i=0;i<r;i++){
								for (int j=0;j<c;j++){
										cout<<'A';
								}
								cout<<endl;
						}
						continue;
				}
				char ch;
				for (int i=0;i<r;i++){
					for (int j=0;j<c;j++){
							if (s[i][j]!='?'){
									ch=s[i][j];
									for (int k=j+1;k<c;k++){
											if (s[i][k]!='?') break;
											s[i][k]=ch;
									}
									for (int k=j-1;k>=0;k--){
											if (s[i][k]!='?') break;
											s[i][k]=ch;
									}
							}
					}
				}
				for (int i=0;i<c;i++){
					for (int j=0;j<r;j++){
							if (s[j][i]!='?'){
									ch=s[j][i];
									for (int k=j+1;k<r;k++){
											if (s[k][i]!='?') break;
											s[k][i]=ch;
									}
									for (int k=j-1;k>=0;k--){
											if (s[k][i]!='?') break;
											s[k][i]=ch;
									}
							}
					}
				}

				for (int i=0;i<r;i++){
						cout<<s[i]<<endl;
				}
		}
		return 0;
}
									
