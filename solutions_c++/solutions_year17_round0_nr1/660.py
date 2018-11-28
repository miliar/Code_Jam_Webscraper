#include <stdio.h>
#include <string.h>
char in[1005];
int notplus()
{
	int i;
	for(i=0;in[i]=='+';i++);
	return i;
}
void doe()
{
	int n,ans=0,len,t,i;
	scanf("%s",in);
	scanf("%d",&n);
	len=strlen(in);
	t=notplus();
	while(t!=len)
	{
		if(t>len-n)
		{
			printf("IMPOSSIBLE\n");
			return;
		}
		for(i=0;i<n;i++)
		{
			if(in[t+i]=='-')
				in[t+i]='+';
			else
				in[t+i]='-';
		}
		t=notplus();
		ans++;
	}
	printf("%d\n",ans);
}
int main()
{
	freopen("in.txt","r",stdin);
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