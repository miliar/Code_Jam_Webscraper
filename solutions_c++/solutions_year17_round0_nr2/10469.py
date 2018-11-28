#include <iostream>
using namespace std;

class num
{
    int n, t;
    public:
    void inp()
    {
        cin>>n;
    }
    void calc()
    {
        int i;
        
        for(i=1;i<=n;i++)
        {
           if(tidy(i)==1)
           {
               t=i;
           }
        }
    }
    int tidy(int a)
    {
        int f, d;
        f=1;
        d=9;
        while(a>0)
        {
            if((a%10)<=d)
            {
                d=a%10;
            }
            else
            {
                f=0;
                break;
            }
            a=a/10;
        }
        return f;
    }
    void out(int y)
    {
        cout<<"Case #"<<y+1<<": "<<t<<endl;
    }
};
int main()
{
    int test;
    int c;
    cin>>test;
    num x[test];
    for(c=0; c<test; c++)
    {
        x[c].inp();
    }
    for(c=0; c<test; c++)
    {
        x[c].calc();
        x[c].out(c);
    }
}