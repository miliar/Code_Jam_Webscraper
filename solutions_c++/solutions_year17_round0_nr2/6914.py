#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    freopen("Input.txt","r",stdin);
    freopen("Output.txt","w",stdout);
    int t;
    cin>>t;
    int tc=0;
    while(t-->0)
    {
        tc++;
        long long int n,x=0;
        cin>>n;
        int r;
        while(n>0)
        {
            r=n%10;
            n=n/10;

            if(n%10 > r ||( n%10 == 0 && n!=0))
            {
                n--;
                long long int y;
                y=0;
                while(x>0)
                {
                    x=x/10;
                    y=10*y+9;
                }
                x=y;
                r=9;
            }

            x=10*x+r;
        }
        n=0;
        while(x>0)
        {
            r=x%10;
            x=x/10;
            n=10*n+r;

        }

        cout<<"Case #"<<tc<<": "<<n<<endl;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
