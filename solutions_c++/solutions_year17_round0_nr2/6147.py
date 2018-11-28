#include <iostream>
#include <string>
#include <fstream>
#define ll long long
using namespace std;

int main()
{
        int t;
        ifstream cin("c1.txt");
        ofstream cout("c1out.txt");
        cin>>t;
        for(int z = 1; z <= t; z++)
        {
                ll n;
                cin>>n;
                string s1;
                string s = to_string(n);
                int l = s.length();
                bool flag = false;
                for(int i = 0 ; i < l-1 ;i++)
                {
                        if(s[i] > s[i+1])
                        {
                                s[i] = ((s[i] - '0') -1) + '0';
                                for(int j = i+1 ; j < l ;j++)
                                        s[j] = '9';
                                i = -1;
                        }
                }
                int i = 0;
                while(s[i] == '0')
                        s.erase(s.begin());
                cout<<"Case #"<<z<<": "<<s<<endl;
        }
        return 0;
}
