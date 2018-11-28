#include<cstdio>
#include<iostream>
#include<vector>
#include<cmath>
using namespace std;
#define FOR(i,a,b) for(int i=a;i<b;i++)

int main(){

	int t,r,c;
	cin>>t;
	FOR(p,1,t+1){
		cin>>r>>c;
		 char a[r][c];
		FOR(j,0,r){
			FOR(k,0,c)
				cin>>a[j][k];
		}
		int cnt=0;
		FOR(i,0,r){
			char ch;
			bool flag=false;
			FOR(j,0,c){
				if(isalpha(a[i][j])){
					FOR(k,0,j){
						if(a[i][k]=='?')
							a[i][k]=a[i][j];
					}
					flag=true;
					ch = a[i][j];
				}
			}
			if(!flag)
				cnt++;
			else {
				FOR(j,0,c){
					if(a[i][j]=='?')
						a[i][j]=ch;
				}
				
				for(int k=i-1;k>=0 && cnt!=0;k--){
					for(int l=0;l<c;l++)
						a[k][l]=a[i][l];
					cnt--;
				}
				
			 }
			}
			
			for(int k=r-1;k>=0 && cnt!=0;k--){
				for(int l=0;l<c;l++)
						a[k][l]=a[k-cnt][l];
				cnt--;
			}
			
			cout<<"Case #"<<p<<":\n";
			FOR(i,0,r){
				FOR(j,0,c)
					cout<<a[i][j];
				cout<<endl;
			}
				
		}
		return 0;
}
