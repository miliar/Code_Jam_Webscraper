#include<iostream>
#include<stdio.h>
#include<string>
#include<string.h>
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

void doing ()
{
	cin>>s;
	int len=s.size();
	if (len==1)
	{
		cout<<s<<endl;return;
	}
	int pos;bool p=0;
	for (int i=1;i<len;i++)
	{
		if (s[i]<s[i-1])
		{
			p=1;
			pos=i;break;
		}
	}
	if (!p)
	{
		cout<<s<<endl; return;
	}
	s[pos-1]-=1;
	for (int i=pos;i<len;i++) s[i]='9';
	for (int i=pos-1;i>=1;i--)
	{
		if (s[i]<s[i-1])
		{
			s[i]='9';
			s[i-1]--;
		}
		else break;
	}
	int temp=0;
	for (int i=0;i<len;i++)
	{
		temp=i;
		if (s[i]!='0') break;
	}
	for (int i=temp;i<len;i++) cout<<s[i];
	cout<<endl;
}

int main ()
{
	freopen("xx.in","r",stdin);
	freopen("xx.out","w",stdout);
	int T;
	cin>>T;
	for (int ca=1;ca<=T;ca++)
	{
	  printf("Case #%d: ",ca);
	  doing ();
    }
	return 0;
}


