//Author:CookiC
//#include"stdafx.h"
#include<iostream>
#define maxn 50
//#pragma warning(disable : 4996)
using namespace std;

int R,C;
bool vis[maxn][maxn];
char s[maxn][maxn];

void paint(int bx,int by,int ex,int ey,char c){
	int i,j;
	for(i=bx;i<ex;++i)
		for(j=by;j<ey;++j){
			vis[i][j]=1;
			s[i][j]=c;
		}
}

void find(int bx,int by){
	char c;
	int i,j,ex,ey;
	c=0;
	for(i=0;i+bx<R&&!c;++i)
		for(j=0;j+by<C&&!c;++j)
			if(s[i+bx][j+by]!='?')
				c=s[i+bx][j+by];
	ex=i+bx;
	ey=j+by;
	while(ey<C){
		for(i=bx;i<ex&&(s[i][ey]=='?'||s[i][ey]==c);++i);
		if(i<ex)
			break;
		++ey;
	}
	while(ex<R){
		for(j=by;j<ey&&(s[ex][j]=='?'||s[ex][j]==c);++j);
		if(j<ey)
			break;
		++ex;
	}
	paint(bx,by,ex,ey,c);
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	ios::sync_with_stdio(false);
	
	int N,T,i,j;
	cin>>N;
	for(T=1;T<=N;++T){
		cin>>R>>C;
		for(i=0;i<R;++i)
			cin>>s[i];
		for(i=0;i<R;++i)
			for(j=0;j<C;++j)
				vis[i][j]=0;
		
		int bx=-1,by=-1,ex=-1,ey=-1;
		for(i=0;i<R;++i)
			for(j=0;j<C;++j)
				if(!vis[i][j])
					find(i,j);
		
		cout<<"Case #"<<T<<":\n";
		for(i=0;i<R;++i)
			cout<<s[i]<<endl;
	}
	return 0;
}

