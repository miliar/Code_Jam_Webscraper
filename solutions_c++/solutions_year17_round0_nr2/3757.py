#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

long long solve(long long a, bool f)
{
    string s = to_string(a);

    for(int i=s.size()-1;i>0;i--){
        if(s[i-1]-'0' > s[i]-'0'){
            if(s[i-1] == '9' && f){
                s[i-1] -= 1;
            }else if(s[i-1] != '9'){
                s[i-1] -= 1;
            }

            s[i] = '9';
        }
    }

    return stoll(s);
}

int main()
{


    freopen("B-large.in", "r", stdin);
    freopen("b-large.txt", "w", stdout);


    long long t, n;
    string s;

    cin >> t;
    for(int i=1;i<=t;i++){
        cin >> n;

        bool f = true;
        while(1){
            long long num = solve(n, f);
            if(num == n)
                break;
            n = num;

            f = false;
        }

        cout << "Case #"<< i << ": " << n <<'\n';
    }

    return 0;
}
