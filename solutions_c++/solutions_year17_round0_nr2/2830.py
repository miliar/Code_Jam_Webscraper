#include<iostream>
#include<cstdio>
#include<queue>

using namespace std;

void myPrint(char *l)
{
	unsigned long long N, o, t;
	sscanf(l, "%lld", &N);
	for(o=1;o<=N;o*=10)
	{
		t = N/o;
		t%=100;
		if(t%10 < t/10)
		{
			t = N/o;
			t/=10;
			t--;
			t*=o*10;
			N=t+o*10-1;
		}
	}
	cout<< N;
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
