#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int t;
    cin>>t;

    for(int i=0;i<t;i++)
    {
        string s;
        cin>>s;
        int flag=0;
        int good;
        int cnt=0;
        int j,z;

        for(j=0;j<s.size()-1;j++)
        {
            if(s[j+1]-48>=s[j]-48)
            {
                if(s[j+1]-48==s[j]-48)
                {cnt++;
                good=s[j]-48;}

                else
                    cnt=0;
            }

            else
            {
                flag=1;
                break;
            }
        }

        if(flag==0)
        {
            cout<<"Case #"<<i+1<<": "<<s<<endl;
        }



         else
         {

           j=j-cnt;
           s[j]=s[j]-1;

            for(int z=j+1;z<s.size();z++)
            {
                s[z]='9';

            }



            vector<char> s2;
            if(s[0]!='0')
            {
                cout<<"Case #"<<i+1<<": "<<s<<endl;
            }

            else
            {   cout<<"Case #"<<i+1<<": ";
                for(z=1;z<s.size();z++)

                {
                    cout<<s[z];
                }
                  cout<<endl;

            }

        }




    }
    return 0;
}
