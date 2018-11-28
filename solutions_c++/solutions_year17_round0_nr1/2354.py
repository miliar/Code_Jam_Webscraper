#include <bits/stdc++.h>

using namespace std;

#define fo "A.out"

string str;
int k;

char rv(char c)
{
    return (c=='-')?'+':'-';
}

void swapK(int vt, int len)
{
    for (int i=vt; i<=vt+len-1; ++i)
        str[i]=rv(str[i]);
}

int main()
{
    //freopen(fo,"w",stdout);
    int T;
    cin >> T;
    int test=0;
    while (T--)
    {
        test++;
        cin >> str >> k;
        int res=0;
        for (int i=0; i<str.length()-k+1; ++i)
            if (str[i]=='-') swapK(i,k), res++;
        bool xet=false;
        for (int i=0; i<str.length(); ++i) if (str[i]=='-') xet=true;
        printf("Case #%d: ",test);
        if (xet) printf("IMPOSSIBLE\n");
        else printf("%d\n",res);
    }
    //fclose(stdout);
}
