/*
 	Pulkit Mittal											Idea of complexities:																				
 	Reg. No. - 20143049										n=50	   O(n^4)
 	CSE, MNNIT - Allahabad									n=100-500  O(n^3)
															n=1000 	   O(n2logn)
 															n=10^4	   O(n^2)
 															n=10^5	   O(nlogn)

*/		
	

#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;

#define MOD 1000000007
#define MOD_INV 1000000006
#define INF 999999999
#define MAX 100009

#define mp make_pair
#define pb push_back
#define rep(i,n) for(i=0;i<n;i++)
#define per(i,n) for(i=n;i>=0;i--)
#define REP for(i=a;i<=b;i++)
#define PER for(i=b;i>=a;i--)

#define X first
#define Y second
#define all(c) c.begin(),c.end()	//eg. sort(all(c))

#define tr(Co, it) for(typeof(Co.begin()) it = Co.begin(); it != Co.end(); it++)
#define present(container,element)	(container.find(element)!=container.end())  //for set,map
#define cpresent(container,element) (find(all(container),element)!=container.end())	//for vector

typedef vector<int> vi;
typedef vector< vi > vvi;
typedef pair< int,int > pp;

#define sz(a) int((a).size)
#define clr(a) memset(a,0,sizeof(a))
#define ini(a) memset(a,-1,sizeof(a))



int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	ll t,k,len,i,j,cnt,f;
	char str[1005],ch;

	scanf("%lld",&t);
	ll num=1;
	while(t--)
	{
		ch=getchar();
		scanf("%s %lld",str,&k);
		//printf("str=%s k=%lld\n",str,k);
		len=strlen(str);
		cnt=0;
		f=1;
		for(i=0;i<=len-k;i++)
		{
			if(str[i]=='+')
				continue;
			for(j=i;j<i+k;j++)
			{
				if(str[j]=='-')
					str[j]='+';
				else
					str[j]='-';
			}
			cnt++;
		}

		for(i=0;i<len;i++)
		{
			if(str[i]=='-')
			{
				f=0;
				break;
			}
		}

		if(f==0)
			printf("Case #%lld: IMPOSSIBLE\n",num++);
		else
			printf("Case #%lld: %lld\n",num++,cnt);

	}
	
	return 0;
}
