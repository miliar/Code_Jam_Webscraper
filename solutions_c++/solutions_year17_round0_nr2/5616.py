#include<iostream>
#include<string>
#include<vector>

using namespace std;

char previous(char c)
{
    int c_int = c - '0';
    c_int--;
    char res = c_int + '0';
    return res;
}

int main()
{
    int T;
    cin >> T;
    for(int cases = 1; cases <= T; cases++)
    {
        cout << "Case #" << cases << ": ";
        string s;
        cin >> s;
        unsigned int cur_pos = 0;
        while(cur_pos < s.size() - 1 && (s[cur_pos] <= s[cur_pos + 1]))
            cur_pos++;
        if(cur_pos == s.size() - 1 || s.size() == 1)
            cout << s << endl;
        else
        {
            if(s[cur_pos] == '0')
            {
                while(s[cur_pos] == '0')
                    cur_pos--;
            }
            else
            {
                while(cur_pos > 0 && s[cur_pos] == s[cur_pos - 1])
                    cur_pos--;
            }
            if(cur_pos == 0 && s[cur_pos] == '1')
                s.erase(s.begin());
            else
            {
                s[cur_pos] = previous(s[cur_pos]);
                cur_pos++;
            }
            for(unsigned int i = cur_pos; i < s.size(); i++)
                s[i] = '9';
            cout << s << endl;
        }
    }
}
