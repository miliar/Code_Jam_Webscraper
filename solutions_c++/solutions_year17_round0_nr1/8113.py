#include <iostream>
#include <string>

using namespace std;

bool mem[1001][1001];
bool sol[1001];
bool impossible = false;


void populate(int k,int n)
{
    memset(mem,0,sizeof(mem));
    for(int i=0;i<n;i++)
    {
        if(i+k<=n)
        for(int j=i;j<i+k;j++)
            mem[j][i]=true;
    }
/*
    for(int i=0;i<n;i++,cout<<endl)
        for(int j=0;j<n;j++)
            cout<<mem[i][j];
*/
}

bool get(char c)
{
    if(c=='-')
        return 1;
    return 0;
}

void calculate(string s,int k)
{

    int n = s.size();

    sol[0] = get(s[0]);

    for(int i=1;i<=n-k;i++)
    {
        int cur = get(s[i]);
        for(int j=1;j<=k-1;j++)
        {
            if(i-j>=0)
            {
                cur^=sol[i-j];
            }
        }
        
        sol[i] = cur;
        /*
        for(int j=0;j<=i;j++)
            cout<<sol[j];
        cout<<endl;
        */
    }
}

bool check(string s,int k)
{
    int n=s.size();
    for(int i=0;i<=n-k;i++)
    {
        if(sol[i])
        {
            for(int j=i;j<i+k;j++)
            {
                if(s[j]=='-')s[j]='+';
                else s[j] = '-';
            }
            //cout<<s<<endl;
        }
    }
    for(int i=0;i<n;i++)
        if(s[i]=='-')return true;
    return false;


}


int main()
{
    int t;
    cin >> t;
    for(int test=1;test<=t;test++)
    {
        string s;
        int k;

        cin >> s >> k;

        populate(k,s.size());
        calculate(s,k);

        int count=0;
        for(int i=0;i<=s.size()-k;i++)
            count+=sol[i];

        impossible = check(s,k);
        cout<<"Case #"<<test<<": ";
        if(impossible)
            cout<<"IMPOSSIBLE\n";
        else
            cout<<count<<endl;
        
    }
    return 0;
}
