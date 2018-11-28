#include <cstdio>
#include <cstring>

int k,l,p;
char num[50];

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&k);
	for(int c=0;c<k;++c)
	{
		scanf("%s", num);
		l=strlen(num);
		p=0;
		for(int i=0;i<l-1;++i)
		{
			char c1=num[i], c2=num[i+1];
			if(c2==c1)continue;
			if(c2>c1)p=i+1;
			else
			{
				num[p]--;
				if(num[p]<'0')return 1;
				for(int j=p+1;j<l;++j)
					num[j]='9';
				break;
			} 
		}
		char* first=num;
		while(*first=='0')++first;
		printf("Case #%d: %s\n",c+1,*first==0?"0":first);
	}
	return 0;
}

