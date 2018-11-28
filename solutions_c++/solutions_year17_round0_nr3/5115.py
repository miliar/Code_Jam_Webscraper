#include<bits/stdc++.h>
using namespace std;
#define gc getchar
#define mp make_pair
#define f first
#define mi 1000000007
#define itr int t;cin>>t;while(t--)
#define sl scanlong
typedef vector<int> vi;
typedef long long int lolz;
lolz Z,Kool,nzm,tzp;
lolz cute[101];
lolz sweet[101];
int main()
{
	int tool;
	int e;
	scanf("%d",&tool);
	for(e=1;e<=tool;e++)
	{
		scanf("%lld",&Z);
		scanf("%lld",&Kool);
		int co=-1;
		sweet[0]=Z/2;
		if(Z%2==0)
        cute[0]=1;
		else cute[0]=2;
		nzm=Kool;
		while(nzm!=0)
		{nzm=nzm/2;
        co++;
		}
		for(int j=0;j<co;j++)
		{  if(sweet[j]%2==0)
            {cute[j+1]=cute[j];
            }
			else cute[j+1]=cute[j] + pow(2,j+1);
        sweet[j+1]=sweet[j]/2;
		}
		if(cute[co]<Kool+ 1- pow(2,co))
        cout << "Case #" <<e << ": " <<sweet[co]-1 << " "<< sweet[co]-1<< endl;
		else if (cute[co]>= Kool+1 )
        cout << "Case #" <<e << ": " << sweet[co] << " "<< sweet[co]<<"\n";
		else
        {cout << "Case #" <<e<< ": " <<sweet[co];
        cout<<" " <<sweet[co]-1<<"\n";}
	}
	return 0;
}
