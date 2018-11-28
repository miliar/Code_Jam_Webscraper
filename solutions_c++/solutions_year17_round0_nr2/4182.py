#include<bits/stdc++.h>
using namespace std;


void get_digits(unsigned long long N,vector<int>& digit)
{
    int i = 0;
    while(N)
    {
        int d = N%10;
        digit.push_back(d);
        N = N/10;
    }
    reverse(digit.begin(),digit.end());
}

int main()
{

    int T;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    cin>>T;

    for(int t=1;t<=T;t++)
    {
        unsigned long long N;
        cin>>N;
        vector<int>digits;
        get_digits(N,digits);
        for(int i=1;i<digits.size();i++)
        {
            int d = digits[i];
            if(d<digits[i-1])
            {
                int j = i-1;
                while(j>=1)
                {
                    if(digits[j]-1>=digits[j-1])
                    {
                        break;
                    }
                    j--;
                }
                digits[j]--;
                i = j+1;
                while(i<digits.size())
                {
                    digits[i] = 9;
                    i++;
                }
            }
        }
        unsigned long long ans = 0;
        unsigned long long l = 1;
        for(int i = digits.size()-1;i>=0;i--)
        {
            ans = ans + l*digits[i];
            l = l * 10;
        }
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }
    return 0;
}
