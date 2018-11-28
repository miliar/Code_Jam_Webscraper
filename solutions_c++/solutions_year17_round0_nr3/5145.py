#include<bits/stdc++.h>
using namespace std;
#define sc scanint
#define sl scanlong
#define mi 100000007
#define getst(s) getline(cin>>ws,s)
#define MAXA 66457976
typedef long long int lol;
lol Nit;
lol Kit,numit,tempit;
lol dpit[101],arrive[101];
int main()
{
	int tit,it;
	scanf("%d",&tit);
	for(it=1;it<=tit;it++)
	{
		scanf("%lld",&Nit);
		scanf("%lld",&Kit);
		int countit=-1;
		arrive[0]=Nit/2;
		if(Nit%2==0)
        {
            dpit[0]=1;
        }
		else
        dpit[0]=2;
		numit=Kit;
		while(numit!=0)
		{numit=numit/2;
			countit++;
		}
		for(int jit=0;jit<countit;jit++)
		{
			if(arrive[jit]%2==0)
            {
                dpit[jit+1]=dpit[jit];
            }
			else
                dpit[jit+1]=dpit[jit] + pow(2,jit+1);
			arrive[jit+1]=arrive[jit]/2;
		}
		if(dpit[countit]< Kit + 1- pow(2,countit))
        {
            cout<< "Case #" << it << ": "<< arrive[countit]-1 << " ";
            cout<<arrive[countit]-1 << endl;
        }
		else if (dpit[countit] >= Kit+1)
        {cout << "Case #" << it << ": " << arrive[countit] <<" " << arrive[countit]<< endl;
        }
		else
        {cout << "Case #" << it << ": ";
        cout<<arrive[countit]  <<" " << arrive[countit]-1<<endl;
        }
	}
	return 0;
}
