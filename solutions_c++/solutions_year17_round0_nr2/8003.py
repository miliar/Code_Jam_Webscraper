#include<bits/stdc++.h>
using namespace std;



int main()
{


   long long int t,temp=0,num=0;
    cin>>t;
    long long int n;
    char r;
    for(int i=1;i<=t;i++)
    {



        cin>>n;
        int f=0;
        stringstream ss;
        ss<<n;
        int s=0;
        string st=ss.str();
        temp=0,num=0;
       long long int sz=st.size();


        for(int g=0;g<sz-1;g++)
        {
            if(st[g]>st[g+1])
            {
                s=1;
                break;
            }
        }
        reverse(st.begin(),st.end());

        if(s==1)
        {


        for(int j=0;j<sz-1;j++)
        {

            if( (st[j+1]-'0'==0) )
            {
                st[j]='9';


            }




            else
            {
                st[j]='9';

                r=st[j+1];

                temp=r-'0';

                temp=temp-1;

                r=temp+'0';
                st[j+1]=r;


            }

        for(int g=0;g<sz-1;g++)
        {
            if(st[g]<st[g+1])
            {
                f=1;

            }
        }
        if(f==0)
        {
            break;
        }

f=0;

        }


         reverse(st.begin(),st.end());
         istringstream iss(st);
         iss>>num;
         cout<<"Case #"<<i<<": "<<num<<endl;

        }

        else
    {
        cout<<"Case #"<<i<<": "<<n<<endl;

    }

    }



    return 0;
}
