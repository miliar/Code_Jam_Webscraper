#include<iostream>
using namespace std;
int main()
    {   int t,k,countans=0;
        string str;
        cin>>t;
        for(int cas=0;cas<t;cas++)
        {
            cin>>str;
            cin>>k;
            countans=0;
            int l=str.length();
            for(int i=0;i<l-k+1;i++)
            {
                if(str[i]=='-')
                {
                    int s=i;
                    for(int co=0;co<k;co++)
                    {
                        if(str[s]=='-')
                            str[s]='+';
                        else
                            str[s]='-';
                        s++;
                    }
                    countans++;
                }
            }
            int pos=1;
            for(int j=l-k+1;j<l;j++)
            {
                if(str[j]=='-')
                {
                    cout<<"Case #"<<cas+1<<": "<<"IMPOSSIBLE\n";
                    pos=0;
                    break;
                }
            }
            if(pos==1)
                cout<<"Case #"<<cas+1<<": "<<countans<<endl;
        }
        return 0;
    }
