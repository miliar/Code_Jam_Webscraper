#include<iostream>
#include<math.h>
using namespace std;

unsigned long long calcTidy(unsigned long long N)
{
	if(N==0)
		return 0;
    unsigned long long soln=0;
    int i;


    int numbdigits=log10(N)+1;

    int a[numbdigits];
    for(i=0;i<numbdigits;++i)
    {
       a[i] =  (N/(unsigned long long)(pow((double)10,(double)(numbdigits-i-1)))) %  10;
    }

    i=0;
    while(i<numbdigits-1)
    {
        if(a[i] <= a[i+1])
            ++i;


        else if(a[i] > a[i+1])
        {
            while(a[i]==a[i-1] && i>=1)
            {
                i--;
            }
            a[i]--;

            for(int j=i+1;j<numbdigits;++j)
            {
                a[j]=9;
            }

        }

    }

 	unsigned long long subsum;

    for(i=0;i<numbdigits;++i)
    {
        subsum = (pow((double)10 , (double)numbdigits-1-i))*a[i];
        soln=soln + subsum;
    }

    return soln;

}

int main()

{
    int T;
	unsigned long long N;
    cin>>T;
    for(int i=1;i<=T;i++)
    {
        cin>>N;
        cout<<"Case #"<<i<<": "<<calcTidy(N)<<endl;
    }

    return 0;
}


