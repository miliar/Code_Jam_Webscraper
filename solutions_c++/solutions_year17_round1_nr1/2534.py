#include<bits/stdc++.h>
using namespace std;
char ma[100][100];
map<pair<int,int>,char > m;
map<pair<int,int>,char >::iterator it;
int main(){
	int t,r,c;
	cin>>t;
	for(int cs=1;cs<=t;cs++){
		m.clear();
		cin>>r>>c;
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				cin>>ma[i][j];
				if(ma[i][j]!='?')m[make_pair(i,j)]=ma[i][j];
			}
		}
		int a,b;
		for(it=m.begin();it!=m.end();it++){
			a=it->first.first;
			b=it->first.second;
			for(int i=a+1;i<r;i++){
				if(ma[i][b]!='?')break;
				ma[i][b]=ma[a][b];
			}
			for(int i=a-1;i>=0;i--){
				if(ma[i][b]!='?')break;
				ma[i][b]=ma[a][b];
			}
		}
		for(it=m.begin();it!=m.end();it++){
			a=it->first.first;
			b=it->first.second;
			if(b!=c-1){
				for(int j=b+1;j<c;j++){
					if(ma[0][j]=='?'){
						//cout<<"Checking: "<<a<<" "<<b<<endl;
						for(int i=0;i<r;i++){
							ma[i][j]=ma[i][j-1];
						}
					}
				}
		 	}
		 	if(b!=0){
				for(int j=b-1;j>=0;j--){
					if(ma[0][j]=='?'){
						//cout<<"Checking: "<<a<<" "<<b<<endl;
						for(int i=0;i<r;i++){
							ma[i][j]=ma[i][j+1];
						}
					}
				}
			}
		}
		cout<<"Case #"<<cs<<":"<<endl;
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				cout<<ma[i][j];
			}cout<<endl;
		}
	}
}