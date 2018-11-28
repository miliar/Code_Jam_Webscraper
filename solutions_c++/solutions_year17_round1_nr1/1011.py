#include<iostream>
#include<cstring>
#include<cstdio>
#include<vector>
#include<cmath>
#include<sstream>
#include<algorithm>
#include<set>
#include<queue>
#include<map>
#include <stdlib.h> 
using namespace std;

int main(){
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	
	int tc;
	cin>>tc;
	
	for(int caso=1;caso<=tc;caso++){
		cout<<"Case #"<<caso<<":"<<endl;
		
		int R,C;
		cin>>R>>C;
		char c[R][C];
		
		set<char>S;
		
		for(int i=0;i<R;i++)
			for(int j=0;j<C;j++){
				cin>>c[i][j];
				if(c[i][j]!='?')
					S.insert(c[i][j]);	
			}
		
		vector<char>v(S.begin(),S.end());
		
		int Mini[1001];
		int Maxi[1001];
		int Minj[1001];
		int Maxj[1001];
		
		
		for(int ii=0;ii<v.size();ii++){
			char ch=v[ii];
			int mini=1<<20;int maxi=0;int minj=1<<20;int maxj=0;
			for(int i=0;i<R;i++)
				for(int j=0;j<C;j++){
					if(c[i][j]==ch){
						mini=min(mini,i);
						maxi=max(maxi,i);
						minj=min(minj,j);
						maxj=max(maxj,j);
					}	
				}
			
			for(int i=mini;i<=maxi;i++)
				for(int j=minj;j<=maxj;j++)
					c[i][j]=ch;
			
			Mini[ii]=mini;
			Maxi[ii]=maxi;
			Minj[ii]=minj;
			Maxj[ii]=maxj;
		}
		
		for(int i=0;i<R;i++)
			for(int j=0;j<C;j++)
				if(c[i][j]=='?'){
					for(int ii=0;ii<v.size();ii++){
						int mini=Mini[ii];
						int maxi=Maxi[ii];
						int minj=Minj[ii];
						int maxj=Maxj[ii];
						mini=min(mini,i);
						maxi=max(maxi,i);
						minj=min(minj,j);
						maxj=max(maxj,j);
						bool yes=1;
						for(int i2=mini;i2<=maxi;i2++)
							for(int j2=minj;j2<=maxj;j2++)
								if(c[i2][j2]!='?' && c[i2][j2]!=v[ii])
									yes=0;
						
						if(yes==1){
							for(int i2=mini;i2<=maxi;i2++)
								for(int j2=minj;j2<=maxj;j2++)
									c[i2][j2]=v[ii];
							Mini[ii]=mini;
							Maxi[ii]=maxi;
							Minj[ii]=minj;
							Maxj[ii]=maxj;
							break;
						}
					}
				}
		
		
		for(int i=0;i<R;i++){
			for(int j=0;j<C;j++)
				cout<<c[i][j];
			cout<<endl;
		}
	}
	
	return 0;
}


