#include <stdio.h>
#include <algorithm>
using namespace std;

struct mode
{
	int a,b;
};

mode cjob[200],jjob[200];

bool yee(mode a,mode b)
{
	return a.a<b.a;
}

int main()
{
	int t,ac,aj,i,x=0;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d",&ac,&aj);
		for(i=0;i<ac;i++) scanf("%d%d",&cjob[i].a,&cjob[i].b);
		if(ac) sort(cjob,cjob+ac,yee); 
		for(i=0;i<aj;i++) scanf("%d%d",&jjob[i].a,&jjob[i].b);
		if(aj) sort(jjob,jjob+aj,yee);
		if(ac+aj<2) printf("Case #%d: 2\n",++x);
		else if(ac==2 && aj==0)
		{
			if(cjob[1].a-cjob[0].b>=720 || cjob[0].a+1440-cjob[1].b>=720) printf("Case #%d: 2\n",++x);
			else printf("Case #%d: 4\n",++x);
		}
		else if(ac==0 && aj==2)
		{
			if(jjob[1].a-jjob[0].b>=720 || jjob[0].a+1440-jjob[1].b>=720) printf("Case #%d: 2\n",++x);
			else printf("Case #%d: 4\n",++x);
		}
		else printf("Case #%d: 2\n",++x);
	}
}
