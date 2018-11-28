#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <list>
#include <cmath>
#include <string>

using namespace std;
typedef long long lli;

int main(){
    ofstream a_out ( "example.txt" );
    int t;
    cin>>t;
    int cnt=1;
    while(t--)
    {
        string s;
        cin >>s;
        s.append("9");
        for(int i =0 ; i < s.length()-1;i++)
        {
            if(s[i+1]<s[i])
            {
                s[i]=s[i]-1;
                for(int j =i+1;j<s.length()-1;j++)
                {
                    s[j]='9';
                }
                break;
            }
        }
//        cout<<s<<endl;
        for(int i =0 ; i < s.length()-1;i++)
        {
            if(s[i+1]<s[i])
            {
                int j=0;
                while(s[j]<=s[i+1])
                    j++;
                s[j]=s[i+1];
                for(j++;j<s.length()-1;j++)
                {
                    s[j]='9';
                }
            }
        }
        cout<<"Case #"<<cnt<<": ";        a_out<<"Case #"<<cnt<<": ";

        int i =0;
        while(s[i]=='0')
            i++;
        for( ; i < s.length()-1;i++)
        {
            cout<<s[i];
            a_out<<s[i];
        }
        cout<<endl;
        a_out<<endl;
        cnt++;
    }

}
