#include <bits/stdc++.h>
#define ll long long
using namespace std;
#define file_input freopen("in.txt","r",stdin)
#define file_output freopen("op.txt","w",stdout)
bool check(ll n)
{
    int f=0;
    int pd=n%10;
    n=n/10;
    while(n!=0)
    {
        int d=n%10;
        n=n/10;
        if(d>pd)
            return false;
        pd=d;
    }
    return true;
}
int main() {
    file_input;
    file_output;
    int test_case;
    cin>>test_case;
    for(int t=1;t<=test_case;t++){
        string st,ans;
        cin>>st;
        int l=st.length();
        if(l==1)
            ans=st;
        else
        {
            int po=-1;
            for(int i=1;i<l;i++)
            {
                if(st[i]<st[i-1])
                {
                    po=i-1;
                    break;
                }
            }
            if(po!=-1)
            {
                while(po>0&&st[po]==st[po-1])
                {
                    po--;
                }
                ans="";
                for(int i=0;i<po;i++)
                    ans=ans+st[i];
                int dd=st[po];
                dd--;
                char ch=dd;
                if(ch!='0')
                    ans=ans+ch;
                for(int i=po+1;i<l;i++)
                    ans=ans+'9';
            }
            else
                ans=st;
        }
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }
	return 0;
}
