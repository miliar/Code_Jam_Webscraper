#include <bits/stdc++.h>
using namespace std;

#define output freopen("output.txt","w", stdout)
#define input freopen("input.txt","r", stdin)

vector<int> num;
void pre()
{
    int l=0,m=1;
    for(int i=1; i<100; )
    {
        if(i%10==0)
        {
            l++;
            i+=l;
        }
        else
        {
            num.push_back(i);
            i++;
        }
    }
    for(int i=100; i<1005; )
    {
        if(i%100==0)
        {
            i+=m*10;
            l=(m-1);
            m++;
        }
        else if(i%10==0)
        {
            l++;
            i+=l;
        }
        else
        {
            num.push_back(i);
            i++;
        }
    }
}

int main() {
    // your code goes here

    //output;
    //input;
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    pre();

    int test;
    cin>>test;
    for(int i=0; i<test; i++)
    {
        string s;
        long long int pos, temp, n=0;
        cin>>s;
        for(int i=0; i<s.length(); i++)
        {
            n=(n*10 + (s[i] - '0'));
        }
        if(n<=1000)
        {
            vector<int>::iterator it;
            it=upper_bound(num.begin(), num.end(), n);
            pos=(it-num.begin());
            cout<<"Case #"<<i+1<<": "<<num[pos-1]<<"\n";
        }
        else
        {
            pos=-1;
            for(int j=0; j<s.length()-1; j++)
            {
                if(s[j] > s[j+1]){
                    pos=j+1;
                    break;
                }
            }
            //cout<<pos<<endl;
            if(pos==-1)
                cout<<"Case #"<<i+1<<": "<<s<<"\n";
            else
            {
                for(int j=pos+1; j<s.length(); j++)
                {
                    s[j]='9';
                }
                for(int j=pos; j>=1; j--)
                {
                    if(s[j] < s[j-1])
                    {
                        s[j]='9';
                        s[j-1]=s[j-1] - 1;
                    }
                }
                cout<<"Case #"<<i+1<<": ";
                for(int mm=0;mm<s.length(); mm++)
                {
                    if(s[mm]!='0')
                        cout<<s[mm];
                }
            cout<<"\n";
            }
        }
    }

    return 0;
}
