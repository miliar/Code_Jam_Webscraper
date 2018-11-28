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



long long int cal(int k)
{
	long long int ans=1;
	for (int i=0; i<k; i++)
	{
		ans=ans*2;
	}
	return ans;
}


int main()
{
	
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	
	freopen("C-large.in","r",stdin);
	freopen("output_large.out","w",stdout);
	
	int T;
	cin>>T;
	
	for (int cnt=1; cnt<=T; cnt++)
	{
		long long int N;
		long long int K;
		cin>>N>>K;
		
		int k=0;
		while ( cal(k+1)-1 < K)
		{
			k++;
		}
		k--;
		
		long long int x=N;
		for (int i=1; i<=k+1; i++)
		{
			x=x/2;
		}
		
		long long int B=N+1-x*cal(k+1);
		long long left_people=K-(cal(k+1)-1);
		if (N==K)
		{
			cout<<"Case #"<<cnt<<": "<<"0 0"<<endl;
		}
		else
		{
			if (left_people>B)
			{
				x--;
			}
				
			long long int ans1;
			long long int ans2;
			
			if (x%2==0)
			{
				ans1=x/2-1;
				ans2=x/2;
			}
			else
			{
				ans1=ans2=(x-1)/2;
			}
			
			cout<<"Case #"<<cnt<<": "<<ans2<<" "<<ans1<<endl;
			
		}
	}
	
	
	
	
	return 0;
	
}
