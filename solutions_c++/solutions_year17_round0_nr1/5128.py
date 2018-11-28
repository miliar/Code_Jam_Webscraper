#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <cmath>
#include <set>
#include <functional>

using namespace std;

int main()
{
    ofstream output("flip.out");
    int t;
    cin >> t;
    for (int tt=0;tt<t;tt++){
        string s;
        int n;
        cin >> s >> n;

        int ans=0;
        for (int i=0;i<=s.size()-n;i++){
            if (s[i]=='-'){
                ans++;
                for (int j=i;j<i+n;j++)
                    if (s[j]=='-') s[j]='+';
                    else s[j]='-';
            }
        }


        bool done=false;
        for (int i=s.size()-n+1;i<s.size();i++)
            if (s[i]=='-'){
                output << "Case #" << tt+1 << ": "<<"IMPOSSIBLE"<< endl;
                done=true;
                break;
            }



        if (!done)
            output << "Case #" << tt+1 << ": "<<ans<< endl;
    }


    return 0;
}
