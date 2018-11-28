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
        cin>>s;
        int l=s.size();

            int j;

            char f=s[l-1];
            for(j=l-2;j>=0;j--)
            {


                if(s[j]>f)
                {
                    int k=j+1;
                    for(k=j+1;k<l;k++)
                    {
                        s[k]='9';
                    }
                    int c=s[j];
                    c--;
                    s[j]=c;


                }

                    f=s[j];





            }cout<<"Case #"<<m<<": ";
           if(s[0]=='0')
               {int k;
                   for(k=1;k<l;k++)
                    cout<<s[k];



               }
               else
               {



                   cout<<s;
               }
                 cout<<"\n";





























        t--;m++;
    }





    return 0;
}
