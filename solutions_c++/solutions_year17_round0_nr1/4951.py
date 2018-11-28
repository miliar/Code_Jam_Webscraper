//
#include<iostream>
#include<cmath>
#include<algorithm>
#include<vector>
#include<cstring>
#include<string>
#include<map>
#include<set>
#include<climits>
#include<fstream>
#include<iomanip>
#include<queue>
#include<stack>
#define lli long long

using namespace std;


int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    ifstream cin("input.in");
    ofstream cout("output.out");


    int T;
    cin>>T;

    for(int t1=1;t1<=T;t1++)
    {
        cout<<"Case #"<<t1<<": ";

        string s;
        cin>>s;


        int n,br=0;
        cin>>n;

        for(int i=0;i<s.size();i++)
        {
            if(i+n>s.size())break;

            if(s[i]=='-')
            {
                //cout<<i<<"\n";
                br++;
                for(int j=i;j<i+n;j++)
                {
                    if(s[j]=='-')s[j]='+';
                    else s[j]='-';
                }
            }
        }


        bool l=0;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='-'){l=1;break;}
        }
        if(l==0)cout<<br<<"\n";
        else cout<<"IMPOSSIBLE\n";


    }

    return 0;
}


