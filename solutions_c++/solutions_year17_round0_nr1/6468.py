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
    freopen("A-large.in", "r", stdin);
    freopen("A-large-output.txt", "w", stdout);

    int t;
    cin >>t;

    for(int test = 1;test <=t;test++ )
    {

        string s;
        cin >> s;

        int k;
        cin >> k;

        int ans = 0; 

        int i=0,j=s.size()-1;

        int flag = 0;

        while(i<j)
        {

            int chose;

            if(flag==0)
                chose = i;
            else
                chose = j;

            if(s[chose]=='-')
            {
                if(flag==0)
                {
                    if((k+chose)<=s.size())
                    {
                        for(int z=chose;z<chose+k;z++)
                        {
                            if(s[z]=='-')
                                s[z]='+';
                            else
                                s[z]='-';
                        }

                        ans++;
                    }
                }
                else
                {
                    if((chose-k)>=-1)
                    {
                        for(int z=chose;z>chose-k;z--)
                        {
                            if(s[z]=='-')
                                s[z]='+';
                            else
                                s[z]='-';
                        }

                        ans++;
                    }
                }
            }


            if(flag==0)
            {
                i++;
                flag=1;
            }
            else
            {
                j--;
                flag=0;
            }

        }

        int imp_flag = 0;
        
        for(int z=0;z<s.size();z++)
        {
            if(s[z]=='-')
                imp_flag=1;
        }

        if(imp_flag==1)
        cout<<"Case #"<<test<<": "<<"IMPOSSIBLE"<<endl;   
        else
        cout<<"Case #"<<test<<": "<<ans<<endl; 

        //cout << s  << endl;

        //cout << ans << endl;
    }


    
return 0;
}
