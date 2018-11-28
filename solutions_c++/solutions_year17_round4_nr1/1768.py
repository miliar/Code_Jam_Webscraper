#include <stdio.h>
int w[105];
void doe()
{
	int n,p,i,x=0,y=0,z=0,a=0,wtf;
	scanf("%d %d",&n,&p);
	for(i=1;i<=n;i++)
		scanf("%d",&w[i]);
	if(p==2)
	{
		for(i=1;i<=n;i++)
		{
			if(w[i]%2==0)
				x++;
			else
				y++;
		}
		printf("%d\n",x+((y+1)/2));
		return;
	}
	if(p==3)
	{
		for(i=1;i<=n;i++)
		{
			if(w[i]%3==0)
				x++;
			else if(w[i]%3==1)
				y++;
			else
				z++;
		}
		a=x;
		if(y>z)
		{
			a+=z;
			y-=z;
		}
		else
		{
			a+=y;
			z-=y;
			y=z;
		}
		a+=(y+2)/3;
		printf("%d\n",a);
		return;
	}
}
int main()
{
	freopen("in.in","r",stdin);
	freopen("out.txt","w",stdout);
	int n,i;
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		printf("Case #%d: ",i);
		doe();
	}
	return 0;
}