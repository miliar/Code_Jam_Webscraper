#include <bits/stdc++.h>
using namespace std;

int main(){
	ifstream in;
	in.open("A-large.in");
	ofstream out;
	out.open("alarge.txt");
	int t,r,c;
	in>>t;
	for(int k=1;k<=t;k++){
		in>>r>>c;
		int pi,pj;
		char ch='?';
		char a[r][c];
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				//printf("character input for matric[%d][%d]  %d , %d \n",r,c,i,j);
				in>>a[i][j];
			}
		}
		int lj=-1;
		int flag=1;
		for(int i=0;i<r;i++){
			lj=-1;
			ch='?';
			flag=1;
			//printf("something\n");
			for(int j=0;j<c;j++){
				if(a[i][j]!='?'&flag){
					ch = a[i][j];
					for(int k=lj+1;k<j;k++){
						a[i][k]=ch;
					}
					lj = j;
					flag=0;
				}else if(a[i][j]!='?'&!flag){
					ch = a[i][j];
				}else if(a[i][j]=='?'){
					a[i][j]=ch;
				}
			}
		}
		int li=-1;
		for(int j=0;j<c;j++){
			li=-1;
			ch='?';
			flag=1;
			//printf("something\n");
			for(int i=0;i<r;i++){
				if(a[i][j]!='?'&flag){
					ch = a[i][j];
					for(int k=li+1;k<i;k++){
						a[k][j]=ch;
					}
					li = i;
					flag=0;
				}else if(a[i][j]!='?'&!flag){
					ch = a[i][j];
				}else if(a[i][j]=='?'){
					a[i][j]=ch;
				}
			}
		}

		out<<"Case #"<<k<<": "<<endl;
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				out<<a[i][j];
			}
			out<<endl;
		}
	}
	return 0;
}