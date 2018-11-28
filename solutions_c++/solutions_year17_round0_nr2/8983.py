#include <bits/stdc++.h>

#define INF_MAX 2147483647
#define INF_MIN -2147483647
#define INF_LL 2000000000000000000LL
#define INF 2000000000
#define EPS 1e-8
#define ll long long
#define mod 1000000007
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define setzero(a) memset(a,0,sizeof(a))
#define setdp(a) memset(a,-1,sizeof(a))
#define IOS ios_base::sync_with_stdio(0)
#define fillArray(a,n) fill_n(a,sizeof(a),n)

using namespace std;


int tests;
string str;
string answer;
int counter;
int main()
{
                freopen("in.in","r",stdin);
              freopen("out.txt","w",stdout);
    IOS;
    cin >> tests;
    bool first = false;
    while(tests--) {
        counter++;
        cin >> str;
        bool solve = false;
        first = false;
        answer.clear();
        for (int i=0 ; i < str.length()-1 ; i++)
        {
            if (str[i]-'0' > str[i+1]-'0')
                solve = true;
        }

        if (solve)
        {
            for (int i=0 ; i < str.length()-1 ; i++)
            {
                if (str[i]-'0' >= str[i+1]-'0')
                {
                    if (!first)
                    {
                        first = true;
                        str[i] = char(((str[i] - '0') - 1) + '0');
                        str[i+1] = '9';
                    }
                    else
                    {
                        str[i+1] = '9';
                        str[i] = '9';
                    }
                }
            }

//            cout << str << endl;
             bool app = false;
                for (int i=0; i < str.length() ; i++)
                {
                if (str[i] != '0')
                    app = true;
                if (app)
                    answer += str[i];
                }
            }
            else
            {
                answer = str;
            }



//        if (str.length() < 2)
//            answer = str;
        cout << "Case #" << counter << ": " << answer;
        if (tests!=0)
            cout << endl;
    }
    return 0;
}
