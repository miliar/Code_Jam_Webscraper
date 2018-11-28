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

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    li t, l = 1;
    ip(t);
    while(t--)
    {
        string s, s2;
        li k;
        cin >> s;
        s2.resize(s.size());
        s2 = s;
        ip(k);
        li i = 0, c = 0, d = 0;
        while(1)
        {
            if(s[i] == '-')
            {
                if(s.size()-i >= k)
                {
                    c++;
                    //cout << c << endl;
                    for(li g = 0; g < k; g++)
                    {
                        if(s[i] == '-')
                            s[i] = '+';
                        else
                            s[i] = '-';
                        i++;
                        //cout << i << endl;
                    }
                    if(s2 == s)
                    {
                        d = 1;
                        break;
                    }
                    //cout << s << endl;
                    i = i-k;
                }
                else
                {
                    d = 1;
                    break;
                }
            }
            else
            {
                i++;
                if(i == s.size())
                    break;
                continue;
            }
        }
        int e = 0;
        for(i = 0; i < s.size(); i ++)
            if(s[i] == '-' || d == 1)
            {
                cout << "Case #" << l << ": " << "IMPOSSIBLE";
                e = 1;
                break;
            }
            if(e == 0)
            {
                cout << "Case #" << l << ": ";
                op(c);
            }
            l++;
        nl();
    }
    return 0;
}
