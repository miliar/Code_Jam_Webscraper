

#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <list>
#include <cstring>
#include <math.h>

using namespace std;

typedef long long int lli;
typedef unsigned long long int ulli;
typedef long double ld;

int main() {

    int t;
    cin >> t;

    for(int num=0;num<t;num++)
    {
        string s;
        int k,flag=0,ans=0;
        cin >> s;
        cin >> k;

        int len = s.size();

        for(int i=0;i<len;i++)
        {
            if(s[i]=='-')
            {
                int p=i;
                if(k>len-i)
                {
                    flag=1;
                    break;
                }
                else
                {
                    ans++;
                    int m=k;
                    int change=0;
                    for(int j=i;m!=0;j++,m--)
                    {
                        if(s[j]=='-')
                            s[j]='+';
                        else
                        {
                            s[j]='-';
                            if(change==0)
                            {
                                i=j-1;
                                change=1;
                            }
                        }
                    }
                    if(change==0) i+=(k-1);
                }

            }
        }

        if(flag==1)
            cout << "Case #" << num+1 << ": " <<  "IMPOSSIBLE" << endl;
        else
            cout << "Case #" << num+1 << ": " <<  ans << endl;

    }

    return 0;
}


