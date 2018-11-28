/*###########################################################################
				Oversized Pan
############################################################################*/
#include "bits/stdc++.h"
#define ll long long
#define lld long long int
#define ulld unsigned long long int
#define u_ unsigned
#define ui unsigned int
#define mod 1000000007
#define pi 3.14159265

using namespace std;


int main(int argc, char const *argv[])
{
	lld t;
	int casen=1;
	scanf("%lld",&t);
	while(t--){
		string s;
		int k;
		cin>>s>>k;
		bool bl[s.size()], cntbl=true;
		for (int i = 0; i < s.size(); ++i)
		{
			if(s[i]=='+')
				bl[i]=1;
			else if((s[i]=='-'))
				bl[i]=0;
		}
		int cnt=0;

		for (int i = 0; i < s.size(); ++i)
        {
        	if(bl[i]==1)
        		continue;
        	else
        	{
        		if(i+k<=s.size()){
        			for (int j = 0; j < k; ++j)
        			{
        				bl[i+j]=!bl[i+j];
        			}
        			cnt++;
        			i=0;
    			}
        	}
        	
        }

		bool pos=true;
		for (int i = 0; i < s.size(); ++i)
		{
			if(bl[i]==0)
			{
				pos=false;
				break;
			}
		}
		if(pos)
			cout<<"Case #"<<casen<<": "<<cnt<<endl;
		else
			cout<<"Case #"<<casen<<": IMPOSSIBLE"<<endl;

		casen++;
	}

	return 0;
}
