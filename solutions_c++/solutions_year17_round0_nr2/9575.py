//B.TidyNumber - codeJam 2017
#include <bits/stdc++.h>

using namespace std;

#define oo (double)1e10
#define moo -((double)1e12)
#define zer (float)1e-6
#define ll long long
#define lli long long int

int main() {

#ifndef ONLINE_JUDGE
    freopen("input.txt", "rt", stdin);
    freopen("out.txt", "wt", stdout);
#endif



    int t;
    cin >> t;
    for (int itr= 1; itr<=t; itr++) {
        lli n;
        cin >> n;
        string str = to_string(n);

        if(str.size() == 1) {
            cout<<"Case #"<<itr<<": "<<str<<endl;
            continue;

        }

        int prevIdx = -1;
        for (int i = str.size() - 1; i > 0; i--) {

            if (str[i] < str[i - 1] || str[i] == '0'){

                str[i] = '9';
                if(str[i-1] != 0) str[i-1] -= 1;
                if (prevIdx != -1) {

                    for (int j = prevIdx;j>=i+1;j--)
                        str[j] = '9';

                    prevIdx = -1;
                }

            }
            else {
                prevIdx = i;
            }


        }

        if(str[0] == '0'){
            str = string(str.begin()+1, str.end());

        }

        cout<<"Case #"<<itr<<": "<<str<<endl;


    }

//    string s = "85";
//
//    cout<<'8' - '5' <<endl;
//    s[0] -=1;
//    cout<<s[0]<<endl ;
//    s = string(s.begin()+1, s.end());
//    cout<<s<<endl;


}

