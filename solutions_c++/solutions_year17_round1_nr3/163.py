#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <unordered_map>
using namespace std;
#define rep(i,n) for(int i=1;i<=(n);++i)
#define rep2(i,a,b) for(int i=(a);i<=(b);++i)
unordered_map<string,int> mym;

struct state_t
{
	int myhp;
	int myatk;
	int bthp;
	int btatk;
}init;
queue<state_t> myq;
string hasher(state_t is)
{
	char buffer[101];
	sprintf(buffer,"%d,%d,%d,%d",is.myhp,is.myatk,is.bthp,is.btatk);
	return buffer;
}
int nbuff,ndebuff;
void task()
{
	scanf("%d%d%d%d%d%d",&init.myhp,&init.myatk,&init.bthp,&init.btatk,&nbuff,&ndebuff);
	while(!myq.empty())myq.pop();
	mym.clear();
	myq.push(init);
	mym[hasher(init)]=0;
	while(!myq.empty())
	{
		state_t pf=myq.front();myq.pop();
		int result=mym[hasher(pf)];
		rep(choice,4)
		{
			state_t pt=pf;
			switch(choice)
			{
			case 1:
				pt.bthp-=pt.myatk;
				break;
			case 2:
				pt.myatk+=nbuff;
				break;
			case 3:
				pt.myhp=init.myhp;
				break;
			case 4:
				pt.btatk-=ndebuff;
				if(pt.btatk<0)
					pt.btatk=0;
				break;
			}
			if(pt.bthp<=0)
			{
				printf("%d\n",result+1);
				return;
			}
			else
			{
				pt.myhp-=pt.btatk;
				if(pt.myhp<=0)
					continue;
			}
			string hashed=hasher(pt);
			if(mym.find(hashed)==mym.end())
			{
				mym[hashed]=result+1;
				myq.push(pt);
			}
		}
	}
	printf("IMPOSSIBLE\n");
}
int main()
{
	freopen("C.in","r",stdin);
	//freopen("C.out","w",stdout);
	int nt;scanf("%d",&nt);
	rep(i,nt){printf("Case #%d: ",i);task();}
}
