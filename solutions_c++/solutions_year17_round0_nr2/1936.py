#include <bits/stdc++.h>

using namespace std;

int check(int n)
{
    vector <int> tmp;
    while(n)
    {
        tmp.push_back(n%10);
        n/=10;
    }
    reverse(tmp.begin(),tmp.end());
    for (int i=1; i<tmp.size(); i++)
    {
        if (tmp[i]<tmp[i-1])
            return 0;
    }
    return 1;
}

int brute(int n)
{
    for (int i=n; i>=1; i--)
    {
        if (check(i))
            return i;
    }
}

long long stoll( string s)
{
    long long ans=0;
    for (int i=0; i<s.size(); i++)
    {
        ans *= 10;
        ans += s[i]-'0';
    }
    return ans;
}

string solve(long long n)
{
    vector <int> digit;
    while(n)
    {
        digit.push_back(n%10);
        n/=10;
    }
    reverse(digit.begin(),digit.end());

    vector <int> suff(digit.size());
    suff[ (int)digit.size()-1 ]=digit.back();
    for (int i=(int)digit.size()-2; i>=0; i--)
    {
        suff[i]=min(suff[i+1],digit[i]);
    }

    int f=0;
    int prev_pos=0;

    string ans;
    for (int i=0; i<digit.size()-1; i++)
    {
        if (f)
        {
            ans+='9';
        }
        else
        {

            if (digit[i]<digit[i+1])
                ans+= '0' + digit[i];
            else if (digit[i]==digit[i+1])
            {
                if (digit[prev_pos]!=digit[i])
                    prev_pos=i;
                ans += '0' + digit[i];
            }
            else
            {
                if (digit[prev_pos] == digit[i] )
                {
                    ans[ prev_pos ]--;
                    prev_pos++;
                    while(prev_pos<ans.size())
                    {
                        ans[ prev_pos ] = '9';
                        prev_pos++;
                    }
                    if (i)
                        ans+='9';
                    else
                    {
                        if (digit[i]>1)
                            ans+= '0' + digit[i] - 1;
                    }
                    f=1;
                }
                else
                {
                    ans += '0' + digit[i] - 1;
                    f=1;
                }

            }
        }
    }
    if (f)
        ans+= '9';
    else
        ans+= '0' + digit.back();
    return ans;
}


int main()
{
    ios_base::sync_with_stdio(false);
    ifstream cin("B-large.in");
    ofstream cout("B-large.out");
    int n;
    cin>>n;
    for (int test=1; test<=n; test++)
    {
        long long x;
        cin>>x;
        cout<<"Case #"<<test<<": "<<stoll( solve(x) )<<'\n';
    }

//    srand(time(0));
//    while(true)
//    {
//        long long n=rand()+1;
//        if ( stoll( solve(n) ) == brute(n) )
//        {
//            cout<<"OK\n";
//        }
//        else
//        {
//            cout<<"ERROR\n";
//            cout<<"n    ="<<n<<'\n';
//            cout<<"brute="<<brute(n)<<'\n';
//            cout<<"solve="<<solve(n)<<'\n';
//            return 0;
//        }
//    }
    return 0;
}
