#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#define repp(a,b,c,d) for(int a=b; a<=c; a+=d)
#define rep(a,b,c) repp(a,b,c,1)
#define revv(a,b,c,d) for(int a=b; a>=c; a-=d)
#define rev(a,b,c) revv(a,b,c,1)
typedef long long ll;

char dat[25];
bool flag;
int main()
{
	int t;
	scanf("%d",&t);
	rep(tc,1,t)
	{
		scanf("%s",dat);
		int lg=strlen(dat)-1,idx;
		if(lg==0) printf("Case #%d: %s\n",tc,dat);
		else
		{
			flag=false;
			while(flag==false)
			{
				rep(i,0,lg-1)
				{
					if(dat[i]>dat[i+1])
					{
						idx=i;
						break;
					}
					if(i==lg-1 && dat[lg-1]<=dat[lg]) flag=true;
				}
				if(flag==true) break;
				rep(i,idx+1,lg) dat[i]='9';
				dat[idx]=((dat[idx]-'0')-1)+'0';
			}
			printf("Case #%d: ",tc);
			idx=0;
			while(dat[idx]=='0') idx++;
			rep(i,idx,lg) printf("%c",dat[i]);
			printf("\n");
		}
	}
	return 0;
}
