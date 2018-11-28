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


//#define PI 3.1415926

const int M=1000+10;

struct NODE{
	long long int R;
	long long int H;	
}node[M];

int cmp (const void *a, const void *b)
{
	if ((*(struct NODE*)a).R*(*(struct NODE*)a).H>(*(struct NODE*)b).R*(*(struct NODE*)b).H )  
	{
		return -1;
	}
	else
	{
		return 1;
	}
}

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
		int N,K;
		cin>>N>>K;
		
		for (int i=0; i<N; i++)
		{
			cin>>node[i].R>>node[i].H;
		}
		
		qsort(node,N,sizeof(node[0]),cmp);
		
		/*for (int i=0; i<N; i++)
		{
			cout<<"i="<<i<<endl;
			cout<<node[i].R<<" "<<node[i].H<<endl;
		}*/
		
		long long int ans=0;
		long long int cur_R;
		for (int i=0; i<N; i++)
		{
			cur_R=node[i].R;
			long long int ans1=cur_R*cur_R+node[i].R*node[i].H*2;
			//long long int max_R=0;
			int num=0;
			//cout<<"i="<<i<<endl;
					//cout<<node[i].R<<" "<<node[i].H<<endl;
			for (int j=0; j<N && num<K-1; j++)
			{
				if (node[j].R<=cur_R && j!=i)
				{
					/*if (node[j].R>max_R)
					{
						max_R=node[j].R;
					}*/
					ans1=ans1+2*node[j].R*node[j].H;
					num++;
					//cout<<"j="<<j<<endl;
					//cout<<node[j].R<<" "<<node[j].H<<endl;
				}
			}
			if (num==K-1)
			{
				//ans1=ans1+max_R*max_R;
				if (ans1>ans)
				{
					ans=ans1;
				}
				//cout<<"ans="<<ans<<endl;
				//ans=ans1;
			}
		}
		
		
		cout<<"Case #"<<cnt<<": ";
		printf("%.10f\n",1.0*3.1415926*ans);
		
	}
	
	
	
	
	
	return 0;
	
}
