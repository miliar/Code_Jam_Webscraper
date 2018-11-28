#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<ctime>
#include<cmath>
#include<iostream>
#include<queue>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<string>
using namespace std;
typedef long long ll;
typedef double db;
typedef pair<db,db> per;
const int MOD = 1000000007;
const int INF = 1000000007;
const int N = 1005;
int a[N],t[N];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,ca=1;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ",ca++);
		int n,p;
		scanf("%d%d",&n,&p);
		int ret=0,sum=0;
		for(int i=0;i<n;i++){scanf("%d",&a[i]);sum+=a[i];}
		memset(t,0,sizeof(t));
		for(int i=0;i<n;i++)
		{
			if(a[i]%p==0)ret++;
			t[a[i]%p]++;
		}
		//printf("t1:%d t2:%d \n",t[1],t[2]);
		if(p==2)
		{
			ret+=t[1]/2+t[1]%2;
		}
		else if(p==3)
		{
			if(t[1]>=t[2])
			{
				ret+=t[2];
				t[1]-=t[2];
				ret+=t[1]/3+(t[1]%3!=0);
			}
			else
			{
				ret+=t[1];
				t[2]-=t[1];
				ret+=t[2]/3+(t[2]%3!=0);
			}
		}
		else
		{
			ret+=t[2]/2;
			t[2]%=2;
			ret+=min(t[1],t[3]);
			if(t[1]>=t[3])
			{
				t[1]-=t[3];
				if(t[2]&&t[1]>=2)
				{
					ret++;
					t[1]-=2;
					ret+=t[1]/4+(t[1]%4!=0);
				}
				else if(t[2])
				{
					ret++;
				}
				else
				{
					ret+=t[1]/4+(t[1]%4!=0);
				}
			}
			else
			{
				t[3]-=t[1];
				if(t[2]&&t[3]>=2)
				{
					ret++;
					t[3]-=2;
					ret+=t[3]/4+(t[3]%4!=0);
				}
				else if(t[2])
				{
					ret++;
				}
				else
				{
					ret+=t[3]/4+(t[3]%4!=0);
				}
			}
		}
		printf("%d\n",ret);
	}
	return 0;
}

