#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <cmath>
#include <set>

using namespace std;

int main()
{
    ofstream output("tiny.out");
    int t;
    cin >> t;
    for (int tt=0;tt<t;tt++){
        string n;
        cin >> n;

        for (int i=n.size()-1;i>=1;i--){
            if (n[i]<n[i-1]){
                n[i-1]--;
                for (int j=i;j<n.size();j++)
                    n[j]='9';
            }
        }

        string ans="0";
        for (int i=0;i<n.size();i++){
            if (n[i]!='0'){
                ans=n.substr(i);
                break;
            }
        }


        output << "Case #" << tt+1 << ": "<<ans << endl;



    }


    return 0;
}
