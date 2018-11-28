#include<iostream>
#include<string>
#include<string.h>
using namespace std;
int main()
{

    int t;
    cin>>t;int m=1;
    while(t>0)
    {


        string s;
        cin>>s;int c=0;
        int l=s.size();
        int k;
        cin>>k;
        int i;

        for(i=0;i<=(l-k);i++)
        {

            if(s[i]=='-')
            {   c++;

                int m;
                for(m=i;m<(i+k);m++)
                {

                    if(s[m]=='+')
                        s[m]='-';
                    else
                        s[m]='+';
                }


            }




        }
        int flag=0;
        int x;

        for(x=i;x<l;x++)
        {
            if(s[x]=='-')
            {
                flag=1;
                break;
            }



        }


        cout<<"Case #"<<m<<": ";
        if(flag==0)
        {

            cout<<c<<"\n";
        }
        else
        {


            cout<<"IMPOSSIBLE"<<"\n";
        }




























        t--;m++;
    }





    return 0;
}