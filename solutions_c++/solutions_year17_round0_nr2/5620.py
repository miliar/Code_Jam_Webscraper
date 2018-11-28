#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;


int main() {

    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int t;
    cin >> t;
    for(int test=0;test<t;test++)
    {
        string s;
        cin >> s;
        int l=s.size();
        for(int i=l-1;i>0;i--)
        {
            if(s[i]=='0')
            {
                if(s[i-1]!='0') s[i-1]--;
                for(int j=i;j<l;j++) s[j]='9';
            }
            else if(s[i]<s[i-1])
            {
                s[i-1]--;
                for(int j=i;j<l;j++) s[j]='9';
            }
        }
        if(s[0]=='0') s = s.substr(1);
        cout << "Case #"<<test+1<<": "<< s << endl;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
