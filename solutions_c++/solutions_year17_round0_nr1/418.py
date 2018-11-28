#include <iostream>
#include <string>
using namespace std;
string line;
void reverse(int l,int r)
{
    for(int i = l;i<r;i++)
    {
        if(line[i] == '+')
            line[i] = '-';
        else
            line[i] = '+';
    }
}
bool check()
{
    for(int k = 0;k<line.length();k++)
    {
        if(line[k] == '-')
            return false;
    }
    return true;
}
int main()
{
    int n,c;
    cin >>n;
    for(int i = 1;i<=n;i++)
    {
        int count = 0;
        cin>>line>>c;
        cout<<"Case #"<<i<<": ";
        for(int k = 0;k+c<=line.length();k++)
        {
            if(line[k] == '-')
            {
                count++;
                reverse(k, k+c);
            }
        }
        if(check())
            cout<<count;
        else
            cout<<"IMPOSSIBLE";
        cout<<endl;
    }
}