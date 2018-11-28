#include<iostream>
#include<cstdio>

using namespace std;

long long calc(long long n, long long k)
{
	if(k==1)
		return n;
	n--;
	k--;
	if(k&1)
		return calc(n/2 + n%2, k/2 + 1);
	else
		return calc(n/2, k/2);
}

void myPrint(char *line)
{
	long long N, K, o, l, r;
	sscanf(line, "%lld %lld", &N, &K);
	N = calc(N,K)-1;
	cout<< (N/2 + N%2)<<' '<<(N/2);
}

int main()
{
	int T;
	char line[1010];
	gets(line);
	sscanf(line, "%d", &T);
	for(int t=1; t<=T; t++)
	{
		gets(line);
		cout<<"Case #"<<t<<": ";
		myPrint(line);
		cout<<endl;
	}
	return 0;
}
