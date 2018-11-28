#include<iostream>
#include<stdlib.h>
#include<string>
#include<stdio.h>

using namespace std;

int check(int n)
{
    int a,b;
    a=n%10;
    n=n/10;
    if(n==0)
        return 1;
    else{
    while(n!=0)
    {
        b=n%10;
        if(b>a)
        {
            return 0;
        }
        a=b;
        n=n/10;
    }
    if(n==0)
    return 1;
    }
}

int test(int n)
{
    int c,c1;
    if(n==1)
        return 1;
    else{
    for(int i=n;i>1;i--)
    {
        c=check(i);
        if(c==1){
            c1=i;
            break;
        }
        else
            continue;
    }
    return c1;
    }
}

int main()
{
    int no_cases;
    freopen( "B-small-attempt1.in", "r", stdin );
	freopen( "outputsmall.txt", "w", stdout );
    cin>>no_cases;

    for(int i=0;i<no_cases;i++)
    {
        int nos_test;
        cin>>nos_test;

        int res;
        res=test(nos_test);
        cout<<"Case #"<<i+1<<": "<<res<<endl;
    }
    return 0;


}















