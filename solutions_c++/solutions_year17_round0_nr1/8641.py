#include <bits/stdc++.h>
using namespace std;
int main()
{
    #ifndef ONLINE_JUDGE
        freopen("A-large.in","r",stdin);
        freopen("Output2.txt","w",stdout);
    #endif // ONLINE_JUDGE
    int n;//Number of test cases
    int f;//Number of flips
    int nf;//Number of flips
    cin>>n;
    string x;//input string
    for(int i=0;i<n;i++)
    {
        bool flag=true;//Maybe or Not
        nf=0;
        bool Pancake[1000];//Pancakes
        cin>>x>>f;
        int l=x.size();//Length of string
        for(int j=0;j<l;j++)
        {
            if (x[j]=='+')
                Pancake[j]=1;
            else if (x[j]=='-')
                Pancake[j]=0;
        }
        for(int k=0;k<l;k++)
        {
            if(Pancake[k]==0&&l-k>=f)
            {
                for(int o=k;o<k+f;o++)
                {
                    if(Pancake[o]==true)
                        Pancake[o]=false;
                    else
                        Pancake[o]=true;
                }
                nf++;
            }
        }
        for(int k=0;k<l;k++)
            if(Pancake[k]==0)flag=false;
        if(flag)
            cout<<"Case #"<<i+1<<": "<<nf<<endl;
        else
            cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
    }
    return 0;
}
