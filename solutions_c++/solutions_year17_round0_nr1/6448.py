#include<bits/stdc++.h>
using namespace std;
int testCases,testCase,i,k,leng,cnt,tmp;
string str;
int main()
{
    
    cin>>testCases;
    for(testCase=1;testCase<=testCases;testCase++)
    {
        cin>>str;
        cin>>k;
        leng=str.size();
        i=0;
        cnt=0;
        while(i<leng)
        {
            while(i<leng && str[i]=='+')i++;
            if(i<leng && leng-i>=k)
            {
                tmp=k;
                int x=i;
                while(tmp--)
                {
                    if(str[i]=='+')
                        str[i]='-';
                    else
                        str[i]='+';
                    
                    i++;
                }
                i=x;
                cnt++;
            }
            else
                break;
        }
        if(i==leng)
            printf("Case #%d: %d\n",testCase,cnt);
        else
            printf("Case #%d: IMPOSSIBLE\n",testCase);
    }
    return 0;
}
