#include<bits/stdc++.h>
using namespace std;

int main()
{
     freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    int t;
    string s;

    scanf("%d",&t);
    getchar();
    for(int kase = 1; kase <= t; kase++ )
    {
        cin>>s;
        //bool check = false;
        for(int i = s.size() - 1; i >= 0 ; i-- )
        {
            //cout<<s[i]<<" "<<s[i-1]<<endl;
            if( s[i] >= s[i-1] )
            {
                continue;
            }
            else
            {
                //check = true;
                //cout<<"i holo "<<i<<endl;
                for(int j = i; j < s.size() ; j++ )
                {
                    s[j] = '9';
                    //cout<<"sob 9 kortesi boro hoar karone "<<s[j]<<endl;
                }
               s[i-1]--;
               //cout<<"komar pore "<<s[i-1]<<endl;
               if( s[i-1] < '0' )
               {
                   s[i-1] = '9';
                   for(int j = 0; j < i-1; j++ )
                   {
                       s[j]--;
                   }
               }

            }
        }

        printf("Case #%d: ",kase);
        for(int k = 0; k < s.size(); k++ )
        {
            if( k ==0 && s[k] == '0')continue;
            cout<<s[k];
        }
        printf("\n");

        //cout<<s<<endl;
    }
}
