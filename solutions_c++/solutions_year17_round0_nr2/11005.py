#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int t,i,j,k=1;
    string n;
    ifstream in;
    ofstream out;
    in.open("abc.txt");
    out.open("abc2.txt");
    in>>t;
    while(t--)
    {
        in>>n;
        if(n.length()==1)
        {
            out<<"Case #"<<k<<": ";
            out<<n<<endl;
            k++;
            continue;
        }
        for(i=0;i<n.length()-1;i++)
        {
            if(n[i]>n[i+1])
            {

                while(i>0 && n[i]<=n[i-1])
                {
                  i--;
                }
                n[i]=n[i]-1;
                while(i<=n.length())
                {
                    i++;
                    n[i]='9';
                }
            }
        }
        for(i=0;i<n.length();i++)
        {
        if(n[i]=='0')
        continue;
        else
        break;
        }
        out<<"Case #"<<k<<": ";
        k++;
        for(j=i;j<n.length();j++)
        {
            out<<n[j];
        }
     out<<endl;
    }
    return 0;
}
