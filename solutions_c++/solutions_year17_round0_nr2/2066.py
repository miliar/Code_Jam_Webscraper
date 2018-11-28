#include <bits/stdc++.h>
using namespace std;

#define boost ios_base::sync_with_stdio(0)
#define endl '\n'
#define ll long long
#define ull unsigned long long
#define max(a,b) ((a>b)?(a):(b))
#define min(a,b) ((a<b)?(a):(b))

//constants
#define MAX 100005
#define inf LLONG_MAX
#define MIN INT_MIN
#define PIE 3.141592653589793238

ll mod=1e9+7;
ll gcd(ll a , ll b){return b==0?a:gcd(b,a%b);}



int main()
{
    boost;cin.tie(0),cout.tie(0);

    ifstream input ("B-large.in");
    ofstream output;
    output.open("B-large-output.in");
    if (input.is_open()&& output.is_open())
    {
        int t;
        input>>t;
        string temp;
        getline(input, temp);
        int kl =1;
        while(t--){
            string s;
            getline(input, s);
            int n=s.length();
            for(int i=n-2; i>=0; --i){
                if(s[i]>s[i+1]){
                    s[i]--;
                    for(int j=i+1; j<n; ++j){
                        if(s[j]=='9')
                            break;
                        s[j] = '9';
                    }
                }
            }
            if(s[0]=='0'){
                s = s.substr(1);
            }
            output<<"Case #"<<kl<<": "<<s<<endl;
            ++kl;
        }



        input.close();
        output.close();
    }


    return 0;
}
