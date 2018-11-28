#include <stdio.h> 
#include <string.h>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long ll;
int w, h;
int t;
//int n, k, l;
ll n, k;

int min(int a, int b)
{
	if (a > b)return b;
	return a;
}
int max(int a, int b)
{
	if (a > b)return a;
	return b;
}
ll max(ll a,ll b)
{
	if(a>b)return a;
	return b;
}
ll min(ll a,ll b)
{
	if(a>b)return b;
	return a;
}

const int MAXN = 30;
typedef struct
{
	ll val;
	ll cnt;
}input;

input a[100][2];

input getLeft(input a)
{
	input ret;

	ret.val = 0, ret.cnt = 0;

	if(a.val == 0)
		return ret;

	ret.val = (a.val-1)/2 + (a.val-1)%2;
	ret.cnt = a.cnt;

	return ret;
}
input getRight(input a)
{
	input ret;

	ret.val = 0, ret.cnt = 0;
	if(a.val == 0)
		return ret;

	ret.val = (a.val-1)/2;
	ret.cnt = a.cnt;

	return ret;
}
int main()
{ 
	int tc, i;
	freopen("clarge.txt","r",stdin);
	freopen("clargeoutput.txt","w",stdout);
	scanf("%d",&tc);

	for(int t=1;t<=tc;t++)
	{
		scanf("%lld%lld", &n,&k);

		memset(a,0,sizeof(a));
		
		input l, r, root;

		root.val = n;
		root.cnt = 1;
	
		a[0][0] = root;

		for(i=1;i<100;i++)
		{
			l = getLeft(a[i-1][0]);
			r = getRight(a[i-1][0]);

			if(l.val > 0)
			{
				a[i][l.val%2].val = l.val;
				a[i][l.val%2].cnt += l.cnt;
			}
			if(r.val > 0)
			{
				a[i][r.val%2].val = r.val;
				a[i][r.val%2].cnt += r.cnt;
			}
			
			l = getLeft(a[i-1][1]);
			r = getRight(a[i-1][1]);

			if(l.val>0)
			{
				a[i][l.val%2].val = l.val;
				a[i][l.val%2].cnt += l.cnt;
			}
			if(r.val>0)
			{
				a[i][r.val%2].val = r.val;
				a[i][r.val%2].cnt += r.cnt;
			}
		}
		
		ll c=1;
		int idx;
		for(i=0;;i++)
		{
			if(a[i][0].val < a[i][1].val)
			{
				input e = a[i][0];
				a[i][0] =  a[i][1];
				a[i][1] = e;
			}
			if(a[i][0].cnt < k)
				k -= a[i][0].cnt;
			else
			{
				idx=0;
				break;
			}

			if(a[i][1].cnt < k)
				k -= a[i][1].cnt;
			else
			{
				idx=1;
				break;
			}
			
		}
		
		l = getLeft(a[i][idx]);
		r = getRight(a[i][idx]);
		printf("Case #%d: %lld %lld\n",t, max(l.val, r.val), min(r.val, l.val));

	}

	return 0;
}

