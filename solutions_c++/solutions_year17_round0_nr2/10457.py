#include<iostream>

using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int n,temp1,N,temp2,diff;
        cin>>n;
        n++;
        again:
            n--;
            N=n;
            diff=2*(n%10);
            do
            {
                temp1=(N%10);
                N=N/10;
                temp2=(N%10);
                if((temp1-temp2)<0)
                {
                    goto again;
                }
            }
            while(N!=0);
            cout<<"Case #"<<(i+1)<<": "<<n<<endl;
    }
    return 0;
}


