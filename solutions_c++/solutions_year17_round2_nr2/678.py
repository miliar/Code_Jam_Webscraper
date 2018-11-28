#include<bits/stdc++.h>
using namespace std;
const int maxn=10000;
int pos[maxn],fin[1005];
char ans[1005];
int N;
void put(int num,int typ,int beg)
{
	for(int i=beg;i<N*6;i+=6)
		pos[i]=typ;
}
bool check(int n)
{
	for(int i=0;i<n;++i)
		if( (fin[i]&fin[(i+1)%n])!=0 )return false;
	return true;
}
int main()
{
	int T;
	scanf("%d",&T);
	int n,r,o,y,g,b,v;
	for(int cas=1;cas<=T;++cas)
	{
		scanf("%d",&n);
		scanf("%d%d%d %d%d%d",&r,&o,&y,&g,&b,&v);
		N=max( max(r,y), b);
		int mod=6*N;
		memset(pos,0,sizeof(pos));
		if(N==r)put(r,1,0),r=0;
		else if(N==y)put(y,2,2),y=0;
		else if(N==b)put(b,4,4),b=0;
		int cur=0;
		for(;r;--r,cur=(cur+6)%mod)
		{
			while(pos[cur])cur=(cur+1)%mod; 
			pos[cur]=1;
		}
		//for(int i=0;i<6*N;++i)cout <<pos[i]<<" ";cout <<endl;
		for(;y;--y,cur=(cur+6)%mod)
		{
			while(pos[cur])cur=(cur+1)%mod; 
			//cout <<cur<<endl;
			pos[cur]=2;
		}
		//for(int i=0;i<6*N;++i)cout <<pos[i]<<" ";cout <<endl;
		for(;b;--b,cur=(cur+6)%mod)
		{
			while(pos[cur])cur=(cur+1)%mod; 
			pos[cur]=4;
		}
		for(int i=0,j=0;i<6*N;++i)
			if(pos[i])fin[j++]=pos[i];
		if(check(n))
		{
			for(int i=0;i<n;++i)	
				if(fin[i]==1)ans[i]='R';
				else if(fin[i]==3)ans[i]='O';
				else if(fin[i]==2)ans[i]='Y';
				else if(fin[i]==6)ans[i]='G';
				else if(fin[i]==4)ans[i]='B';
				else if(fin[i]==5)ans[i]='V';
			ans[n]='\0';
			printf("Case #%d: %s\n",cas,ans);
		}
		else
			printf("Case #%d: IMPOSSIBLE\n",cas);
	}
	return 0;
}
