#include<bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for(int l=1;l<=t;l++)
	{
		
		char c[1009];
		int a;
		scanf("%s %d",c,&a);
		int freq=0;
		int i,f1=0;
		for(i=0;i<1009;i++)
		{
			if(c[i]=='-')
			{
			//	f1=1;
				}
			else if(c[i]=='+')
			{}
			else 
				break;
		}
		int s=i;
		//cout << s << endl;
		for(i=0;i<=(s-a);i++)
		{

			if(c[i]=='-')
			{
				for(int j=0;j<a;j++)
				{
					if(c[i+j]=='-')
						c[i+j]='+';
					else
						c[i+j]='-';
				}
				freq++;
			}
			//cout << c << endl;
		}
		for(i=0;i<s;i++)
		{
			if(c[i]=='-')
			{
				f1=1;
				break;
			}
		}
		if(f1==1)
		{
			cout << "Case #"<< l << ": IMPOSSIBLE" << endl;
			
		}
		else
		{
			cout << "Case #"<< l << ": " << freq << endl;
		}
	}

	return 0;
}
