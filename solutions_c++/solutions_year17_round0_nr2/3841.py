#include <bits/stdc++.h>

using namespace std;
bool check(string test)
{
    for(int i=0; i<test.length()-1; i++)
    {
        if(test[i]!='1')return false;
    }
    if(test[test.length()-1]!='0')return false;
    return true;
}
int main()
{
    int t;
    cin>>t;
    vector <long long>finala;
    while(t>0)
    {
        long long n;
        string test;
        test="";
        cin>>n;
        if(n/10==0)
        {
            finala.push_back(n);
            t--;
            continue;
        }
        while(n!=0)
        {
            test=(char)(n%10+'0')+test;
            n/=10;
        }
        if(check(test))
        {
            long long ans=0;
            for(int i=0; i<test.length()-1; i++)
            {
                ans*=10;
                ans+=9;
            }
            finala.push_back(ans);
            t--;
            continue;
        }
        for(int i=1; i<test.length(); i++)
        {
            if(test[i]<test[i-1])
            {
                while(i>1&&test[i-1]==test[i-2])i--;
                test[i-1]=test[i-1]-1;
                for(int j=i; j<test.length(); j++)
                {
                    test[j]='9';
                }
            }
        }
        long long ans=0;
        for(int i=0; i<test.length(); i++)
        {
            ans*=10;
            ans+=test[i]-'0';
        }
        finala.push_back(ans);
        t--;
    }
    ofstream myfile;
    myfile.open ("solution.txt");
    for(int i=0; i<finala.size(); i++)
    {
        myfile<<"Case #"<<i+1<<": "<<finala[i]<<endl;
        //cout<<"Case #"<<i+1<<": "<<finala[i]<<endl;
    }
    myfile.close();


    return 0;
}
