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


const int M=1000+5;

long long int K[M];
long long int S[M];


int main()
{
	
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	
	freopen("A-large.in","r",stdin);
	freopen("output_large.out","w",stdout);
	
	
	int T;
	cin>>T;
	
	for (int cnt=1; cnt<=T; cnt++)
	{
		int D,N;
		cin>>D>>N;
		
		for (int i=0; i<N; i++)
		{
			cin>>K[i]>>S[i];
		}
		
		
		int index=-1;
		for (int i=0; i<N; i++)
		{
			int num=0;
			for (int j=0; j<N; j++)	
			{
				if (j!=i)
				{
					if ( (D-K[i])*S[j] >= (D-K[j])*S[i])
					{
						num++;
					}
				}
			}
			if (num==N-1)
			{
				index=i;
				break;
			}
		}
		
		cout<<"Case #"<<cnt<<": ";
		printf("%.10f\n",1.0*D*S[index]/(D-K[index]));
	}
	
	
	
	
	
	return 0;
	
}
