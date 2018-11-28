#include<iostream>
using namespace std;
int main()
{  int T;
cin>>T;
int p =1 ;
for(p;p<=T;p++)
    {int N;int c;
    cin>>N;
    for(int i=N;i>0;i--)
    {
        int m=i;
        int j=9;
        do
        {
            int r=j;
            j=(int)(m%10);
            if(r>=j)
                c=1;
            else
                c=0;
            m=m/10;
        }while((m>0)&&(c==1));
        if(c==1)
        {
            cout<<"case #"<<p<<": "<<i<<"\n";
            break;
        }
    }
}
}
