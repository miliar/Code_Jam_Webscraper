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

	ll t,r,c,i,j,k,cnt,num=1;
	char mat[100][100],ch,ans;
	scanf("%lld",&t);
	while(t--)
	{
		cnt=0;
		scanf("%lld%lld",&r,&c);
		for(i=0;i<r;i++)
		{
			ch=getchar();
			scanf("%[^\n]s",&mat[i]);
		}

		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
			{
				if(mat[i][j]=='?')
				{
					ans='*';
					if(j-1>=0 && mat[i][j-1]!='?')
					{
						ans=mat[i][j-1];
					}
					else
					{
						for(k=j+1;k<c;k++)
						{
							if(mat[i][k]!='?')
							{
								ans=mat[i][k];
								break;
							}
						}
					}

					if(ans!='*')
						mat[i][j]=ans;
					else
					{
						continue;
					}

				}
			}
		}

		for(j=0;j<c;j++)
		{
			for(i=0;i<r;i++)
			{
				if(mat[i][j]=='?')
				{
					ans='*';
					if(i-1>=0 && mat[i-1][j]!='?')
					{
						ans=mat[i-1][j];
					}
					else
					{
						for(k=i+1;k<r;k++)
						{
							if(mat[k][j]!='?')
							{
								ans=mat[k][j];
								break;
							}
						}
					}


					mat[i][j]=ans;
				}
			}
		}

		printf("Case #%lld:\n",num++);
		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
				printf("%c",mat[i][j]);
			printf("\n");
		}



	}	
	
	return 0;
}
