#include <iostream>
#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>
#include <string>

using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large-output.txt", "w", stdout);

    int t;
    cin >>t;

    for(int test = 1;test <=t;test++ )
    {

        string n;
        cin >> n;

        string ans = "";

        int flag =0;

        ans += n[0];

        for(int i=1;i<n.size();i++)
        {
            if(n[i]<n[i-1])
            {

                    ans[i-1]--;

                    for(int j=i;j<n.size();j++)
                        ans += '9';

                    if(i>=2)
                    {
                        if(ans[i-2]>ans[i-1])
                        {
                            char temp = ans[i-2];

                            ans[i-1]='9';

                            for(int j=i-2;j>0;j--)
                            {
                                if(ans[j]==temp && ans[j-1]<temp)
                                    ans[j]=temp-1;
                                else if(ans[j]==temp)
                                    ans[j]='9';

                            }

                            if(ans[0]==temp)
                                ans[0]--;

                        }
                    }

                    flag = 1;
                    break;
                
                if(flag==1)
                    break;

            }
            else
            {
                ans+=n[i];

                 if(flag==1)
                    break;
            }

            
        }

        if(ans[0]=='0')
        {
            string s2 = ans;

            ans = "";

            for(int i=1;i<s2.size();i++)
                ans+=s2[i];
        }
        
        cout<<"Case #"<<test<<": "<<ans<<endl;   
        


    }


    
return 0;
}
