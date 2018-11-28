#include<iostream>
using namespace std;
int tidy()
{
    int N;int c;
    cin>>N;
    for(int i=N;i>0;i--)
    {
        int m=i;
        int j=9;
        do
        {
            int r=j;
            j=m%10;
            if(r>=j)
                c=1;
            else
                c=0;
            m=m/10;
        }while((m>0)&&(c==1));
        if(c==1)
        {
            return i;
            break;
        }
    }
}
int main()
{
    int p;
    cin>>p;
    for(int i=0;i<p;i++)
    {
        int l=tidy();
        cout<<"Case #"<<(i+1)<<": "<<l<<"\n";
    }
}
