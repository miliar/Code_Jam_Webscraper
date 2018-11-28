#include <bits/stdc++.h>
#define LL long long
using namespace std;
string str1;
void fun()
{
    char c = '9';
    for(int i=1; i<str1.size(); i++)
    {
        if(!i)break;
        if(str1[i] < str1[i-1])
        {
            for(int j=i; j<str1.size(); j++)
                str1[j] = '9';


            c = str1[i-1];
            c--;
            str1[i-1] = c;
            i-=2;
        }
    }

    if(str1[0] == '0')
    {
        int sz = str1.size()-1;
        string str2="";
        for(int i=0; i<sz; i++)str2+='9';
        str1 = str2;
    }

}
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin>>T;
    for(int tt=1; tt<=T; tt++)
    {
        cin>>str1;
        fun();
        printf("Case #%d: ", tt);
        cout<<str1<<endl;
    }
return 0;
}
