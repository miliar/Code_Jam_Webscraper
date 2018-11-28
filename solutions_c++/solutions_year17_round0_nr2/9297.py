#include<bits/stdc++.h>
using namespace std;


int main()
{
    int t,tcase=1;
    ifstream cin("inputf.in");
    ofstream cout("output.txt");
    cin>>t;
    while(t--)
    {
        string string1,string2;
        cin>>string1;
        string2=string1;
        int size1=0;
        size1=string1.length();
        sort(string2.begin(),string2.end());
        if(string1==string2)
        {
            cout<<"Case #"<<tcase<<": "<<string1<<endl;
            tcase++;
        }
        else
        {
            int flg=0;
            for(int i=0;i<size1;i++)
            {
                if(flg==1)
                {
                    string1[i]='9';
                }
                if((string1[i]-'0'>=string1[i+1]-'0')&&(flg==0))
                {
                    string1[i]=(char)((string1[i]-1));
                    flg=1;
                }

            }
            int f=0;
            cout<<"Case #"<<tcase<<": ";
            tcase++;
            for(int i=0;i<size1;i++)
            {
                if(string1[i]!='0'||f!=0)
                {
                    f=1;
                    cout<<string1[i];
                }
            }
            cout<<endl;
        }
    }
    return 0;
}
