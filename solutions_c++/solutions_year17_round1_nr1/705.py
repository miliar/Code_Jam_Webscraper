#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int N,M;
char A[109][109];

void Copy(int i1,int i2){
	for(int j=1;j<=M;j++) A[i1][j]=A[i2][j];
}

void Init(){
	cin>>N>>M;
	for(int i=1;i<=N;i++){
		string tmp;
		cin>>tmp;
		for(int j=1;j<=M;j++)
			A[i][j]=tmp[j-1];
	}
}

void Solve(){
	for(int i=1;i<=N;i++){
		char c='?';
		for(int j=1;j<=M;j++){
			if(A[i][j]=='?') A[i][j]=c;
			else{
				if(c=='?'){
					for(int j2=1;j2<j;j2++) A[i][j2]=A[i][j];
				}
				c=A[i][j];
			}
		}
	}
	int d=-1;
	for(int i=1;i<=N;i++){
		if(A[i][1]=='?'){
			if(d!=-1) Copy(i,d);
		}else{
			if(d==-1){
				for(int i2=1;i2<i;i2++) Copy(i2,i);
			}
			d=i;
		}
	}
}

void Output(){
	for(int i=1;i<=N;i++){
		for(int j=1;j<=M;j++) cout<<A[i][j];
		cout<<"\n";
	}
}

int main(){
	int Test;
	cin>>Test;
	for(int i=1;i<=Test;i++){
		Init();
		Solve();
		cout<<"Case #"<<i<<":\n";
		Output();
	}
}