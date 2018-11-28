#include<iostream>
#include<cstdio>
#include<queue>

using namespace std;

void myPrint(char *l)
{
	int k, len, i;
	for(len=0; l[len]=='+' || l[len]=='-'; len++);
	l[len] = 0;
	sscanf(l+len+1, "%d", &k);
	queue<int> ends;
	char g = '+';
	int out = 0;
	for(i=0; i<len; i++)
	{
		if(!ends.empty() && i==ends.front())
		{
			g = (g=='+'? '-': '+');
			ends.pop();
		}
		if(l[i] == g)
			continue;
		if(i+k-1 >= len)
		{
			cout << "IMPOSSIBLE";
			return;
		}
		out++;
		ends.push(i+k);
		g = (g=='+'? '-': '+');
	}
	cout<< out;
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
