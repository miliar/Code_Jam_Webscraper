#include <iostream>
#include <string.h>
#include <fstream>
using namespace std;



int main()
{
    FILE *fin = freopen("C:/Users/trigfan/Desktop/GoogleCodeJam/0A/A-large.in", "r", stdin);
	FILE *fout = freopen("C:/Users/trigfan/Desktop/GoogleCodeJam/0A/A-large.out", "w", stdout);
    int T;
	cin >> T;
	for(int t = 1; t <= T; t++)
	{
        int L,ans=0,K;
        string X;
        cin>>X;
        cin>>K;
        L=X.length();
        char S[L];
        for(int i=0; i<L; i++)
            S[i]=X[i];
        for(int i=0; i<=L-K; i++)
        {
            if(S[i]=='-')
            {
                for(int j=0; j<K; j++)
                {
                    if(S[i+j]=='-')
                        S[i+j]='+';
                    else
                        S[i+j]='-';
                }
                ans++;
            }
        }
        bool check=true;
        for(int i=0; i<L; i++)
        {
            if(S[i]!='+')
                check=false;
        }
        cout << "Case #" << t << ": ";
        if(check)
            cout<<ans<<endl;
        else
            cout<<"IMPOSSIBLE"<<endl;
	}


    return 0;
}
