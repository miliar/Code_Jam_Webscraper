#include <bits/stdc++.h>

using namespace std;

string to_string(long long a)
{
    stringstream ss;
    ss << a;
    string ret;
    ss >> ret;
    while(ret.size()>0 && ret[0]=='0') ret=ret.substr(1, ret.size()-1);
    return ret;
}


int main()
{
    freopen("inp.in", "r", stdin);
    freopen("outp.out", "w", stdout);
    ios::sync_with_stdio(false);
    int tc;
    cin >> tc;
    for(int case_no=1; case_no<=tc; case_no++)
    {
        cout << "Case #" << case_no << ": ";
        //printf("Case #%d: ", case_no);
        string num_as_string;
        cin >> num_as_string;
        int n=num_as_string.size();
        vector<bool> increasing(n, false);
        increasing[0]=true;
        for(int i=1; i<n; i++)
        {
            if(num_as_string[i]>=num_as_string[i-1] && increasing[i-1]) increasing[i]=true;
        }
        if(increasing[n-1])
        {
            cout << num_as_string << endl;
            continue;
        }

        int first_false_idx=-1;
        for(int i=0; i<n; i++)
        {
            if(!increasing[i])
            {
                first_false_idx=i;
                break;
            }
        }

        long long before = atoll(num_as_string.substr(0, first_false_idx).c_str());
        string before_as_string = to_string(before);
        int first_same_idx=-1;
        for(int i=before_as_string.size()-1; i>=0; i--)
        {
            if(before_as_string[i]==before_as_string[before_as_string.size()-1]) first_same_idx=i;
            else break;
        }

        string part = before_as_string.substr(0, first_same_idx+1);  // don't forget to delete zero's from the start
        long long num = atoll(part.c_str());
        num--;
        long long actual_n = atoll(num_as_string.c_str());
        while(num <= (actual_n-9)/10) // 10*before+9 <= actual_n, attention for overflow
        {
            num=10*num+9;
        }
        cout << num << endl;
    }
    return 0;
}
