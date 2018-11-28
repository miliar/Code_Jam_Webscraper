#include <bits/stdc++.h>
#include <string>
using namespace std;
string NumberToString ( int Number )
{
	stringstream ss;
	ss << Number;
	return ss.str();
}
bool issorted(string s)
{
    bool res = true;
    for(int i = 1; i < s.size(); i++)
        if(s[i] < s[i-1])
            res = false;
    return res;
}
bool isssorted(int s)
{
    string Result;
    ostringstream convert;
    convert << s;
    Result = convert.str();
    //cout << Result.size();
    return issorted(Result);
}
int main()
{
    freopen("B-large.in","rt",stdin);
    freopen("B-large.out","wt",stdout);
    int n;
    cin >> n;
    string s;
    for(int k = 1; k <= n; k++)
    {
        cin >> s;
        int ss = atoi(s.c_str());
        //cout << ss;
//        while(!isssorted(ss))
//        {
//            ss--;
//        }
//
//        cout << ss <<"\t";
        bool flag = true;
        for(int q = 0; q < s.size()*2 && flag; q++)
        {
            int i;
            int flag1 = true;
            for(i = s.size()-2; i >= 0; i--)
                if(s[i] > s[i+1])
                {
                    flag1 = false;
                    break;
                }
            if(!flag1)
            {
                if((s[i] == '1' || s[i] == '0') && i == 0)
                {
                    cout << "Case #" << k << ": ";
                    for(int i = 1; i < s.size(); i++)
                    {
                        cout << '9';
                    }
                    //if(k != n)
                    cout << endl;
                    flag = false;
                }
                else if(s[i] == '0')
                {

                    while(i != 0 && s[i] == '0')
                        i--;
                    if((s[i] == '1' || s[i] == '0') && i == 0)
                    {
                        cout << "Case #" << k << ": ";
                        for(int i = 1; i < s.size(); i++)
                        {
                            cout << '9';
                        }
                        cout << endl;
                        flag = false;
                    }
                }
                else
                {
                    s[i]--;
                    for(int j = i+1; j < s.size(); j++)
                        s[j] = '9';
                }
            }


        }
        if(flag)
        {
            cout << "Case #" << k << ": " << s;
            //if(k != n)
            cout << endl;
        }
//        if(ss != atoi(s.c_str()))
//            cout << "safohisfaiohfsiuahoiadsoihfaouihfdoihadsoiadfdiosjapio\n";

    }
    return 0;
}
