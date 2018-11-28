#include <map>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>

#define enableFastIO ios_base::sync_with_stdio(false); cin.tie(NULL);
#define inc(i,j,k) for (auto i=j;i<=k;i++)
#define li long int
#define lli long long int

using namespace std;

int main()
{
    //enableFastIO;
    int n, ans = 0;
    cin >> n;
    inc(testcase,1,n) {
        string s;
        int k=0,blanks=0,flips=0;
        cin >> s >> k;
        //cout << "Processing " << s << " with K=" << k << endl;
        for (char c:s) if (c=='-') blanks ++;
        //cout << "Blanks " << blanks << endl;
        if (blanks ==0) ans = 0;
        else {
                int index = 0,flips=0;
                while (index < s.length()){
                    //cout << "Checking " << index << " cakes: " << s  << " flips so far: "<< flips << endl;
                    if (s[index]!='+'){
                        if (index+k>s.length()){ flips = -1; break;}
                        flips++;
                        inc(i,index,index+k-1)
                            s[i] = s[i]=='+'? '-':'+';
                    }
                    index++;
                }
                ans = flips;
        }
        if (ans >=0 )
               cout << "Case #" << testcase << ": " << ans << endl;
        else cout  << "Case #" << testcase << ": IMPOSSIBLE" << endl;
    }
}
