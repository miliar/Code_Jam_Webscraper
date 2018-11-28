#include<bits/stdc++.h>
//shreyx#1
#define vi vector<int>
#define sd(x) scanf("%d",&x)
#define s(x,y) scanf(x,y)
#define sst(x) scanf("%s",x)

#define ull unsigned long long
#define ll long long
// Problem B: Tidy nombers
using namespace std;

int main()
{
    int t,ca=1,no_of_digits;
    ull n,num,x;
    int i,dig1,dig2;
    sd(t);
    while(ca<=t)
    {
        s("%llu",&n);
        num=n;
        i=0;
        no_of_digits=(int)log10((double)n)+1;
        x=(ull)pow((double)10,no_of_digits-1);
        while(i<no_of_digits-1)
        {
            dig1=(num/x)%10;
            dig2=((num*10)/x)%10;
            if(dig1>dig2)
            {
                num=(num/x)*x-1;
                i--;
                x*=10;
                if(i==-1)
                    break;
            }
            else
            {
                x/=10;
                i++;
            }
        }

        printf("Case #%d: %llu\n",ca,num);
        ca++;
    }
    return 0;
}
