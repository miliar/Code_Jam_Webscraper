/*gcj-2014-qr-b1.cpp*/
#include<stdio.h>
#include<string.h>

int tcases;
size_t n;

int nodec()
{
	char s[25], flag=1;
	sprintf(s, "%llu", n);
	for(int i=1; s[i]; i++)
	{
		if(s[i]<s[i-1])
		{
			flag--;
			break;
		}
	}
	return flag;
}

void sol()
{
	size_t ans=0;
	int ratio;
	char s[25], rec, pos;
	sprintf(s, "%llu", n);
	for(int i=1; s[i]; i++)
	{
		if(s[i]<s[i-1])
		{
			ratio=i-1;
			rec=s[i-1];
			break;
		}
	}
	pos=ratio;
	while(s[pos]==rec) pos--;
	pos++;
	s[pos]--;
	for(int i=pos+1; s[i]; i++) s[i]='9';
	for(int i=0; s[i]; i++) ans=ans*10+s[i]-48;
	printf("%llu\n", ans);
}

int main()
{
	//freopen("B.in", "r", stdin);
	//freopen("Bout.txt", "w", stdout);
	int kase=1;
	for(scanf("%d", &tcases); tcases--;)
	{
		scanf("%llu", &n);
		printf("Case #%d: ", kase++);
		if(1<=n&&n<=9) printf("%llu\n", n);
		else if(nodec()) printf("%llu\n", n);
		else sol();
	}
	return 0;
}
