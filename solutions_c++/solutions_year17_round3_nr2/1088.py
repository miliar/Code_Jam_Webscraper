#include<bits/stdc++.h>
using namespace std;

int X[5][2],Y[5][2];

int main(){
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,tt,i,x,y;
	scanf("%d",&t);
	for(tt=1;tt<=t;++tt){
		scanf("%d %d",&x,&y);
		for(i=0;i<x;++i)
			scanf("%d %d",&X[i][0],&X[i][1]);
		for(i=0;i<y;++i)
			scanf("%d %d",&Y[i][0],&Y[i][1]);
		printf("Case #%d: ",tt);
		if((x+y)==1){
			cout<<"2"<<endl;
			continue;
		}
		else if(x==1&&y==1){
			cout<<"2"<<endl;
			continue;
		}
		if(x==2){
			if(X[0][0]>X[1][0]){
				int tx=X[0][0];
				int ty=X[0][1];
				X[0][0]=X[1][0];
				X[0][1]=X[1][1];
				X[1][0]=tx;
				X[1][1]=ty;
			}
		}
		if(y==2){
			if(Y[0][0]>Y[1][0]){
				int tx=Y[0][0];
				int ty=Y[0][1];
				Y[0][0]=Y[1][0];
				Y[0][1]=Y[1][1];
				Y[1][0]=tx;
				Y[1][1]=ty;
			}
		}
		if(x==(x+y)||y==(x+y)){
			if(x==(x+y)){
				if(X[x-1][1]<=720)
					cout<<"2"<<endl;
				else if(X[0][0]>=720)
					cout<<"2"<<endl;
				else if(X[x-1][1]-X[0][0]<=720)
					cout<<"2"<<endl;
				else if(X[x-1][0]-X[0][1]>=720)
					cout<<"2"<<endl;
				else
					cout<<"4"<<endl;
			}
			else if(y==(x+y)){
				if(Y[y-1][1]<=720)
					cout<<"2"<<endl;
				else if(Y[0][0]>=720)
					cout<<"2"<<endl;
				else if(Y[y-1][1]-Y[0][0]<=720)
					cout<<"2"<<endl;
				else if(Y[y-1][0]-Y[0][1]>=720)
					cout<<"2"<<endl;
				else
					cout<<"4"<<endl;
			}
		}
	}
	return 0;
}
