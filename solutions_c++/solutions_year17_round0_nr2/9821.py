#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int T, N=1;
    scanf("%d", &T);
    
    while(N<=T)
    {
        int num, count=0, j=0, d[1000];
        scanf("%d", &num);
        
        while(num>0)
        {
            int Num1=num, j=0;
            count=0;
            while(Num1)
            {
                d[j]= Num1 % 10;
                Num1 /= 10;
                j++;
            }
            for(int i=0; i<j-1; i++)
            {
	            int k=i+1;
                if(d[i]<d[k])
                {
                    count++;
                    break;
                }
            }
            if(count==0)
            {
                cout << "Case #" << N << ": " << num << endl;
                break;
            }
        num--;
        }
    N++;
    }
return 0;
}