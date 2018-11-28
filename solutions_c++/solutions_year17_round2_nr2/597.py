#include<cstdio>
#include<cstring>
#include<string>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<cmath>
#include<iostream>
#define fi first
#define se second
#define MP make_pair
#define PB push_back
#define PII pair<int,int>
typedef long long LL;
using namespace std;
int l,T;
char s[100];
template<class T>
void read(T&x)
{
	char ch=getchar();int mk=1;x=0;for(;ch!='-'&&(ch<'0'||ch>'9');ch=getchar());
	if (ch=='-') mk=-1,ch=getchar();for(;ch>='0'&&ch<='9';ch=getchar()) x=x*10+ch-48;x*=mk;
}
bool check()
{
	for(int i=1;i<l;i++)
		if (s[i-1]>s[i]) return 0;
	return 1;
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	read(T);
	for(int _=1;_<=T;_++)
	{
		printf("Case #%d: ",_);
		scanf("%s",s);
		l=strlen(s);
		for(int i=l-2;i>=0&&!check();i--)
		{
			s[i]--;
			s[i+1]='9';
		}
		bool pre=1;
		for(int i=0;i<l;i++)
		{
			if (s[i]>'0') pre=0;
			if (!pre||s[i]>'0') printf("%c",s[i]);
		}
		printf("\n");
	}
	return 0;
}

