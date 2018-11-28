#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

#define sc(x) scanf("%d",&x);
#define sc2(x,y) scanf("%d%d",&x,&y);
#define sc3(x,y,z) scanf("%d%d%d",&x,&y,&z);

#define scl(x) scanf("%lld",&x);
#define scl2(x,y) scanf("%lld%lld",&x,&y);
#define scl3(x,y,z) scanf("%lld%lld%lld",&x,&y,&z);

#define pb push_back
#define mp make_pair

#define M 1000000007
#define inf 99999999999999999LL	//long long inf

#define debug(x) cerr<<#x<<" :: "<<x<<"\n";
#define debug2(x,y) cerr<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\n";
#define debug3(x,y,z) cerr<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\t"<<#z<<" :: "<<z<<"\n";
#define debug4(x,y,z,a) cerr<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\t"<<#z<<" :: "<<z<<"\t"<<#a<<" :: "<<a<<"\n";

#define LIM 100020

char ch[400020]	;
int arr[50002];
int tamtam,leni;
void revert(int ind)
{
	int i;
	for(i=ind;i<ind+tamtam;i++)
	{
		arr[i] ^= 1;
	}
}
int tutu = 1;
int main()
{
	int i,j,t;
	sc(t);
	while(t--)
	{
		memset(arr,0,sizeof arr);
		scanf("%s %d",ch,&tamtam);
		int len = strlen(ch);
		leni = len;
		for(i=0;i<len;i++)
		{
			if(ch[i]=='+')
				arr[i] = 1;
		}
		int chutad  = 0;
		for(i=0;i+tamtam<=len;i++)
		{
			if(arr[i]==0)
			{	
				revert(i);
				chutad++;
			}
			else
			{
				continue;
			}
		}
		int flag = 0;
		for(i=0;i<len;i++)
		{
			if(arr[i]!=1)
				flag = 1;
		}
		if(flag)
		{
			printf("Case #%d: IMPOSSIBLE\n",tutu++);
		}
		else
		{
			printf("Case #%d: %d\n",tutu++,chutad);
		}
	}		
	return 0;
}