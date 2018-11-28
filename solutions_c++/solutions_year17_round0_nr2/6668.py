#include<bits/stdc++.h>
using namespace std;

string s;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t, n;
    scanf("%d", &t);
    for(int qu = 1; qu <= t; qu++)
    {
        cin>>s;
        n = (int)s.length();
        int j = -1;
        for(int i = 0; i < n - 1; i++)
        {
            if(s[i] > s[i + 1])
            {
                j = i;
                while(j >= 0 && s[j] == s[i])
                    j--;
                j++;
                break;
            }
        }
        if(j == -1)
            cout<<"Case #"<<qu<<": "<<s<<endl;
        else
        {
            printf("Case #%d: ", qu);
            s[j]--;
            for(int i = j + 1; i < n; i++)
                s[i] = '9';
            int i = 0;
            while(s[i] == '0')
                i++;
            for(; i < n; i++)
                printf("%c", s[i]);
            printf("\n");
        }
    }
    return 0;
}
