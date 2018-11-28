#include<iostream>
using namespace std;

int main()
{
    long long int i=0,num;
    int data[18],n,test;
    cin>>test;
    for(int l=1;l<=test;l++)
    {
        cin>>num;
        for(i=17;num;i--)
        {
            data[i]=num%10;
            num/=10;
        }
        i++;
        n=i;
        for(i;i<17;i++)
        {
            if(data[i]>data[i+1])
            {
                data[i]-=1;
                for(int j=i+1;j<18;j++)
                    data[j]=9;
                break;
            }
        }
        //Reverse Logic

        for(i=17;i>n;i--)
        {
            if(data[i]<data[i-1])
            {
                data[i]=9;
                data[i-1]-=1;
            }
        }
        if(data[n]==0)
            n++;
        cout<<"Case #"<<l<<": ";
        for(i=n;i<18;i++)
            cout<<data[i];
        cout<<endl;
    }
}
