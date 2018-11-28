#include <iostream>
#include<string>
#include<algorithm>
using namespace std;

int main()
{
    int c=0,i,t,k,flag,count,j,len;
    string s;
    
    cin >> t;
    for(int tc=1; tc<=t; tc++)
    {
        flag=0;
        count=0;
        cin >> s >> k;
        len=s.length();
        for(i=0;i<len-k+1;i++)
        {
            if(s[i]=='-')
            {
                s[i]='+';
                for(j=i+1;j<i+k;j++)
                {
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                }
                count++;
            }
        }
        for(i=len-k+1;i<len;i++)
        {
            if(s[i]=='-')
                flag=1;
        }
        if(flag==0)
            cout << "Case #"<<tc<<": "<<count << endl;
        else
            cout << "Case #"<<tc<<": "<<"IMPOSSIBLE" << endl;
        
    }
    
    return 0;
}