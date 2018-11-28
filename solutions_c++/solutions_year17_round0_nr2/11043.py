#include <iostream>
#include <stdio.h>

using namespace std;

long long int modexp(int x,int n)
{
    long long int res=1;
    while(n>0)
    {
        if(n%2==1)
        {
            res=res*x;
        }
        x=x*x;
        n=n/2;
    }
    return res;
}

int main()
{
   freopen("B-small-attempt5.in","r",stdin);
    freopen("output1.txt","w",stdout);

    int t,out=1;
    cin>>t;
    while(t--)
    {



    long long int num,i=1,value=1,case1=0,in=1,a,f=0,numcopy,ans,res,rem=0,flag=0,count=-1;
    int A[20];
    cin>>num;
    numcopy=num;
    A[0]=numcopy%10;
    while(numcopy!=0)
    {
        a=rem;
        rem=numcopy%10;


        if(i>=2 && value==1)
        {
            A[i-1]=rem;
            if(A[i-1]==A[i-2])
            {
                value=1;
            }
            else
            {
                value=2;
                f=1;
            }
        }



        if(rem>=a && flag==1)
        {
            if(rem>a)
            {
                case1=1;
            }
            count=i;
            in++;
            res=numcopy;
        }


        i++;
        flag=1;
        numcopy=numcopy/10;

    }


//cout<<i<<" "<<in+<<endl;

    res=(res*modexp(10,count-1))-1;
    cout<<"Case #"<<out<<": ";
    if(i==in+1 && f==0 )
    {  cout<<num<<endl;

    }
    else if(count!=-1 && case1==1)
        cout<<res<<endl;
        else
            cout<<num<<endl;

            out++;

    }
    return 0;
}
