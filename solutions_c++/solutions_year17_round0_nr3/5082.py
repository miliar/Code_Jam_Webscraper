#include<bits/stdc++.h>
using namespace std;
#define sc scanint
#define f first
#define s second
#define pb push_back
#define mi 100000007
#define try int t;cin>>t; while(t--)
typedef long long llu;
typedef vector<int> vi;
llu ashty[101];
llu Nun,Kun;
llu nom,tp;
llu dipi[101];


int main()
{
	int tl,test;
	scanf("%d",&test);
	for(tl=1;tl<=test;tl++)
	{
		scanf("%lld",&Nun);
		scanf("%lld",&Kun);
		ashty[0]=Nun/2;
		int c=-1;

		if(Nun%2==0)
        {
            dipi[0]=1;
        }
		else
        {

            dipi[0]=2;
        }
		nom=Kun;
		while(nom!=0)
		{
			nom=nom/2;
			c++;
		}
		for(int jz=0;jz<c;jz++)
		{
			if(ashty[jz]%2==0)
            {
        dipi[jz+1]=dipi[jz];
            }
			else
            {
    dipi[jz+1]=dipi[jz] + pow(2,jz+1);
            }
        ashty[jz+1]=ashty[jz]/2;
		}


		if(dipi[c]<Kun+1-pow(2,c))
        {
            cout<<"Case #" << tl << ": " << ashty[c]-1;
            cout<<" "<< ashty[c]-1 << endl;
        }
		else if (dipi[c] >= Kun+1 )
        {
            cout << "Case #" <<tl;
            cout<< ": " << ashty[c] << " " << ashty[c] << endl;
        }
		else
        {
            cout << "Case #"<< tl << ": "<<ashty[c]<<" " << ashty[c]-1<<"\n";
        }
	}
	return 0;
}
