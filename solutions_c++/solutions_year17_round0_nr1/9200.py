#include<iostream>
using namespace std;
int main()
{
    int tc;
    cin>>tc;
    int rcount=0;
    while(tc>0)
    {
        rcount++;
        string s;
        int count =0;
        int flipper;
        cin>>s;
        cin>>flipper;
        for(int i=0;i<s.size()-flipper+1;i++)
        {
            if(s.at(i) == '-')
            {
                count++;
                for(int j=i;j<i+flipper;j++)
                {
                     if(s.at(j) == '-')
                     {
                         s.at(j) = '+';
                     }
                     else{

                        s.at(j) ='-';
                     }
                }
            }
        }
        bool flag=false;
        for(int k=0;k<s.size();k++)
        {
            if(s.at(k) == '-')
            {
                cout<<"Case #"<<rcount<<": IMPOSSIBLE"<<endl;
                flag=true;
                break;
            }

        }
        if(flag==false)
        {
            cout<<"Case #"<<rcount<<": "<<count<<endl;
        }

        tc--;
    }

    return 0;
}
