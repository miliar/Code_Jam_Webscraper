#include<iostream>
#include<stdio.h>

#define li long long
#define ip(x) scanf("%lld", &x)
#define ipi(x) scanf("%d", &x)
#define ipc(x) scanf("%c", &x)
#define op(x) printf("%lld", x)
#define opi(x) printf("%d", x)
#define opc(x) printf("%c", x)
#define ps(x) printf(x)
#define sp(x) printf(#x)
#define nl() printf("\n")

using namespace std;

string correct(li c, string s)
{
    for(li i = c; i < s.length(); i++)
    {
        s[i] = '9';
    }
    s[c-1] = s[c-1] - 1;
    if(s[0] == '0')
    {
        string s1;
        s1.resize(s.size()-1);
        for(li i = 0; i < s.size()-1; i++)
        {
            s1[i] = s[i+1];
        }
        return s1;
    }
    return s;
}

int check(string s)
{
    for(li i = 1; i < s.size(); i++)
    {
        if(s[i] >= s[i-1])
        {
            continue;
        }
        else
        {
            return i;
        }
    }
    return -1;
}

int main()
{
    freopen("B-small-attempt2.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    li t;
    ip(t);
    li k = 1;
    while(t--)
    {
        string s, s1, s2;
        cin >> s;
        li c = check(s);
        //cout << c << endl;
        if(c == -1)
            cout << "case #" << k <<": " << s << "\n";
        else
        {
            s1 = correct(c, s);
            //cout << s1 << endl;
            li d = check(s1);
            if(d == -1)
                cout << "case #" << k <<": " << s1 << "\n";
            else
            {
                //cout << s1 << endl;
                s1[0] -= 1;
                for(li i = 1; i < s1.length(); i++)
                {
                    s1[i] = '9';
                }
                if(s1[0] == '0')
                    for(li i = 1; i < s1.length(); i++)
                        cout << "case #" << k <<": " << s1[i];
                else
                {
                    cout << "case #" << k <<": " << s1;
                }
                nl();
            }
        }
        k++;
    }
    return 0;
}
