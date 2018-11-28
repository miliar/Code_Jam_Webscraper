#include<bits/stdc++.h>
#define f0(s,d) for(int (s) = 0; (s)<(d); (s)++)
#define f1(s,d) for(int (s) = 1; (s)<(d); (s)++)
#define int long long

using namespace std;

bool test(int n)
{
    if(n<10)
        return true;
    string t = "";
    while(n>0)
    {
        t += (n%10) + '0';
        n/=10;
    }
    reverse(t.begin(), t.end());
    for(int i = 1; i<t.size(); i++)
        if(t[i]<t[i-1])
            return false;

    return true;
}

#undef int
int main()
#define int long long
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int T;
    cin>>T;
    for(int z = 1; z<=T; z++)
    {
        int n;
        cin>>n;
        while(n>0)
        {
            if(test(n))
            {
                cout<<"Case #"<<z<<": "<<n<<endl;
                break;
            }
            n--;
        }
    }
}
