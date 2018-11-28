#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,n,k;
    ifstream in_file;
    in_file.open("input1.in");
    ofstream out_file;
    out_file.open("out.in");
    int test_case=1;
    in_file>>t;
    while(t--)
    {
        string s;
        in_file>>s;
        in_file>>k;
        int total_count=0;
        for(int i=0;i<=s.length()-k;i++)
        {
            if(s[i]=='-')
            {
                total_count++;
                n=i+k;
                for(int j=i;j<n;j++)
                {
                    if(s[j]=='-')
                    {
                        s[j]='+';
                    }
                    else
                    {
                        s[j]='-';
                    }
                }
            }
        }
        bool flag=1;
        for(int i=0;i<s.length();i++)
        {
            if(s[i]=='-')
            {
                flag=0;
                break;
            }
        }
        if(flag)
            out_file<<"Case #"<<test_case<<": "<<total_count<<"\n";
        else
             out_file<<"Case #"<<test_case<<": IMPOSSIBLE\n";

             test_case++;

    }
    in_file.close();
    out_file.close();
    return 0;
}
