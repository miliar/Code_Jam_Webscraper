#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
	int T;
	scanf("%d ", &T);
	for(int t=1; t<=T; t++)
	{
		cout << "Case #" << t << ": ";
		int N, n[6], i, l=0, first=0;
		const char *name = "ROYGBV";
		scanf("%d %d %d %d %d %d %d ", &N, &n[0], &n[1], &n[2], &n[3], &n[4], &n[5]);
		for(i=0;i<6;i++)
		{
			if(n[(i+4)%6]>(n[(i)%6]+n[(i+1)%6]+n[(i+2)%6]))
				break;
		}
		if(i<6)
		{
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		while(N--)
		{
			l+=2;
			l%=6;
			if((n[l]>n[(l+1)%6] && n[l]>n[(l+2)%6]) ||
				(first==l && (n[l]>=n[(l+1)%6] && n[l]>=n[(l+2)%6])))
			{
				cout << name[l];
				n[l]--;
				if(!first)
					first = l;
				if(n[l]<0)
					cout<<endl<<"ERROR"<<endl;
				continue;
			}
			l++;
			l%=6;
			if(n[l]>n[(l+1)%6] || (first==l && n[l]>=n[(l+1)%6]))
			{
				cout << name[l];
				n[l]--;
				if(!first)
					first = l;
				if(n[l]<0)
					cout<<endl<<"ERROR"<<endl;
				continue;
			}
			l++;
			l%=6;
			cout << name[l];
			n[l]--;
			if(!first)
				first = l;
			if(n[l]<0)
				cout<<endl<<"ERROR"<<endl;
		}
		cout<<endl;
	}
	return 0;
}

