#include <iostream>

using namespace std;

long long f[20][10],res,n,ntest,x;
string s;

void cal(int pos)
{
	if (pos==s.length()) 
	{
		res++;
		return;
	}
	int last=1;
	if (pos) last=s[pos-1]-'0';
	for (int i=last;i<s[pos]-'0';i++)
		res+=f[n-pos][i];
	//cout << res << "\n";
	if (pos==0 or s[pos]>=s[pos-1]) cal(pos+1); 
}

string itos(long long x)
{
	string ret="";
	while (x) ret+=x%10+'0',x/=10;
	reverse(ret.begin(),ret.end());
	return ret;
}

long long count(long long x)
{
	s=itos(x);
	n=s.length();
	res=0;
	cal(0);
	for (int i=1;i<n;i++)
		for (int j=1;j<=9;j++)
				res+=f[i][j];
	return res;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	for (int i=1;i<10;i++)
		f[1][i]=1;
	for (int i=1;i<=18;i++)
		for (int j=1;j<=9;j++)
			for (int k=j;k>=1;k--)
				f[i+1][k]+=f[i][j];
	cin >> ntest;
	for (int __=1;__<=ntest;__++)
	{
		cin >> x;
		long long l=1,r=x,ret=x,bound=count(x);
		while (l<=r)
		{
			long long m=(l+r)/2;
			if (count(m)==bound) ret=m,r=m-1;
			else l=m+1;
		}
		cout << "Case #" << __ << ": ";
		cout << ret << "\n";
	}
}