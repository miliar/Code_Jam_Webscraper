/**/
#include <bits/stdc++.h>
#define MAX 21
using namespace std;

int main()
{
    freopen("bL.in", "r", stdin);
    freopen("bL.out", "wt", stdout);
    int t, _t=1;
    scanf("%d\n", &t);
    while(_t<=t)
    {
        
        char str[MAX], buf[MAX]="\0", res[MAX]="\0";
        cin>>str;
        int n = strlen(str), i=1;
        buf[0] = str[0];
        while(1)
        {
            if(i==n)
            {
                if(buf) strcat(res, buf);//res = res + buf;
                memset(buf, '\0', MAX);
                break;
            }
            if(str[i]==buf[0])
            {
                buf[strlen(buf)] = str[i];
                i++;
                continue;
            }
            if(str[i]<buf[0])
            {
                int len = strlen(buf);
                buf[0] = buf[0]-1;
                for(int j=1;j<len;j++)
                    buf[j]='9';
                strcat(res, buf);//res = res + buf;
                memset(buf, '\0', MAX);
                goto fill9s;
            }
            strcat(res, buf);//res = res + buf;
            memset(buf, '\0', MAX);
            buf[0] = str[i];//buf = str[i];
            i++;
        }
        fill9s:if(buf) strcat(res, buf);//res = res + buf;
        while(i!=n)
        {
            strcat(res, "9");//res = res + '9';
            i++;
        }
        printf("Case #%d: ", _t);
        int k = 0, len = strlen(res);
        while(res[k]=='0') k++;
        for(int j = k;j<len;j++)
            printf("%c", res[j]);
        printf("\n");
        _t++;
    }
    return 0;
}
/**/