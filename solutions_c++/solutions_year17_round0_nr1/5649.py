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
        bool solved=true;
        string s;
        cin >> s;
        int k,c(0);
        cin >> k;
        if(s.size()/2)
        for(int i=0;i<s.size();i++)
        {
            //cout << s << endl;
            if(s[i]=='-')
            {
                if(s.size()-i<k)
                {
                    cout << "Case #"<<test+1<<": IMPOSSIBLE" << endl;
                    solved=false;
                    break;
                }
                else
                {
                    c++;
                    for(int j=i;j<i+k;j++)
                    {

                        if(s[j]=='-') s[j]='+';
                        else s[j]='-';
                    }
                }
            }

        }
        if (solved) cout << "Case #"<<test+1<<": "<< c<<endl;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
