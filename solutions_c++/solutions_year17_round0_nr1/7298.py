#include<bits/stdc++.h>
using namespace std;

int main()
{

    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,k;
    string s,ss;

    scanf("%d",&t);
    getchar();
    for(int kase = 1; kase <= t; kase++ )
    {
        cin>>s>>k;
        int sz = s.size();
        ss = "";
        for(int i = 0; i < sz; i++ )ss += "+";
        //cout<<ss<<endl;
        long long cnt = 0;

        bool check,ok;
        check = true;
        while(1)
        {
            ok = true;
            if( s == ss )break;
            //cout<<s<<endl;
            int p = 0;
            for(int i = 0; i < sz; i++ )
            {
                if(s[i] == '-')
                {
                    p = i;
                    //cout<<p<<endl;
                    break;
                }
                else if( s[i] == '+' )continue;
            }


            for(int j = p; j < p+k ; j++ )
            {
                if(  j < sz  )
                {
                    //cout<<"j er man "<<j<<endl;
                    if( s[j] == '-')s[j] = '+';
                    else if( s[j] == '+')s[j] = '-';
                }
                else
                {
                    ok = false;
                    break;
                }

            }

            if( ok == false )
            {
                check = false;
                break;
            }
            //cout<<s<<endl;
            cnt++;
            //cout<<cnt<<endl;
        }
        if( check == false )printf("Case #%d: IMPOSSIBLE\n",kase);
        else                  printf("Case #%d: %lld\n",kase,cnt);
    }
}
