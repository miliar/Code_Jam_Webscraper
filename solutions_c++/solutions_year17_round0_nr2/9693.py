#include<iostream>
#include<cstring>
using namespace std;
int main()
{
    int t;
    cin>>t;

    for(int m=1;m<=t;m++)
    {
        string number;
        cin>>number;

        int len=number.length();

        for(int i=len-1;i>0;i--)
        {

            if(number[i-1]<=number[i])
                continue;

            number[i-1]=char(number[i-1]-1);
            for(int j=i;j<len;j++)
                    number[j]='9';


        }
        cout<<endl<<"Case #"<<m<<": ";
        if(number[0]=='0')
        {
            for(int i=1;i<len;i++)
               cout<<number[i];
        }
        else{
           for(int i=0;i<len;i++)
               cout<<number[i];
        }

    }

    return 0;
}

