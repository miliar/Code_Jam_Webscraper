#include <iostream>
using namespace std;
int main()
{
	int t,t1=0;
	cin>>t;
	while(t1<t)
	{
		int N,k,count=1;
		cin>>N>>k;
		int maxind=0;
		int minind=0;
		int maxdiff=-1;
		int find=0;
		int sind=0;
		char a[N+2];
		for(int i=1;i<N+1;i++)
			a[i]='e';
		a[0]='o';
		a[N+1]='o';
		int ind[k+2];
		for(int i=1;i<k+1;i++)
			ind[i]=-1;
		ind[0]=0;
		ind[k+1]=N+1;
		while(count<=k)
		{
			find=0;
			maxdiff=-1;
			maxind=0;
			minind=0;
			for(int i=1;i<=k+1;i++)
			{
				if((ind[i]!=-1))
				{
					sind=i;
					if((ind[sind]-ind[find])>maxdiff)
					{
						maxdiff=ind[sind]-ind[find];
						minind=ind[find];
						maxind=ind[sind];
						find=sind;
					}
					else
						find=sind;
				}
			}
			a[(maxind/2)+(minind/2)]='o';
			ind[count]=(maxind/2)+(minind/2)+((maxind%2)+(minind%2))/2;
			//ind[count]=(maxind+minind)/2;
			if(count==k)
			{
				cout<<"Case #"<<t1+1<<": ";
				int LS=ind[count]-minind-1;
				int RS=maxind-ind[count]-1;
				if(LS>=RS)
					cout<<LS<<" "<<RS<<endl;
				else
					cout<<RS<<" "<<LS<<endl;
			}
			int index=1;
						for(int x=count-1;x>=0;x--)
						{
							if(ind[x+1]>=ind[x])
							{
								break;
							}
							else
							{
								int temp=ind[x];
								ind[x]=ind[x+1];
								ind[x+1]=temp;
							}
						}
			count++;
		}
		t1++;
	}
	return 0;
}

