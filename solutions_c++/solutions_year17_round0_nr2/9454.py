#include<bits/stdc++.h>

using namespace std;

#define std::cout cout;
#define std::cin cin;

int main()
{
	int i,j,t,cases,r,c,flag=1,a[20];
	long long int N,T;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("problem2.out","w",stdout);
	scanf("%d",&cases);
	for(t=1;t<=cases;t++)
    {
	scanf("%lld",&N);
	if(N%10==0)
    {
        N--;
    }
    while(N>0)
    {
        T=N;
        c=0;
        i=0;
        while(T>0)
        {
            a[i]=T%10;
            T/=10;
            c++;
            i++;
        }
        for(i=c-1;i>0;i--)
        {
            if(a[i]>a[i-1])
            {
                flag=0;
                break;
            }
            else
                flag=1;
        }
        if(flag==1)
            break;
        N--;
    }
    printf("Case #%d: %lld\n",t,N);
    }
	return 0;
}
