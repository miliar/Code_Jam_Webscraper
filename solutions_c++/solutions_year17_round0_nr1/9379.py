#include<cstring>
#include<cstdio>
#include<iostream>
using namespace std;
int T;//1<=T<=100
char S[1000];

int main()
{
    freopen("A-large.in","r", stdin);
	freopen("A-large.out","w", stdout);
    int T0;
    cin>>T;
    T0 = T;
    int K,Cou = 0;
    while(T--)
    {
        bool flag = 0;
        Cou = 0;
        cin>>S;
        cin>>K;
        int len = strlen(S);
        for( int i = 0; i<=len-K;++i)
        {
            if(S[i] == '-' )
            {
                Cou++;
                for(int i0 = i ; i0 < len && i0 < i+K ; ++i0)
                {
                    if(S[i0] == '-')
                        S[i0] = '+' ;
                    else
                        S[i0] = '-' ;
                }
            }
        }
        for(int i = 0 ; i < len ; i++)
        {
            if(S[i] == '-')
            {
                flag = 1;
                break;
            }
        }

        if(flag == 1)
            cout<<"Case #"<<T0-T<<": IMPOSSIBLE"<<endl;
        else
            cout<<"Case #"<<T0-T<<": "<<Cou<<endl;
    }



    return 0;
}
