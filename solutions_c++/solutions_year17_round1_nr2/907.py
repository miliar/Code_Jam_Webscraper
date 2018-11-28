#include <stdlib.h>
#include <time.h>
#include <vector>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;


const int M=100;

int array[M][M];

int flag[M][M];

int ingre[M];

int main()
{
	
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	
	freopen("B-large.in","r",stdin);
	freopen("output_large.out","w",stdout);
	
	int T;
	cin>>T;
	
	for (int cnt=1; cnt<=T; cnt++)
	{
		int N,P;
		cin>>N>>P;
		
		for (int i=0; i<N; i++)
		{
			cin>>ingre[i];
		}
		for (int i=0; i<N; i++)
		{
			for (int j=0; j<P; j++)
			{
				cin>>array[i][j];
			}
		}
		
		for (int i=0; i<N; i++)
		{
			sort(array[i],array[i]+P);
		}
		
		/*for (int i=0; i<N; i++)
		{
			for (int j=0; j<P; j++)
			{
				cout<<array[i][j]<<" ";
			}
			cout<<endl;
		}*/
		
		for (int i=0; i<M; i++)
		{
			for (int j=0; j<M; j++)
			{
				flag[i][j]=0;
			}
		}
		
		for (int j=0; j<P; j++)
		{
			flag[N-1][j]=1;
		}
		
		if (N==1)
		{
			int ans=0;
			for (int i=0; i<P; i++)
			{
				int upper=10*array[0][i]/(9*ingre[0]);
				int lower=10*array[0][i]/(11*ingre[0])+(10*array[0][i]%(11*ingre[0])!=0);
				//cout<<"i="<<i<<endl;
				//cout<<"lower="<<lower<<endl;
				//cout<<"upper="<<upper<<endl;
				if (lower<=upper)
				{
					ans++;
				}
			}
			cout<<"Case #"<<cnt<<": "<<ans<<endl;
		}
		else
		{
			for (int i=N-2; i>=0; i--)
			{
				int index=0;
				for (int j1=0; j1<P; j1++)
				{
					int upper1=10*array[i][j1]/(9*ingre[i]);
					int lower1=10*array[i][j1]/(11*ingre[i])+(10*array[i][j1]%(11*ingre[i])!=0);
					for (int j2=index; j2<P; j2++)
					{
						int upper2=10*array[i+1][j2]/(9*ingre[i+1]);
						int lower2=10*array[i+1][j2]/(11*ingre[i+1])+(10*array[i+1][j2]%(11*ingre[i+1])!=0);
						
						if (lower1<=upper1 && lower2<=upper2 && flag[i+1][j2]==1)
						{
							if (  (upper1>=lower2 && lower1<=lower2) || (lower1<=upper2 && lower1>=lower2 )   )
							{
								//ans++;
								index=j2+1;
								flag[i][j1]=1;
								//ok=true;
								break;
							}
						}
					}
				}
			}
			
			int ans=0;
			for (int i=0; i<P; i++)			
			{
				ans=ans+flag[0][i];
			}
			
			cout<<"Case #"<<cnt<<": "<<ans<<endl;
		}
	}
	
	
	
	
	return 0;
	
}
