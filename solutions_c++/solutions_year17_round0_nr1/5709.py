#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <math.h>
using namespace std;

int main() {
	freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
	int t;
    cin>>t;
    for(int cases=1;cases<=t;++cases)
    {
        string s;
        int k;
        cin>>s;
        cin>>k;
        int ans = 0, n=s.length();
        for(int i=0;i<=n-k;++i)
        {
            if(s[i] == '-')
            {
                for(int j=i;j<i+k;++j)
                {
                    if(s[j] == '-')
                        s[j] = '+';
                    else
                        s[j] = '-';
                }
                ans++;
            }
            //cout<<s<<endl;
        }
        int f=0;
        for(int i=n-k;i<n;++i)
        {
            if(s[i]=='-')
            {
                f=1;
                break;
            }
        }
        if(f==0)
            cout<<"Case #"<<cases<<": "<<ans<<endl;
        else
            cout<<"Case #"<<cases<<": IMPOSSIBLE"<<endl;
    }
  return 0;
}
