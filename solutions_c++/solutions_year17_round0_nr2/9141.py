/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
 * Created By : Muskan Agarwal
 * CSE, MNNIT-ALLAHABAD 
 * muskanagarwal469@gmail.com
 _._._._._._._._._._._._._._._._._._._._._.*/
 #include<bits/stdc++.h>
using namespace std;
 
#define MP make_pair
#define pb push_back
#define rep(i,n) for(int i=0;i<n;i++)
#define REP(i,a,b) for(int i=a;i<=b;i++)
#define PER(i,a,b) for(int i=b;i>=a;i--)
#define X first
#define Y second
 
 //i/o
#define inp(n) scanf("%d",&n)
#define inpl(n) scanf("%lld",&n)
#define inp2(n,m) inp(n), inp(m)
#define inp2l(n,m) inpl(n), inpl(m)
 
 
//cost
#define MOD 1000000007
#define MOD_INV 1000000006
#define MAX 100009
//#define INF 1000000005
#define INF 99999999999999999ll
const int N = 100002;
#define NINF -1000000005
#define mp make_pair
typedef long long ll;
typedef pair< pair<ll,ll>,ll > pairs;
int check(char str[20],int n)
{
	int i=0;
	while(i<n-1 && str[i]<=str[i+1])
	{
		i++;
	}
	
	return i;
	
}
void solve(int a)
{
	char ans[20];
	char str[20];
	scanf("%s",str);
	int i;
	int n = strlen(str);
	if(n==1)
	printf("Case #%d: %s\n",a,str);
	//printf("sdfs");
	else
	{
	   i = check(str,n);
		//printf("check %d\n",i);
		if(i==n-1)
		{
			printf("Case #%d: %s\n",a,str);
		//	return;
		}
		else
		{
			if(str[i]==str[0] && str[0]=='1')
			{
				for(int j=0;j<n-1;j++)
				ans[j]='9';
				ans[n-1]=0;
				printf("Case #%d: %s\n",a,ans);
				
			//	return;
				
			}
			else if(str[i]==str[0])
			{
				str[0]=str[0]-1;
				for(int j=1;j<n;j++)
				str[j]='9';
				printf("Case #%d: %s\n",a,str);
			}
			else
			{
				
				str[i]=str[i]-1;
				
				for(int j=i+1;j<n;j++)
				str[j]='9';
				printf("Case #%d: %s\n",a,str);
				//return;
				
			}
			
		}
	}
}
int main()
{
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;inp(t);
	int a=0;
	while(t--)
	{
		a++;
		solve(a);
	}
}
