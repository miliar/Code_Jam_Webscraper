#include<bits/stdc++.h>
#define ll long long

using namespace std;
typedef pair<int,int> pii;
//long long int;

int main()
{
    int t;
    cin>>t;
    for(int z=1;z<=t;z++)
    {
        string s;
        cin>>s;
        int n;
        cin>>n;
        int i=0,counter=0,j;
        while(i<=s.length()-n)
        {
            if(s[i]=='-')
            {

                j=i;
                for(int l=1;l<=n&&j<s.length();l++)
                    {
                        if(s[j]=='+')
                            s[j]='-';
                        else
                            s[j]='+';
                        j++;
                    }
                counter++;
            }
            i++;
            //cout<<i<<" "<<endl;
        }
        int flag=0;
        //cout<<s<<endl;
        for(int l=0;l<s.length();l++)
        {
            if(s[l]=='-')
            {
                flag=1;break;
            }
        }
        cout<<"Case #"<<z<<": ";
        if(flag==1)
        {
            cout<<"IMPOSSIBLE"<<endl;
            continue;
        }
        cout<<counter<<endl;
    }
}
