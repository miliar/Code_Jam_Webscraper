#include<iostream>
#include<cstdio>
#include<math.h>
using namespace std;
int main()
{
	int T;
	cin >>T;

	for(int i=0; i<T; i++)
	{


		char S[1002];
		memset(S,'\0',sizeof(S));
		cin>>S;
		unsigned long int K;
		cin>>K;

		int len = strlen(S);
		unsigned long long int val = 0;
		unsigned long long int x = pow(2,K) - 1;
		for(int j=len-1; j>=0; j--)
		{

			if(S[j] == '-')
			{
				val += pow(2,len-j-1);
			}
		}

		int flips =0;
		while(val!=0 && len >= K)
		{

			if(val%2 == 1)
			{
				unsigned long long int and1 = val & x;
				unsigned long long int small_val=0;
				for(int z=0;z<K;z++)
				{
					unsigned long long int and2 = and1 & 1;

					if((and1 & 1) == 0) {//cout<<"YOG"<<z<<endl;
						small_val += pow(2,z);
					}
					and1>>=1;
				}
				val = val>>K;
				val = val<<K;
				val = val | small_val;

				flips++;

			}
			else
			{
				val >>= 1;
				len--;
			}
		}
		cout<<"Case #"<<i+1<<": ";
		if(val == 0) cout<<flips<<endl;
		else cout<<"IMPOSSIBLE"<<endl;
	
	}

}


