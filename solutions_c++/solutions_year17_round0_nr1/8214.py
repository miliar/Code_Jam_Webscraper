#include<iostream>
using namespace std;
int main()
{
    int i,j,t,k,l,result,n,flag;
    string str;
    cin>>t;
    for (i=0;i<t;i++)
    {
        flag=0;
        result=0;
        cin>>str;
        cin>>n;
        for(j=0;j<=str.size()-n;j++)
        {
            if(str.at(j)=='-')
            {
                for(k=0;k<n;k++)
                {
                    if(str.at(k+j)=='+')
                    {
                        str.at(k+j)='-';
                    }
                    else{
                        str.at(k+j)='+';
                    }
                }
                result++;
            }
        }
        for(l=str.size()-n+1;l<str.size();l++)
        {
            if(str.at(l)=='-')
            {
                flag=1;
                break;
            }
        }
        if(flag==1)
        {
            cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
        }
        else{
            cout<<"Case #"<<i+1<<": "<<result<<endl;
        }
        str.clear();
    }
    return 0;
}
