#include<bits/stdc++.h>
#define ll long long int
#define F first
#define S second
#define M 1000000007
#define SI(x) scanf("%d", &x)
#define PI(x) printf("%d\n", x)
#define SL(x) scanf("%I64d", &x)
#define PL(x) printf("%I64d\n", x)
#define PB push_back
#define MP make_pair

using namespace std;

bool possible(ll n)
{
    vector<int> v;
    while(n>0)
    {
        int x = n%10;
        v.push_back(x);
        n/=10;
    }

    for(int i = 0; i<v.size()-1; i++)
    {
        if(v[i+1]>v[i]) return 0;
    }

    return 1;
}

int main()
{
    freopen("gcj2w.txt","w",stdout);
    freopen("B.in","r",stdin);
    int t;
    cin >> t;
    int x = 1;
    while(t--)
    {
        ll n;
        cin >> n;
        cout << "Case #" << x++ << ": ";
        if(possible(n)) cout << n << endl;

        else
        {
            vector<int> ans;
            vector<int> v;

            while(n>0)
            {
                int x = n%10;
                v.push_back(x);
                n/=10;
            }

            //v.push_back(1);

            reverse(v.begin(), v.end());

            for(int i = v.size(); i>0; i--)
            {
                if(v[i]<0) v[i] = 9;

                if(v[i-1]>v[i])
                {
                    v[i] = 9;
                    v[i-1]--;
                }
            }
            if(v[0]==0) v.erase(v.begin(), v.begin()+1);
            bool f = 0;

            for(int i = 0; i<v.size(); i++)
            {
                if(v[i] == 9) f = 1;
                if(f) v[i] = 9;

                cout << v[i];
            }


            cout << endl;
        }
    }
}
