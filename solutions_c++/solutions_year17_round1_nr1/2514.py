#include<bits/stdc++.h>
using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	fstream in("A-large.in", ios::in);
	fstream out("GR.out",ios::out);
	int tc;
	in>>tc;
	for(int i=1;i<=tc;i++){
		int r,c;
		in>>r>>c;
		string gr[r];
		for(int j=0;j<r;j++){
			in>>gr[j];
		}
		char c2,c1;
		//int r1=0,r2=0,co1=0,co2=0;
		for(int j=0;j<r;j++){
			c2='?';
			for(int k=0;k<c;k++){
				c1=gr[j][k];
				if(c1!='?')
					c2=c1;
				else
					gr[j][k]=c2;
			}
		}
		c2='?';
		for(int j=0;j<r;j++){
			c2='?';
			for(int k=c-1;k>=0;k--){
				c1=gr[j][k];
				if(c1!='?')
					c2=c1;
				else
					gr[j][k]=c2;
				
			}
		}
		for(int j=0;j<c;j++){
			c2='?';
			for(int k=0;k<r;k++){
				c1=gr[k][j];
				if(c1!='?')
					c2=c1;
				else
					gr[k][j]=c2;
			}
		}
		for(int j=0;j<c;j++){
			c2='?';
			for(int k=r-1;k>=0;k--){
				c1=gr[k][j];
				if(c1!='?')
					c2=c1;
				else
					gr[k][j]=c2;
				
			}
		}
		out<<"Case #"<<i<<":"<<endl;
		for(int j=0;j<r;j++){
			out<<gr[j]<<endl;
		}
					
	}
	return(0);
}
		
	
