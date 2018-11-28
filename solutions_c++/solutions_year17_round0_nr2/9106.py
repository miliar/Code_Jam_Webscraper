#include<bits/stdc++.h>
using namespace std;
bool checkTidy(long long num)
{
    int r,temp=num%10;
    num=num/10;
    if(temp==0)
        return false;
    while(num>0)
    {
        r=num%10;
        if(r>temp)
            return false;
        num=num/10;
        temp=r;
    }
    return true;
}
int main()
{
    ifstream fin;
    ofstream fout;

    fin.open("input.in",ios::in);
    fout.open("output.txt",ios::out);

    int t;
    fin>>t;

    for(int i=1;i<=t;i++)
    {
        long long n,j,ans;
        fin>>n;

        if(n<=9)
            fout<<"Case #"<<i<<": "<<n<<endl;
        else
        {
            ans=n/10-1;
            for(j=n;j>0;j--)
            {
                if(checkTidy(j))
                {
                    ans=j;
                    break;
                }
            }
            fout<<"Case #"<<i<<": "<<ans<<endl;
        }
    }
    fin.close();
    fout.close();
    return 0;
}

