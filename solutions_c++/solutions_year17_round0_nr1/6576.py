#include<iostream>
#include<stdio.h>
#include<string>
#include<string.h>
#include<cstring>
#include<algorithm>
#include<vector>
#include<cmath>
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

string s;
int cnt,k;

void doing ()
{
	cnt=0;
	cin>>s>>k;
	int len=s.size();
	for (int i=0;i<len-k+1;i++)
	{
		if (s[i]=='-')
		{
			cnt++;
			for (int j=i;j<=i+k-1;j++)
			{
				if (s[j]=='+') s[j]='-';
				else s[j]='+';
			}
		}
	}
	bool p=0;
	for (int i=0;i<len;i++)
	{
		if (s[i]=='-')
		{
			p=1;break;
		}
	}
	if (p) cout<<"IMPOSSIBLE"<<endl;
	else cout<<cnt<<endl;
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


