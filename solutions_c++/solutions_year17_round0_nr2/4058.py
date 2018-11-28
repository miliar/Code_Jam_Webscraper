#include<bits/stdc++.h>
using namespace std;

unsigned long long int out(unsigned long long int n)
{
    if(n<10)
        return n;
    vector<unsigned long long int>v;
    while(n>0)
    {
        v.push_back(n%10);
        n=n/10;
    }
    int flag=0;
    int temp=v.size()-1;
    for(int i=v.size()-2;i>=0;i--)
    {
        if(flag==0)
        {
            if(v[temp]>v[i])
            {
                v[temp]--;
                v[i]=9;
                flag=1;
            }
            for(int x=temp;x<v.size()-1;x++)
            {
                if(v[x]<v[x+1])
                {
                    v[x]=9;
                    v[x+1]--;
                }
            }
        }
        else
            v[i]=9;
        temp--;
    }
    unsigned long long int ans=0;
    for(int i=v.size()-1;i>=0;i--)
        ans=ans*10+v[i];
    return ans;
}

int main()
{
    ifstream fin ("q2large.in");
    ofstream fout ("q2large.out");
    int tc;
    fin >> tc;
    for(int t=1;t<=tc;t++)
    {
        unsigned long long int n;
        fin >> n;
        fout <<"Case #" << t << ": " << out(n) << endl;
    }
    return 0;
}
