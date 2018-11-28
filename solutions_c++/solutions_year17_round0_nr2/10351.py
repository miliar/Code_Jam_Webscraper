#include <bits/stdc++.h>
#define read(x) freopen("x" , "r" , stdin)
#define write(x) freopen("x", "w" , stdout)
using namespace std;
typedef long long int lli;

int main ()
{
    freopen("in.txt" , "r" , stdin);
    freopen("out.txt" , "w" , stdout);

    int tc;

    cin >> tc;

    for(int t=1;t<=tc;t++){
        lli n;
        cin >> n;

        for(lli i=n;i > 0;i--){
            string a = to_string(i);

            vector <char> v1,v2;

            for(int j = 0;j < a.size();j++){
                v1.push_back(a[j]);
            }
            v2 = v1;

            sort(v2.begin(),v2.end());

            if(v2 == v1){
                printf("Case #%d: %lli\n",t,i);
                break;
            }
        }
    }

    return 0;
}
