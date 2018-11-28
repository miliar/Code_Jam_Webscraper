#include <bits/stdc++.h>
using namespace std;
int main()
{	
	int tn,ti;
	scanf("%d",&tn);
	long long int ans=0;
	int n,k,i,j;
	for(ti=1;ti<=tn;ti++)
	{
		cin >> n >> k;
		vector<int> a(n+1,0);
		a[n]=1;
		int lastrs;
		int lastls;
		int x;
		for(i=0;i<k;)
		{
			for(j=n;j>0;j--)
			{
				if(a[j]>0)
				{
					x = a[j];
					a[j] = 0;
					if(j%2==0)
					{
						a[j/2-1] = a[j/2-1] + x;
						a[j/2] = a[j/2] + x;
						i = i + x;
						lastls = j/2-1;
						lastrs = j/2;
					}
					else
					{
						a[j/2] = a[j/2] + x;
						a[j/2] = a[j/2] + x;
						i = i + x;
						lastls = j/2;
						lastrs = j/2;
					}
					n = j;
					//cout << i << " " <<j << endl;
					break;
				}
			}
		}
		printf("Case #%d: ",ti);
		cout << max(lastrs,lastls) << " " << min(lastrs,lastls) << endl; 
		
	}
	return 0;
}