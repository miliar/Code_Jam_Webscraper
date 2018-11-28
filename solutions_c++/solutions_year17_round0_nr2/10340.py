#include <iostream>
#include <iostream>
#include <fstream>
using namespace std;
int pow(int b,int p)
{
    int i,q=b;
    if(p==0)
    {
        return 1;
    }
    for(i=p;i>=2;i--)
    {
        q=q*b;
    }
    return q;
}

int tidy(int n)
{
    int *x;
    int i,j,q;
    if(n==0)
    {
        i=1;
        goto a;
    }
    for(i=0;;i++)
    {
        q=n/pow(10,i);
        if(q==0)
            break;
    }
    a:
    x=new int [i];
    q=n;
    for(j=i-1;j>=0;j--)
    {
        x[i-1-j]=q/pow(10,j);
        q=q-x[i-1-j]*pow(10,j);
    }
    for(j=0;j<=i-2;j++)
    {
        if(x[j]<=x[j+1])
            continue;
        else return 0;
    }
    return 1;
}
int main()
{
    //tidy numbers
    int t,i,j,k,q,temp,n;
    ifstream myfile ("B-small-attempt2.in");
    if (myfile.is_open())
    {
        myfile>>t;
    }

    else cout << "Unable to open file";
    ofstream output ("example.in");
    for(i=1;i<=t;i++)
    {
        myfile>>n;
        temp=n;
        for(temp=n;temp>=0;temp--)
        {
            if(tidy(temp)==1)
                break;
        }
        output<<"Case #"<<i<<": "<<temp<<endl;
    }
    output.close();
    return 0;
}
