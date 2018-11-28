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
void solve(int a)
{
	char str[1005];
	int n;
	scanf("%s",str);
	int k;inp(k);
	n = strlen(str);
	int count = 0;
	for(int i=0;i<=n-k;i++)
	{
		if(str[i]=='-'){
		for(int j=i;j<i+k;j++)
		{
			if(str[j]=='+')
			str[j]='-';
			else
			str[j]='+';
		}
		count++;
		}
	}
	int flag=1;
	for(int i=n-k+1;i<n;i++)
	{
		if(str[i]=='-')
		{flag=0;break;}
	}
	if(flag==0)
	printf("Case #%d: IMPOSSIBLE\n",a);
	else
	printf("Case #%d: %d\n",a,count);
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
