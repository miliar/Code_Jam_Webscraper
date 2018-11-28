#include<bits/stdc++.h>
using namespace std;
int main()
{
    int T,i,t=1;
    cin>>T;
    while(T--)
    {
       int count=0;
        char S[1005];
        int K,k,flag=0;
        scanf("%s",S);
        cin>>K;
        int N=strlen(S);
        for(i=0;i<N;i++)
        {
            if(S[i]=='-'&&(i+K)<=N)
                {
                    count++;
                    for(k=i;k<i+K;k++)
                    {

                        if(S[k]=='-')
                            S[k]='+';
                        else
                            S[k]='-';
                    }
                }
            if(S[i]=='-')
                flag=1;
        }
        if(flag==1)
        cout<<"Case #"<<t<<": IMPOSSIBLE\n";
        else
            cout<<"Case #"<<t<<": "<<count<<endl;
            t++;
    }

    return 0;
}
