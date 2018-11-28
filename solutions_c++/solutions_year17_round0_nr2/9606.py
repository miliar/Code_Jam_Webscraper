#include <bits/stdc++.h>
using namespace std;
#define ull unsigned long long
int main() {
    ull t,n;
    cin>>t;
    for(ull q=0;q<t;q++)
    {
        cin>>n;
        ull ans=0,x,p,c;
        for(ull i=n;i>=0;i--)
        {
            x=i;
            p=x%10;
            x=x/10;
            while(x>0 || c!=0)
            {
                c=x%10;
                if((p<c))
                {
                    break;
                }
                x=x/10;
                p=c;
            }
            if(x==0)
            {
                ans=i;
                break;
            }
        }
        cout<<"Case #"<<q+1<<": "<<ans<<endl;
    }
	return 0;
}
