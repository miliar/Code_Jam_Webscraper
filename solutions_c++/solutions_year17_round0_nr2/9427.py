#include <iostream>
using namespace std;

int main ()
{ 
	int digits[99];
	int a,k,i,r,c=0,t,z=1;
	cin >> t;
	while (z<=t)
	{
	cin >> k;
    for (i=k; i>=1; i--)
    {
            a = i;
            r = 0;
        if (a%10!=0)
        {
            while(a)
            {
            digits[r] = a%10;
            a/=10;
            r+=1;
            }
            r-=1;
            for (int z=r; z>0; z--)
            {
                if(digits[z] <= digits[z-1])
                {
                  c = 1;
               }
               else
               {
                   c = 0;
                   break;
               }
            }
            if(c==1)
            {
                cout << "Case #" << z << ": " << i << endl;
                z++;
                break;
            }
        }

    }
	}
	}