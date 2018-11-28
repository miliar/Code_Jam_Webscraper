#include<bits/stdc++.h>

typedef long long int lli;
using namespace std;

int main()
{
    int T;
    #ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    #endif
    cin>>T;
    for(int j=1;j<=T;j++)
    {
        lli N, T;
        cin>>N;
        T = N;
        int digit[20];
        int d_cnt=1;
        // N = 132
        // digit[] = {2, 3 , 1}
        // Storing the digits in reverse order.
        while(T)
        {
            digit[d_cnt]=T%10;
            T=T/10;
            d_cnt+=1;
        }
        // Starting from last we find the limit till it increases.
        int i, inc_idx=d_cnt-1,lf_idx=-1;
        for(i=d_cnt-2;i>=1;i--)
        {
            if(digit[i] >= digit[i+1])
            {
                inc_idx=i;
            }
            else
                break;
        }
        //cout<<" Inc value = "<<inc_idx<<endl;
        cout<<"Case #"<<j<<": ";
        if(inc_idx == 1)
            cout<<N<<endl;
        else
        {
            //Move to right
            for(i=inc_idx;i<d_cnt-1;i++)
            {
                if(digit[i] == digit[i+1])
                {
                    inc_idx=i+1;
                }
                else
                    break;
            }

            digit[inc_idx]-=1;
            for(i=inc_idx-1;i>=1;i--)
            {
                digit[i]=9;
            }
            lli A=0;
            for(i=d_cnt-1;i>=1;i--)
            {
                A = (A *10) + digit[i];
            }
            cout<<A<<endl;
        }
    }
    return 0;
}
