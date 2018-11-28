#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
using namespace std;
int main(){
	string fileName="A-large";
	freopen((fileName+".in").c_str(),"r",stdin);
	freopen((fileName+".out").c_str(),"w",stdout);
	int nn;
	cin>>nn;
	int ii=0;
	while(ii<nn){
		cout<<"Case #"<<ii+1<<": "<<endl;
		int r,c,chl=0;
		bool cempty[30];
		char cake[30][30],ori[30][30];
		for(int i=0;i<30;i++)
			for(int j=0;j<30;j++){
				cake[i][j]=0;
				ori[i][j]=0;
			}
		cin>>r>>c;
		for(int i=0;i<r;i++){
			bool allempty=1;
			for(int j=0;j<c;j++){
				cin>>cake[i][j];
				ori[i][j]=cake[i][j];
				if(cake[i][j]!='?'){
					allempty=0;
				}
			}
			cempty[i]=allempty;
		}
		for(int i=0;i<c;i++){
			for(int j=0;j<r;j++){
				if(ori[j][i]!='?'){
					int k=i+1;
					while(ori[j][k]=='?'&&k<c)cake[j][k++]=cake[j][i];
					k=i-1;
					while(cake[j][k]=='?'&&k>=0)cake[j][k--]=cake[j][i];
				}
			}
		}
	//	cout<<"hello"<<endl;
		for(int i=1;i<r;i++){
			if(cempty[i]&&(!cempty[i-1])){
				cempty[i]=0;
				for(int j=0;j<c;j++)cake[i][j]=cake[i-1][j];
			}
		}
		for(int i=r-2;i>=0;i--)
			if(cempty[i]&&(!cempty[i+1])){
				cempty[i]=0;
				for(int j=0;j<c;j++)
					cake[i][j]=cake[i+1][j];
			}
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				cout<<cake[i][j];
//				if(ori[i][j]!='?'&&ori[i][j]!=cake[i][j])cout<<"WRONG";
			}
			cout<<endl;
		}
		ii++;
	}
}

