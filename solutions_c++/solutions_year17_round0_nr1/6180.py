#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{
        int t,k;
        string s;
        ifstream cin("c3.txt");
        ofstream cout("c3out.txt");
        cin>>t;
        for(int i = 1; i <= t; i++)
        {
                bool status = true;
                int Count = 0;
                cin>>s>>k;
                int l = s.length();
                for(int i = 0 ; i < l ;i++)
                {
                        if(s[i] == '-' and i <= (l-k))
                        {
                                for(int j = i ; j < (i+k) ; j++)
                                {
                                        if(s[j] == '-')
                                                s[j] = '+';
                                        else
                                                s[j] = '-';
                                }
                                Count++;
                        }
                        else if(s[i] == '-' and i > (l-k))
                        {
                                status = false;
                        }
                }
                if(status)
                        cout<<"Case #"<<i<<": "<<Count<<endl;
                else
                        cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
        }
        return 0;
}


