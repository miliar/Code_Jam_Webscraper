#include <iostream>
#include <string>
#include <stack>
#include <fstream>
#include <algorithm>

using namespace std;

int main()
{
    long long int t;
    int k = 0;
    ifstream in;
    ofstream out;
    in.open("B-large.in");
    out.open("output.out");
    string s;
    bool flag = 0;
    stack <char> st;
    in >> t;
    while(t--)
    {
        flag = 0;
        in >> s;
        reverse(s.begin(),s.end());
        int len = s.size();
        for(int i = 0; i < len; i++)
            st.push(s[i]);

        s = "";
        char c = st.top();
        st.pop();
        while(!st.empty())
        {
            char ch = st.top();
            st.pop();
            if(c > ch && !flag)
            {
                --c;
                if(c == 47)
                    c = '9';
                ch = '9';
                flag = 1;
            }
            else if(c > ch && flag)
                ch = c;
            s += c;
            c = ch;
        }
        s += c;
        if(s[0] == '0')
            s = s.substr(1);

        len = s.size();
        for(int i = 0; i < len; i++)
            st.push(s[i]);

        s = "";
        c = st.top();
        st.pop();
        while(!st.empty())
        {
            char ch = st.top();
            st.pop();

            if(ch > c)
            {
                c = '9';
                --ch;
                if(ch == 47)
                    ch = '9';
            }

            s = c + s;
            c = ch;
        }
        s = c + s;

        if(s[0] == '0')
            s = s.substr(1);
        out << "Case #" << ++k << ": "<< s << endl;
    }
    in.close();
    out.close();
    return 0;
}
