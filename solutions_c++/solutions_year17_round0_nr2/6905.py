#include<iostream>
using namespace std;
int main()
    {   int t;
        string str;
        cin>>t;
        for(int c=0;c<t;c++)
        {
            cin>>str;
            long long int l=str.length();
            if(l==1)
                    {
                        cout<<"Case #"<<c+1<<": "<<str<<"\n";
                        continue;
                    }
            long long int countS=1,j;
            for(long long int i=0;i<l-1;i++)
            {
                if(str[i]<str[i+1])
                {
                    countS=1;
                    //continue;
                }
                else
                    if(str[i]==str[i+1])
                        countS++;
                else
                {
                    for(j=i+1;j<l;j++)
                        str[j]='9';
                    j=i;
                    while(countS!=1)
                    {
                        str[j]='9';
                        j--;
                        countS--;
                    }
                    str[j]--;
                    break;
                }
            }
            if(str[0]=='0')
                    str.erase(0,1);
            cout<<"Case #"<<c+1<<": "<<str<<"\n";
        }
        return 0;
    }
