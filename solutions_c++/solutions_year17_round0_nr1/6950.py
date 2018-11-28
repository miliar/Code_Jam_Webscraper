#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
long long arr[100009],has[100009],cnt=0;


#define mp make_pair
#define pb push_back

ll gcd(ll a ,ll b)
{
	if(b%a==0) return a;
	else return gcd(b%a,a);
}
int main()
{
	int  n,m,i,j,k,a=1,b,x,t,y,z,c;
	freopen("A-large.in", "r", stdin);
    freopen("output.out", "w", stdout);
	scanf("%d",&t);
	while(t--)
	{
		char str[1009];
		scanf("%s %d",str,&k);
		n=strlen(str);m=0;
		for(i=0;i<=n-k;i++)
		{
			if(str[i]=='-')
			{m++;
				for(j=i;j<i+k;j++)
				{
					if(str[j]=='-') str[j]='+';
					else str[j]='-';
				}
			}
		}
		for(i=0;i<n;i++)
		{
			if(str[i]=='-') break;
		}
		if(i==n) printf("Case #%d: %d\n",a++,m);
		else printf("Case #%d: IMPOSSIBLE\n",a++);
	}
	return 0;
}
