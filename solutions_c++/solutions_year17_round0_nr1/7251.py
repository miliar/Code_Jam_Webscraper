#include <iostream>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int k=1; k<=t; k++)
    {
        string s;
        int n,c=0;
        cin>>s>>n;
        int l=s.length(),flag=0;
        for(int i=0; i<l; i++)
        {
            if(s[i]=='-')
            {
                if(i+n-1<l)
                {
                    c++;
                for(int j=i;j<i+n;j++)
                {
                    if(s[j]=='-')
                    {
                        s[j]='+';
                    }
                    else
                    {
                        s[j]='-';
                    }
                }
                }
                else
                flag=1;
            }
        }
        
            if(flag==1)
            cout << "Case #" << k << ": " << "IMPOSSIBLE" << endl;
            else 
            cout << "Case #" << k << ": " << c << endl;
    }
    return 0;
}

