#include<bits/stdc++.h> //akshita
using namespace std;
long long int nonu,katappa,number,temperature;
long long int dope_shope[101],akshita[101];
int main()
{
	int test,integer;
	scanf("%d",&test);
	for(integer=1;integer<=test;integer++)
	{scanf("%lld",&nonu);scanf("%lld",&katappa);
		int counter=-1;akshita[0]=nonu/2;
		if(nonu%2==0)
            dope_shope[0]=1;
		else
            dope_shope[0]=2;
		number=katappa;
		while(number!=0)
        {
			number=number/2;
			counter++;
        }
		for(int june=0;june<counter;june++)
		{
			if(akshita[june]%2==0)
            {
                dope_shope[june+1]=dope_shope[june];
            }
			else
            {
                dope_shope[june+1]=dope_shope[june] + pow(2,june+1);
            }
			akshita[june+1]=akshita[june]/2;
		}
        if(dope_shope[counter] < katappa + 1 - pow(2,counter))
            printf("Case #%d: %lld %lld\n",integer,akshita[counter]-1,akshita[counter]-1);
		else if (dope_shope[counter]>= katappa+1)
            printf("Case #%d: %lld %lld\n",integer,akshita[counter],akshita[counter]);
		else
            printf("Case #%d: %lld %lld\n",integer,akshita[counter],akshita[counter]-1);
	}
	return 0;
}
