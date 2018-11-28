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

	ll t,len,i,j,num=1;
	char ch,str[50];
	scanf("%lld",&t);
	while(t--)
	{
		ch=getchar();
		scanf("%[^\n]s",str);
		len=strlen(str);
		if(len==1)
		{	
			printf("Case #%lld: %s\n",num++,str);
			continue;
		}

		for(i=len-1;i>0;i--)
		{
			if(str[i]<str[i-1])
			{
				str[i-1]-=1;
				str[i]='9';
			}
		}

		for(i=0;i<len-1;i++)
		{
			if(str[i]>str[i+1])
			{
				str[i+1]='9';
			}
		}

		printf("Case #%lld: ",num++);
		for(i=0;i<len;i++)
		{
			if(str[i]!='0')
			{
				printf("%c",str[i]);
			}
		}
		printf("\n");

	}

	
	return 0;
}
