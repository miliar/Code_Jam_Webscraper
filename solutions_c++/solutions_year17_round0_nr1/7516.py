#include <bits/stdc++.h>
using namespace std;
int main()
{
    //ofstream myfile;
    //myfile.open ("mycode.txt");
    int t,it=1;
    cin>>t;
    while(t!=0)
    {
    string S;

    int k;
    cin>>S>>k;
    int sum=0,sumnt=0;
    for(int i=0;i<S.length()-k+1;i++)
    {
        if(S[i]=='-')
        {
            sum++;
            for(int j=i;j<i+k;j++)
            {
                if(S[j]=='-')
                    S[j]='+';
                else if(S[j]=='+')
                    S[j]='-';
            }

        }
    }
    for(int i=S.length()-1;i>S.length()-k;i--)
    {
        if(S[i]=='-')
        {
            sumnt=1;
            break;
        }
    }
    if(sumnt==1)
        cout<<"Case #"<<it<<": "<<"IMPOSSIBLE"<<endl;
       // myfile<<"Case #"<<it<<": "<<"IMPOSSIBLE"<<endl;
    else
        cout<<"Case #"<<it<<": "<<sum<<endl;
        //myfile<<"Case #"<<it<<": "<<sum<<endl;
    it++;
    t--;
    }
    //myfile.close();
    return 0;
}
