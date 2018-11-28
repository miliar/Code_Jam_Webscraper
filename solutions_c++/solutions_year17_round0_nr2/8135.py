#include <iostream>
#include <string>

using namespace std;

bool check(long long n)
{
    int last = n%10;
    n/=10;
    bool res = true;

    while(n!=0)
    {
        int cur = n%10;
        if(last<cur)
            return false;
        last = cur;
        n/=10;
    }

    return true;
}

char minusOne(char num)
{
    if(num!=0)
        return num-1;
    else
        return '9';
}

string fix(string s,int pos)
{
    for(int i=pos;i<s.size();i++)
        s[i]='9';

    s[pos-1] = minusOne(s[pos-1]);
    for(int i=pos-2;i>=0;i--)
    {
        bool sub = false;
        while(s[i]>s[i+1])
        {
            sub = true;
            s[i+1] = minusOne(s[i+1]);
        }
        if(sub)
            s[i] = minusOne(s[i]);
    }


    string result="";
    int i;
    for(i=0;i<s.size();i++)
        if(s[i]!='0')
            break;
    for(int j=i;j<s.size();j++)
        result.push_back(s[j]);

    return result;
}

string first_partition(long long n)
{
    string s;
    while(n!=0)
    {
        s.push_back((n%10)+'0');
        n/=10;
    }
    reverse(s.begin(),s.end());

    int last = s[0]-'0';
    for(int i=1;i<s.size();i++)
    {
        int cur = s[i]-'0';
        if(cur<last)
        {
            return fix(s,i);
            break;
        }
        last = cur;
    }

    return s;
}

int main()
{
    int t;
    cin >> t;
    for(int test=1;test<=t;test++)
    {
        
        long long n;
        cin >> n;
        cout<<"Case #"<<test<<": ";

        if(check(n))
                cout<<n<<endl;
        else
        {
            cout<<first_partition(n)<<endl;
        }

    }
    return 0;
}

