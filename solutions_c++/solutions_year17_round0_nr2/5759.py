#include<bits/stdc++.h>
#define ll long long
using namespace std;
#define INF 1000000000000

int main()
{
    ifstream cin; cin.open("B-large.in"); ofstream cout; cout.open("fileout.txt"); //comment while testing.
    ll t;
    cin>>t;
    for(int testcase=1;testcase<=t;testcase++)
    {
        // Solve problem
        string s;
        cin>>s;
        int n = s.length();
        for(int i=0;i<s.length();i++)
        {
            if(s[i] == '0')
            {
                for(int j=i;j<n;j++){
                    s[j] = '9';
                }
                int j;
                for(j=i-1;j>1;j--)
                {
                    if(s[j] > s[j-1])
                    {
                        break;
                    }
                }
                s[j]--;
                for(int k=j+1;k<i;k++)
                    s[k]='9';
            }
        }
        int ro=1;
        while(ro == 1){
            ro=0;
            for(int i=0;i<s.length()-1;i++)
            {
                if(s[i] > s[i+1]){
                    s[i]--;
                    ro=1;
                    for(int j=i+1;j<n;j++){
                        s[j] = '9';
                    }
                }
            }
        }

        if(s[0]=='0'){
                s.erase(s.begin());
        }
        cout<<"Case #"<<testcase<<": "<<s<<endl;
    }
    return 0;
}
