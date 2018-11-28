#include<iostream>
#include<cstring>
using namespace std;

int check(char * s)
{
    int con=1;
for(int i=0;i<=strlen(s);i++)
{
    if(s[i]=='-')
    {
        con=0;
    }

}

return con;

}

void rearrange(char * a,int n,int& count1,int k)
{

    if(n+k<=strlen(a))
    {


    for(int j=n;j<n+k;j++)
    {
        if(a[j]=='-')
        {
            a[j]='+';
        }
        else
        {
            a[j]='-';
        }


    }
    count1=count1+1;

    }



}
int main()
{
    int t,x=-2;

    cin>>t;
    for(int i=1;i<=t;i++)
    {
        int count1=0,k;
        char* s= new char[1010];
        cin>>s;
        cin>>k;
        int len =strlen(s);
        for(int j=0;j<=len;j++)
        {
            if(s[j]=='-')
            {
                x=j;
                rearrange(s,j,count1,k);


            }

        }




         if(x==-2)
        {
         cout<<"Case #"<<i<<": "<<count1<<"\n";
        }
        else
        {

        if(check(s))
        {

        cout<<"Case #"<<i<<": "<<count1<<"\n";

        }
         else
        {cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<"\n";}




    }
    for(int k=0;k<=len;k++)
        { s[k]='\0';}
    }
    return 0;
}
