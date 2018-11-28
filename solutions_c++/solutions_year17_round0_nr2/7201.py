#include<iostream>
#include<string>
#include<cstdlib>
using namespace std;
char neg(char c)
{
    int a=(int)c-48-1;
    char ch='0'+a;
    return ch;
}
int ctoi(char c)
{
    int a=(int)c-48;
}
bool istidy(string n)
{
    for(long long i=0;i<n.length()-1;i++)
    {
        if(ctoi(n[i])>ctoi(n[i+1]))
            return false;
    }
    return true;
}
int main()
{
    int t,ni;
    string n;
    cin>>t;
    int k=0;
    while(t--)
    {
        k++;
        cin>>n;
        cout<<"Case #"<<k<<": ";
        while(!istidy(n))
        {
            for(int i=0;i<n.length()-1;i++)
            {
                if(ctoi(n[i])>ctoi(n[i+1]))
                {
                    n[i]=neg(n[i]);
                    for(int j=i+1;j<n.length();j++)
                        n[j]='9';
                }
            }
        }
        cout<<atoll(n.c_str())<<'\n';
    }
    return 0;
}
