#include<iostream>
#include<stdio.h>
#include<string>
#include<string.h>
#include<cstring>
#include<algorithm>
#include<vector>
#include<cmath>
#include<queue>
using namespace std;

#define ll long long

ll read()
{
    ll x=0,f=1;char c=getchar();
    while(c<'0'||c>'9'){if(c=='-')f=-1;c=getchar();}
    while(c>='0'&&c<='9'){x=x*10+c-'0';c=getchar();}
    return x*f;
}

inline void out (int x)
{
	if (x>9) out(x/10);
	putchar (x%10+'0');
}

int n,k;
priority_queue<int>q;

void doing ()
{
	scanf("%d%d",&n,&k);
	while (!q.empty()) q.pop();
	q.push(n);
	for (int i=1;i<=k-1;i++)
	{
		int t=q.top();
		q.pop();
		if (t&1)
		{
		    q.push(t>>1);
		    q.push(t>>1);
		}
		else
		{
			q.push(t>>1);
			q.push(t-(t>>1)-1);
		}
	}
	int t=q.top();
//	cout<<t<<endl;
	if (t&1)
	{
		cout<<(t>>1)<<" "<<(t>>1)<<endl;
	}
	else
	{
		int t1=max((t>>1)-1,(t>>1));
		int t2=min((t>>1)-1,(t>>1));
		cout<<t1<<" "<<t2<<endl;
	}
}

int main ()
{
	freopen("xx.in","r",stdin);
	freopen("xx.out","w",stdout);
	int T;
	cin>>T;
	for (int i=1;i<=T;i++)
	{
	  printf("Case #%d: ",i);
	  doing ();
    }
	return 0;
}


